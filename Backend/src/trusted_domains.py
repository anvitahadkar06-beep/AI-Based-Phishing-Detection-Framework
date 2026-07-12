from urllib.parse import urlparse

# Popular trusted domains
TRUSTED_DOMAINS = {

    "google.com",
    "github.com",
    "microsoft.com",
    "amazon.com",
    "amazon.in",
    "apple.com",
    "paypal.com",
    "facebook.com",
    "instagram.com",
    "linkedin.com",
    "openai.com",
    "chatgpt.com",
    "youtube.com",
    "gmail.com",
    "google.co.in",
    "wikipedia.org"

}


def is_trusted(url):

    """
    Returns True if URL belongs to a trusted domain.
    """

    domain = urlparse(url).netloc.lower()

    if domain.startswith("www."):
        domain = domain[4:]

    for trusted in TRUSTED_DOMAINS:

        if domain == trusted or domain.endswith("." + trusted):
            return True

    return False