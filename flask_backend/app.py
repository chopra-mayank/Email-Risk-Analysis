from flask import Flask, request, jsonify
from schemas import EmailPayload
import random
import logging
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SPAM_KEYWORDS = ["free", "win", "prize", "offer", "discount", "cash", "urgent", "congratulations", "click", "limited"] # A set of Spam Keywords

def analyze_email_body(body):
    tokens = word_tokenize(body)
    logger.info("Tokenized email body: %s", tokens)

    pos_tags = pos_tag(tokens)
    logger.info("POS tags: %s", pos_tags)

    noun_count = sum(1 for word, tag in pos_tags if tag.startswith('NN'))
    verb_count = sum(1 for word, tag in pos_tags if tag.startswith('VB'))
    logger.info("Noun count: %d, Verb count: %d", noun_count, verb_count)

    return {
        'noun_count': noun_count,
        'verb_count': verb_count,
    }

def detect_spam(body):
    body_lower = body.lower()

    spam_count = sum(1 for keyword in SPAM_KEYWORDS if keyword in body_lower)
    logger.info("Spam keyword count: %d", spam_count)

    return spam_count / len(SPAM_KEYWORDS)

@app.route('/process-email', methods=['POST'])
def process_email():
    logger.info("Received request at /process-email with payload: %s", request.json)
    payload = request.json
    email = EmailPayload(**payload)

    analysis_result = analyze_email_body(email.body)

    spam_score = detect_spam(email.body)

    risk_score = random.uniform(0, 1)
    grammar_score = random.uniform(0, 1)

    if analysis_result['noun_count'] > 5:
        risk_score *= 1.2  # Increase risk score if many nouns
    if analysis_result['verb_count'] > 5:
        grammar_score *= 1.1  # Improve grammar score if many verbs

    response = {
        'risk_score': risk_score,
        'spam_score': spam_score,
        'grammar_score': grammar_score,
    }

    logger.info("Sending response: %s", response)
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000)
