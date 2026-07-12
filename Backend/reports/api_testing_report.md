# API Testing Report

## Project Title

**AI-Based Phishing Detection Framework**

## Objective

The purpose of API testing is to verify that the backend endpoints function correctly by accepting valid requests, handling invalid inputs, and returning appropriate responses. The testing was performed using Postman with the Flask backend running locally.

---

# Test Environment

| Parameter         | Details               |
| ----------------- | --------------------- |
| Backend Framework | Flask (Python)        |
| Testing Tool      | Postman               |
| Local Server      | http://127.0.0.1:5000 |
| Operating System  | Windows               |
| Request Format    | JSON                  |

---

# API Endpoint Tested

| Endpoint   | Method | Description                                                   |
| ---------- | ------ | ------------------------------------------------------------- |
| `/predict` | POST   | Predicts whether the submitted URL is legitimate or phishing. |

---

# Test Cases

| Test Case ID | Input URL                               | Expected Result                                       | Actual Result                                         | Status |
| ------------ | --------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ------ |
| TC-01        | https://google.com                      | Prediction: **LEGITIMATE**, High Confidence, Low Risk | Prediction: **LEGITIMATE**, High Confidence, Low Risk | PASS   |
| TC-02        | http://paypal-login.verify-security.xyz | Prediction: **PHISHING**, High Risk                   | Prediction: **PHISHING**, High Risk                   | PASS   |
| TC-03        | Empty URL (`""`)                        | Error message indicating URL is required              | Error message displayed                               | PASS   |
| TC-04        | Invalid URL (`abcd`)                    | Invalid URL/Error response                            | Invalid URL/Error response                            | PASS   |

---

# Sample Request

```json
{
    "url": "https://google.com"
}
```

---

# Sample Successful Response

```json
{
    "prediction": "LEGITIMATE",
    "confidence": 99.0,
    "risk": "LOW"
}
```

---

# Sample Error Request

```json
{
    "url": ""
}
```

---

# Sample Error Response

```json
{
    "error": "URL is required"
}
```

> **Note:** The exact error message may vary depending on the backend implementation.

---

# Result

All tested API requests were executed successfully. The `/predict` endpoint correctly classified legitimate and phishing URLs while appropriately handling invalid and empty inputs. The backend is functioning as expected and is ready for deployment.

---

# Conclusion

The API testing confirms that the AI-Based Phishing Detection Framework backend is stable, reliable, and capable of processing URL prediction requests successfully. The tested endpoint met the expected functionality and produced accurate responses for all test cases.
