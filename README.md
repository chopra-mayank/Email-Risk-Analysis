# Email Risk Analysis System

This project is an **Email Risk Analysis System** that analyzes emails for risk, spam, and grammar scores. It consists of:
- A **Node.js backend** to receive emails and update MongoDB.
- A **Flask backend** to analyze emails and generate risk scores.
- A **MongoDB database** to store email records.

---

## Table of Contents
1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [How to Run](#how-to-run)
4. [API Endpoints](#api-endpoints)
5. [Example Request and Response](#example-request-and-response)
6. [Folder Structure](#folder-structure)
7. [Contributors](#contributors)

---

## Features
- **Email Analysis**: Analyze emails for risk, spam, and grammar scores.
- **Logging**: Logs API requests and responses for debugging.
- **NLP Processing**: Basic NLP processing using NLTK for spam detection.

---

## Technologies Used
- **Backend**: Node.js (Express), Flask (Python)
- **Database**: MongoDB
- **Libraries**: Axios, Mongoose, NLTK, Pydantic
- **Tools**: Postman (for testing), Git (for version control)

---

## How to Run

### Prerequisites
1. Install [Node.js](https://nodejs.org/).
2. Install [Python](https://www.python.org/).
3. Install [MongoDB](https://www.mongodb.com/).

### Steps
1. **Start MongoDB**:
   ```bash
   mongod
   ```
2. **Run the Node.js Backend**:
   ```bash
   cd node_backend
   npm install
   node index.js
   ```
3. **Run the Flask Backend**:
   ```bash
   cd flask_backend
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   python app.py
   ```

4. **Test the System Using Postman**:
   
   Send a POST request to `http://localhost:3000/analyze-email` with the following JSON body:
   ```json
   {
     "email_id": "12345",
     "senderEmail": "test@example.com",
     "body": "This is a test email."
   }
   ```

---

## API Endpoints

### Node.js Backend
- **POST /analyze-email**: Submit an email for analysis.

  **Request Body:**
  ```json
  {
    "email_id": "12345",
    "senderEmail": "test@example.com",
    "body": "This is a test email."
  }
  ```
  **Response:**
  ```json
  {
    "message": "Email analyzed and updated successfully"
  }
  ```

### Flask Backend
- **POST /process-email**: Analyze an email and return risk scores.

  **Request Body:**
  ```json
  {
    "email_id": "12345",
    "senderEmail": "test@example.com",
    "body": "This is a test email."
  }
  ```
  **Response:**
  ```json
  {
    "risk_score": 0.75,
    "spam_score": 0.8,
    "grammar_score": 0.9
  }
  ```

---

## Example Request and Response

**Request (via Postman)**
- **URL:** `http://localhost:3000/analyze-email`
- **Method:** POST
- **Body (JSON):**
  ```json
  {
    "email_id": "12345",
    "senderEmail": "test@example.com",
    "body": "Congratulations! You have won a free prize."
  }
  ```

**Response**
- **From Node.js Backend:**
  ```json
  {
    "message": "Email analyzed and updated successfully"
  }
  ```
- **From Flask Backend:**
  ```json
  {
    "risk_score": 0.75,
    "spam_score": 0.8,
    "grammar_score": 0.9
  }
  ```

---

## Folder Structure
```
email-risk-analysis/
├── node_backend/              # Node.js backend
│   ├── models/                # MongoDB models
│   │   └── email.js
│   ├── routes.js              # API routes
│   ├── index.js               # Main server file
│   └── package.json           # Node.js dependencies
├── flask_backend/             # Flask backend
│   ├── app.py                 # Flask application
│   ├── schemas.py             # Pydantic validation
│   └── requirements.txt       # Python dependencies
└── README.md                  # Project documentation
```
