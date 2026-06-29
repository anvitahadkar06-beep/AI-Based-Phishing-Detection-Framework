# API Specification: AI-Based Phishing Detection Framework

This document defines the RESTful API endpoints for the system. All requests and responses must be in **JSON** format.

## API Endpoint Table

| Endpoint | Method | Purpose |
| :--- | :--- | :--- |
| `/api/chat` | `POST` | Send prompts to AI |
| `/api/history` | `GET` | Retrieve conversations |
| `/api/users` | `GET` | Fetch user information |
| `/api/feedback` | `POST` | Store ratings |
| `/api/health` | `GET` | Health check |

## API Specification Details

### 1. `/api/chat` (POST)
Used to send user prompts or URL/email inputs to the AI engine for analysis.
* **Request Body**: `{"prompt": "string"}`
* **Response**: `{"response": "string", "timestamp": "ISO8601"}`

### 2. `/api/history` (GET)
Retrieves the history of past AI interactions for the authenticated user.
* **Response**: `{"conversations": [...]}`

### 3. `/api/users` (GET)
Fetches user profile information and system preferences.
* **Response**: `{"user_id": "string", "name": "string", "email": "string"}`

### 4. `/api/feedback` (POST)
Stores user ratings or feedback regarding the AI's detection accuracy.
* **Request Body**: `{"rating": "integer", "comment": "string"}`
* **Response**: `{"status": "success"}`

### 5. `/api/health` (GET)
Simple endpoint to verify that the API server is active and reachable.
* **Response**: `{"status": "online"}`
