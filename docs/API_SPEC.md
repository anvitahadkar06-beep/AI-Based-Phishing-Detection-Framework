# 📘 API Specification

## AI-Based Phishing Detection Framework

This document describes the RESTful API exposed by the Flask backend of the **AI-Based Phishing Detection Framework**.

The API enables client applications to submit URLs for phishing analysis, verify backend availability, and monitor service health.

---

# 🌐 Base URL

## Local Development

```
http://127.0.0.1:5000
```

## Production

```
https://<your-render-service>.onrender.com
```

---

# 📋 API Overview

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Returns API information and server status |
| `/health` | GET | Performs a backend health check |
| `/predict` | POST | Analyzes a URL and returns phishing detection results |

---

# 📌 Endpoint Specifications

---

## 1️⃣ Home Endpoint

### Endpoint

```
GET /
```

### Description

Returns basic information about the API and verifies that the backend server is running.

### Request Body

None

### Successful Response (200 OK)

```json
{
    "message": "AI-Based Phishing Detection Backend",
    "status": "Running"
}
```

---

## 2️⃣ Health Check Endpoint

### Endpoint

```
GET /health
```

### Description

Checks whether the backend service is operational.

Useful for deployment monitoring and uptime verification.

### Request Body

None

### Successful Response (200 OK)

```json
{
    "status": "healthy"
}
```

---

## 3️⃣ URL Prediction Endpoint

### Endpoint

```
POST /predict
```

### Description

Analyzes the submitted URL using the hybrid phishing detection engine.

The backend performs:

- URL feature extraction
- Trusted domain verification
- Rule-based phishing analysis
- Machine Learning prediction
- Risk assessment

The final prediction is returned as a JSON response.

---

### Request Headers

```http
Content-Type: application/json
```

---

### Request Body

```json
{
    "url": "https://google.com"
}
```

---

### Successful Response (200 OK)

```json
{
    "url": "https://google.com",
    "prediction": "LEGITIMATE",
    "confidence": 99.0,
    "risk": "LOW",
    "trusted": true,
    "rule_score": 0,
    "reasons": [
        "Trusted domain - safe override"
    ]
}
```

---

### Error Responses

#### Missing JSON Body

**Status Code**

```
400 Bad Request
```

Response

```json
{
    "error": "No JSON data received."
}
```

---

#### Missing URL

**Status Code**

```
400 Bad Request
```

Response

```json
{
    "error": "URL is required."
}
```

---

#### Internal Server Error

**Status Code**

```
500 Internal Server Error
```

Response

```json
{
    "error": "Description of the exception"
}
```

---

# 🔄 Request Flow

```text
Client
   │
   ▼
POST /predict
   │
   ▼
Flask API
   │
   ▼
Feature Extraction
   │
   ▼
Hybrid Decision Engine
   ├──────────────┐
   ▼              ▼
ML Model     Rule Engine
   │              │
   └──────┬───────┘
          ▼
Prediction Response
          │
          ▼
Client
```

---

# 📊 HTTP Status Codes

| Status Code | Meaning |
|-------------|---------|
| 200 | Request processed successfully |
| 400 | Invalid request or missing input |
| 500 | Internal server error |

---

# 🔒 Content Type

All requests and responses use JSON.

Request Header

```http
Content-Type: application/json
```

Response Header

```http
Content-Type: application/json
```

---

# 🧪 Example cURL Request

```bash
curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d "{\"url\":\"https://google.com\"}"
```

---

# 📖 Notes

- The backend accepts one URL per request.
- Trusted domains may bypass machine learning prediction through the hybrid decision engine.
- All prediction requests are logged for audit and analysis.
- The API is designed to integrate with the React frontend but can also be consumed by any HTTP client capable of sending JSON requests.
