from prediction import predict_url

urls = [

    "https://google.com",

    "https://github.com",

    "http://secure-login-bank-update.com",

    "http://192.168.1.1/login",

    "https://bit.ly/abc123",

    "https://paypal-login-secure-update.com"

]

for url in urls:

    result = predict_url(url)

    print("\n" + "=" * 60)

    print("URL:", result["url"])

    print("Prediction:", result["prediction"])

    print("Confidence:", result["confidence"])

    print("Probability:")

    print(result["probabilities"])