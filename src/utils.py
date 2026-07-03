from datetime import datetime


def get_risk_level(probability):

    if probability < 20:
        return "VERY SAFE"

    elif probability < 40:
        return "LOW RISK"

    elif probability < 60:
        return "MEDIUM RISK"

    elif probability < 80:
        return "HIGH RISK"

    return "CRITICAL"


def current_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")