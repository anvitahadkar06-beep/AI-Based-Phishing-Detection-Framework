# AI-Based Phishing Detection System

## Deployment Report

---

## Project Overview

The AI-Based Phishing Detection System is a full-stack web application developed to detect phishing websites using Machine Learning, rule-based analysis, and trusted domain validation. The system analyzes a given URL and predicts whether it is **LEGITIMATE** or **PHISHING**, while also providing a confidence score, risk level, and detection reasons.

The project consists of:
- React.js Frontend
- Flask Backend
- Random Forest Machine Learning Model
- Rule-Based Detection Engine
- Trusted Domain Validation
- REST API Communication

---

## Deployment Architecture

```text
                 User
                   │
                   ▼
        React Frontend (Vercel)
                   │
            REST API Request
                   │
                   ▼
        Flask Backend (Render)
                   │
      ┌────────────┼────────────┐
      │            │            │
      ▼            ▼            ▼
 Feature      Rule Engine   Trusted Domain
Extraction                  Validation
      │            │            │
      └────────────┼────────────┘
                   ▼
        Random Forest Model
                   │
                   ▼
      Prediction & Risk Analysis
                   │
                   ▼
          Response to Frontend
```

---

## Backend Deployment

**Platform:** Render

### Deployment Steps

- Connected the GitHub repository to Render.
- Selected the **Backend** folder as the Root Directory.
- Configured Python as the runtime environment.
- Added a **Procfile** to run the Flask application using Gunicorn.
- Updated the `requirements.txt` file with only the required dependencies.
- Configured the Build Command:
  ```
  pip install -r requirements.txt
  ```
- Configured the Start Command:
  ```
  gunicorn src.app:app
  ```
- Successfully deployed the Flask REST API.

---

## Frontend Deployment

**Platform:** Vercel

### Deployment Steps

- Connected the GitHub repository to Vercel.
- Selected the **Frontend** folder as the Root Directory.
- Installed all required React dependencies.
- Generated the production build automatically.
- Updated the frontend API endpoint to communicate with the deployed Render backend.
- Successfully deployed the React application.

---

## Deployment Challenges

The following issues were encountered during deployment:

- Initial deployment failed because the original `requirements.txt` contained unnecessary packages that required system-level compilers.
- The dependency list was optimized by retaining only the packages required for the phishing detection application.
- Gunicorn was configured as the production WSGI server.
- Backend API endpoints were tested after deployment.
- Frontend API configuration was updated to connect with the deployed backend.
- Trusted domain validation was improved to correctly recognize trusted domains and their subdomains.

All deployment issues were successfully resolved.

---

## Deployment Testing

The deployed application was tested using multiple URLs.

| URL | Expected Result | Actual Result | Status |
|-----|-----------------|---------------|--------|
| https://google.com | Legitimate | Legitimate | ✅ Pass |
| https://github.com | Legitimate | Legitimate | ✅ Pass |
| https://mail.google.com | Legitimate | Legitimate | ✅ Pass |
| https://google-login-security.com | Phishing | Phishing | ✅ Pass |
| http://secure-login-bank-update.com | Phishing | Phishing | ✅ Pass |

---

## Deployment Outcome

The deployment was successfully completed.

### Backend

- Successfully hosted on Render.
- Flask REST API is accessible online.
- Machine Learning model loads successfully.
- Prediction API works correctly.

### Frontend

- Successfully hosted on Vercel.
- React application is accessible online.
- Communicates successfully with the deployed backend.
- Displays prediction results, confidence score, and risk level in real time.

---

## Features Verified After Deployment

- URL scanning
- Machine Learning prediction
- Rule-based phishing analysis
- Trusted domain validation
- Confidence score generation
- Risk level calculation
- API communication
- Responsive user interface

---

## Conclusion

The AI-Based Phishing Detection System was successfully deployed using **Render** for the backend and **Vercel** for the frontend. The deployed application performs real-time phishing detection by combining a Random Forest Machine Learning model with rule-based analysis and trusted domain validation. Production testing confirmed that the system correctly classifies legitimate and phishing URLs while providing accurate confidence scores and risk assessments. The successful deployment demonstrates the application's stability, reliability, and readiness for practical cybersecurity applications.
