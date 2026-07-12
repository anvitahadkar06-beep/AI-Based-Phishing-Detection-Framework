from urllib.parse import urlparse

# Trusted domains
TRUSTED_DOMAINS = {

    "google.com",
    "github.com",
    "microsoft.com",
    "apple.com",
    "amazon.com",
    "amazon.in",
    "flipkart.com",
    "paypal.com",
    "linkedin.com",
    "facebook.com",
    "instagram.com",
    "twitter.com",
    "x.com",
    "openai.com",
    "chatgpt.com",
    "youtube.com",
    "gmail.com",
    "yahoo.com",
    "wikipedia.org",
    "reddit.com",
    "stackoverflow.com",
    "oracle.com",
    "adobe.com",
    "netflix.com",
    "zoom.us",
    "dropbox.com"

}


def get_domain(url):

    domain = urlparse(url).netloc.lower()

    if domain.startswith("www."):
        domain = domain[4:]

    return domain


def is_trusted(url):

    domain = get_domain(url)

    for trusted in TRUSTED_DOMAINS:

        if domain == trusted or domain.endswith("." + trusted):

            return True, trusted

    return False, domain


if __name__ == "__main__":

    urls = [

        "https://google.com",
        "https://github.com",
        "https://mail.google.com",
        "https://amazon.in",
        "https://paypal-login-secure-update.com",
        "http://secure-login-bank-update.com"

    ]

    for url in urls:

        trusted, domain = is_trusted(url)

        print("=" * 60)
        print("URL :", url)
        print("Domain :", domain)
        print("Trusted :", trusted)