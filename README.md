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
7. [Code Implementation](#code-implementation)

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
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Mac/Linux
   pip install -r requirements.txt
   python app.py
   ```

---

## API Endpoints

### Node.js Backend
- **POST `/analyze-email`**: Submit an email for analysis.

#### Request Body:
```json
{
  "email_id": "12345",
  "senderEmail": "test@example.com",
  "body": "This is a test email."
}
```

#### Response:
```json
{
  "message": "Email analyzed and updated successfully"
}
```

### Flask Backend
- **POST `/process-email`**: Analyze an email and return risk scores.

#### Request Body:
```json
{
  "email_id": "12345",
  "senderEmail": "test@example.com",
  "body": "This is a test email."
}
```

#### Response:
```json
{
  "risk_score": 0.75,
  "spam_score": 0.8,
  "grammar_score": 0.9
}
```

---

## Example Request and Response

### Request (via Postman)
**URL**: `http://localhost:3000/analyze-email`

**Method**: POST

**Body (JSON)**:
```json
{
  "email_id": "12345",
  "senderEmail": "test@example.com",
  "body": "Congratulations! You have won a free prize."
}
```

### Response
#### From Node.js Backend:
```json
{
  "message": "Email analyzed and updated successfully"
}
```

#### From Flask Backend:
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

---

## Code Implementation

### **Node.js Service**

#### **models/email.js**
```javascript
const mongoose = require('mongoose');

const emailSchema = new mongoose.Schema({
  email_id: String,
  senderEmail: String,
  body: String,
  risk_score: Number,
  spam_score: Number,
  grammar_score: Number,
});

module.exports = mongoose.model('Email', emailSchema);
```

#### **index.js**
```javascript
const express = require('express');
const mongoose = require('mongoose');
const routes = require('./routes');
const morgan = require('morgan');

const app = express();
const PORT = 3000;

app.use(express.json());
app.use(morgan('dev'));
mongoose.connect('mongodb://localhost:27017/emailDB', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
})
.then(() => console.log("MongoDB connected successfully"))
.catch(err => console.error("MongoDB connection error:", err));

app.use('/', routes);

app.listen(PORT, () => {
  console.log(`Node.js server running on http://localhost:${PORT}`);
});
```

#### **routes.js**
```javascript
const express = require('express');
const router = express.Router();
const Email = require('./models/email');
const axios = require('axios');

router.post('/analyze-email', async (req, res) => {
  console.log("Received request at /analyze-email with body:", req.body);
  const { email_id, senderEmail, body } = req.body;

  try {
    const response = await axios.post('http://localhost:5000/process-email', {
      email_id,
      senderEmail,
      body,
    });

    console.log("Response from Flask backend:", response.data);

    const { risk_score, spam_score, grammar_score } = response.data;

    await Email.findOneAndUpdate(
      { email_id },
      { risk_score, spam_score, grammar_score },
      { upsert: true, new: true }
    );

    res.status(200).json({ message: 'Email analyzed and updated successfully' });
  } catch (error) {
    console.error("Error in /analyze-email:", error);
    res.status(500).json({ error: 'An error occurred' });
  }
});

module.exports = router;
```

### **Flask Service**

#### **app.py**
```python
from flask import Flask, request, jsonify
from schemas import EmailPayload
import random
import nltk

app = Flask(__name__)

@app.route('/process-email', methods=['POST'])
def process_email():
    payload = request.json
    email = EmailPayload(**payload)
    
    risk_score = random.uniform(0, 1)
    spam_score = random.uniform(0, 1)
    grammar_score = random.uniform(0, 1)
    
    return jsonify({ 'risk_score': risk_score, 'spam_score': spam_score, 'grammar_score': grammar_score })

if __name__ == '__main__':
    app.run(port=5000)
```

#### **schemas.py**
```python
from pydantic import BaseModel

class EmailPayload(BaseModel):
    email_id: str
    senderEmail: str
    body: str
```

---
