"""
rule_engine.py

Rule-based analysis for phishing URLs.
Works alongside the ML model to improve practical accuracy.
"""


def analyze_rules(features):
    """
    Analyze extracted features and calculate a rule score.

    Parameters
    ----------
    features : dict
        Dictionary containing extracted URL features.

    Returns
    -------
    dict
    """

    score = 0
    reasons = []

    # ------------------------
    # HTTPS
    # ------------------------
    if features["Has_HTTPS"] == 0:
        score += 15
        reasons.append("Uses HTTP instead of HTTPS")

    # ------------------------
    # IP Address
    # ------------------------
    if features["Has_IP"] == 1:
        score += 20
        reasons.append("Uses IP address instead of domain")

    # ------------------------
    # Tiny URL
    # ------------------------
    if features["Tiny_URL"] == 1:
        score += 15
        reasons.append("Uses URL shortener")

    # ------------------------
    # Suspicious Keywords
    # ------------------------
    if features["Contains_Login"] == 1:
        score += 12
        reasons.append("Contains 'login'")

    if features["Contains_Verify"] == 1:
        score += 10
        reasons.append("Contains 'verify'")

    if features["Contains_Update"] == 1:
        score += 10
        reasons.append("Contains 'update'")

    if features["Contains_Bank"] == 1:
        score += 12
        reasons.append("Contains 'bank'")

    if features["Contains_Secure"] == 1:
        score += 8
        reasons.append("Contains 'secure'")

    # ------------------------
    # Long URL
    # ------------------------
    if features["URL_Length"] > 75:
        score += 8
        reasons.append("Very long URL")

    # ------------------------
    # Hyphens
    # ------------------------
    if features["Num_Hyphens"] >= 3:
        score += 6
        reasons.append("Contains many hyphens")

    # ------------------------
    # Dots
    # ------------------------
    if features["Num_Dots"] >= 3:
        score += 6
        reasons.append("Contains many dots")

    # ------------------------
    # Entropy
    # ------------------------
    if features["Entropy"] > 4.2:
        score += 8
        reasons.append("High URL randomness")

    # ------------------------
    # Safe Indicators
    # ------------------------
    if features["Has_HTTPS"] == 1:
        score -= 8

    if features["Has_IP"] == 0:
        score -= 5

    if features["Suspicious_Keyword_Count"] == 0:
        score -= 10

    if features["URL_Length"] < 30:
        score -= 5

    # ------------------------
    # Clamp Score
    # ------------------------
    score = max(0, min(score, 100))

    return {
        "rule_score": score,
        "reasons": reasons
    }