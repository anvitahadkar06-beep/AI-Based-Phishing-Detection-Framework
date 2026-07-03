import math
import re
from urllib.parse import urlparse

import pandas as pd

TINY_URLS = [
    "bit.ly",
    "tinyurl.com",
    "goo.gl",
    "t.co",
    "ow.ly",
    "buff.ly",
    "cutt.ly",
    "is.gd",
    "tiny.cc"
]

KEYWORDS = [
    "login",
    "verify",
    "update",
    "secure",
    "bank"
]


def entropy(text):
    if not text:
        return 0

    probability = [text.count(c) / len(text) for c in set(text)]

    return round(
        -sum(p * math.log2(p) for p in probability),
        4
    )


def extract_features(url):

    parsed = urlparse(url)

    domain = parsed.netloc.lower()

    path = parsed.path

    query = parsed.query

    data = {}

    data["URL_Length"] = len(url)
    data["Domain_Length"] = len(domain)
    data["Path_Length"] = len(path)
    data["Query_Length"] = len(query)

    data["Num_Dots"] = url.count(".")
    data["Num_Hyphens"] = url.count("-")
    data["Num_Underscores"] = url.count("_")
    data["Num_Slashes"] = url.count("/")
    data["Num_Digits"] = sum(i.isdigit() for i in url)

    data["Num_Special_Chars"] = len(
        re.findall(r"[^A-Za-z0-9]", url)
    )

    data["Num_Subdomains"] = max(
        domain.count(".") - 1,
        0
    )

    ip_pattern = r"^\d+\.\d+\.\d+\.\d+$"

    data["Has_IP"] = int(
        bool(re.match(ip_pattern, domain))
    )

    data["Has_HTTPS"] = int(
        parsed.scheme == "https"
    )

    data["Has_At_Symbol"] = int(
        "@" in url
    )

    data["Has_Prefix_Suffix"] = int(
        "-" in domain
    )

    data["Has_Redirection"] = int(
        "//" in url[8:]
    )

    data["Tiny_URL"] = int(
        domain in TINY_URLS
    )

    lower = url.lower()

    count = 0

    for word in KEYWORDS:
        if word in lower:
            count += 1

    data["Suspicious_Keyword_Count"] = count

    data["Contains_Login"] = int("login" in lower)
    data["Contains_Verify"] = int("verify" in lower)
    data["Contains_Update"] = int("update" in lower)
    data["Contains_Bank"] = int("bank" in lower)
    data["Contains_Secure"] = int("secure" in lower)

    data["Entropy"] = entropy(url)

    return pd.DataFrame([data])