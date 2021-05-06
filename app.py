from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

@app.route('/')
def root():
    return jsonify({"message": 'Welcome to my Flask API for snooker players!'}), 200

if __name__ == "__main__":
    app.run(debug=True)