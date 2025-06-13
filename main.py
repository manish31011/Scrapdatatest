from flask import Flask, request, jsonify
from login_selenium import login_turnitin

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Username and password required"}), 400

    success = login_turnitin(email, password)

    return jsonify({"message": "Login Successful" if success else "Login Failed"})


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
