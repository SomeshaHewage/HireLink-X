from flask import Flask, jsonify
from serverless_wsgi import handle_request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Hello, World!")

def lambda_handler(event, context):
    return handle_request(app, event, context)
