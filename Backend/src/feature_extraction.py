"""
===========================================================
AI Based Phishing Detection Framework
Feature Extraction Module
===========================================================

This module extracts all machine learning features from a URL.

The same module is used for:
1. Dataset Generation
2. Model Training
3. Flask Backend Prediction

Author: Pranjali Mahadik
===========================================================
"""

import re
import math
import string
import ipaddress

from urllib.parse import urlparse

import pandas as pd


# =========================================================
# URL Shortening Services
# =========================================================

SHORTENING_SERVICES = {

    "bit.ly",
    "tinyurl.com",
    "goo.gl",
    "t.co",
    "ow.ly",
    "buff.ly",
    "is.gd",
    "cutt.ly",
    "rebrand.ly",
    "rb.gy",
    "tiny.cc",
    "adf.ly",
    "shorte.st"

}


# =========================================================
# Suspicious Keywords
# =========================================================

SUSPICIOUS_KEYWORDS = [

    "login",
    "verify",
    "secure",
    "update",
    "bank",
    "signin",
    "confirm",
    "password",
    "wallet",
    "paypal",
    "payment",
    "account",
    "invoice",
    "security",
    "recover",
    "unlock",
    "validate"

]


# =========================================================
# Check if Domain is an IP Address
# =========================================================

def is_ip(domain):

    try:
        ipaddress.ip_address(domain)
        return 1

    except ValueError:
        return 0


# =========================================================
# Shannon Entropy
# Measures randomness of URL
# =========================================================

def calculate_entropy(text):

    if len(text) == 0:
        return 0

    entropy = 0

    for character in set(text):

        probability = text.count(character) / len(text)

        entropy -= probability * math.log2(probability)

    return round(entropy, 4)


# =========================================================
# Count Special Characters
# =========================================================

def count_special_characters(url):

    special = 0

    allowed = string.ascii_letters + string.digits

    for char in url:

        if char not in allowed:
            special += 1

    return special


# =========================================================
# Count Digits
# =========================================================

def count_digits(url):

    return sum(c.isdigit() for c in url)


# =========================================================
# Count Subdomains
# =========================================================

def count_subdomains(domain):

    domain = domain.replace("www.", "")

    parts = domain.split(".")

    if len(parts) <= 2:
        return 0

    return len(parts) - 2


# =========================================================
# Detect URL Shortener
# =========================================================

def is_shortened(domain):

    domain = domain.lower()

    for service in SHORTENING_SERVICES:

        if service in domain:
            return 1

    return 0


# =========================================================
# Count Suspicious Keywords
# =========================================================

def keyword_count(url):

    url = url.lower()

    count = 0

    for word in SUSPICIOUS_KEYWORDS:

        if word in url:
            count += 1

    return count


# =========================================================
# Keyword Presence
# =========================================================

def has_keyword(url, keyword):

    return int(keyword in url.lower())

# =========================================================
# Main Feature Extraction Function
# =========================================================

def extract_features(url):
    """
    Extract all machine learning features from a URL.

    Parameters
    ----------
    url : str
        Website URL

    Returns
    -------
    dict
        Dictionary containing all extracted features
    """

    # -----------------------------
    # Add protocol if missing
    # -----------------------------
    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    parsed = urlparse(url)

    domain = parsed.netloc.lower()

    path = parsed.path

    query = parsed.query

    # -----------------------------
    # Basic Length Features
    # -----------------------------
    url_length = len(url)

    domain_length = len(domain)

    path_length = len(path)

    query_length = len(query)

    # -----------------------------
    # Character Counts
    # -----------------------------
    num_dots = url.count(".")

    num_hyphens = url.count("-")

    num_underscores = url.count("_")

    num_slashes = url.count("/")

    num_digits = count_digits(url)

    num_special = count_special_characters(url)

    # -----------------------------
    # Domain Features
    # -----------------------------
    num_subdomains = count_subdomains(domain)

    has_ip = is_ip(domain)

    has_https = int(parsed.scheme == "https")

    has_at = int("@" in url)

    has_prefix_suffix = int("-" in domain)

    # Extra // after protocol
    has_redirection = int("//" in url[8:])

    tiny_url = is_shortened(domain)

    # -----------------------------
    # Keyword Features
    # -----------------------------
    suspicious_keyword_count = keyword_count(url)

    contains_login = has_keyword(url, "login")

    contains_verify = has_keyword(url, "verify")

    contains_update = has_keyword(url, "update")

    contains_bank = has_keyword(url, "bank")

    contains_secure = has_keyword(url, "secure")

    # -----------------------------
    # Entropy
    # -----------------------------
    entropy = calculate_entropy(url)

    # -----------------------------
    # Feature Dictionary
    # -----------------------------
    features = {

        "URL_Length": url_length,

        "Domain_Length": domain_length,

        "Path_Length": path_length,

        "Query_Length": query_length,

        "Num_Dots": num_dots,

        "Num_Hyphens": num_hyphens,

        "Num_Underscores": num_underscores,

        "Num_Slashes": num_slashes,

        "Num_Digits": num_digits,

        "Num_Special_Chars": num_special,

        "Num_Subdomains": num_subdomains,

        "Has_IP": has_ip,

        "Has_HTTPS": has_https,

        "Has_At_Symbol": has_at,

        "Has_Prefix_Suffix": has_prefix_suffix,

        "Has_Redirection": has_redirection,

        "Tiny_URL": tiny_url,

        "Suspicious_Keyword_Count": suspicious_keyword_count,

        "Contains_Login": contains_login,

        "Contains_Verify": contains_verify,

        "Contains_Update": contains_update,

        "Contains_Bank": contains_bank,

        "Contains_Secure": contains_secure,

        "Entropy": entropy

    }

    return features

# =========================================================
# Convert Features to DataFrame
# Used by ML model for prediction
# =========================================================

def extract_features_dataframe(url):
    """
    Extract features and return them as a pandas DataFrame.

    Parameters
    ----------
    url : str

    Returns
    -------
    pandas.DataFrame
    """

    features = extract_features(url)

    return pd.DataFrame([features])


# =========================================================
# Test Feature Extraction
# =========================================================

if __name__ == "__main__":

    sample_urls = [

        "https://google.com",

        "https://github.com",

        "http://secure-login-bank-update.com",

        "http://192.168.1.1/login",

        "https://bit.ly/abc123",

        "https://paypal-login-secure-update.com",

        "https://amazon.in"

    ]

    for url in sample_urls:

        print("=" * 80)
        print("URL :", url)
        print()

        features = extract_features(url)

        for key, value in features.items():

            print(f"{key:30} : {value}")

        print()