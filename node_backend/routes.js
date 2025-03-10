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