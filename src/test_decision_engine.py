from feature_extractor import extract_features
from decision_engine import decide

urls = [
    "https://google.com",
    "https://github.com",
    "http://secure-login-bank-update.com",
    "http://192.168.1.1/login",
    "https://bit.ly/abc123"
]

for url in urls:

    # STEP 1: Extract features
    features_df = extract_features(url)

    # Convert DataFrame → dict
    features = features_df.to_dict(orient="records")[0]

    # STEP 2: Pass BOTH url + features
    result = decide(url, features)

    print("\n============================================================")
    print("URL:", url)
    print("Prediction:", result["prediction"])
    print("Confidence:", result["confidence"])
    print("Risk:", result["risk"])
    print("Trusted:", result["trusted"])
    print("Rule Score:", result["rule_score"])
    print("Reasons:", result["reasons"])