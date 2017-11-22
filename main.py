import logging
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.before_request
def before_request():
    logging.info(request.headers)
    logging.info(request.values)
    if 'application/json' in request.headers['Content-Type']:
        logging.info(request.json)

@app.route('/')
def index():
    return 'hello'

@app.route('/webhook', methods=['POST'])
def webhook():
    return jsonify(status='ok', requested=request.json)
