import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from login_selenium import login_turnitin

load_dotenv()

API_KEY = os.getenv("SECRET_API_KEY")

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    
    provided_key = request.headers.get('X-API-KEY')
    if provided_key != API_KEY:
        return jsonify({"error": "Invalid API key"}), 401
    
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Username and password required"}), 400

    success = login_turnitin(email, password)

    return jsonify({"message": "Login Successful" if success else "Login Failed"})


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
