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