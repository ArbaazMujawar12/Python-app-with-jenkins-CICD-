from flask import Flask, jsonify
import os

app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return jsonify({
        "message": "Python Flask Application Successfully Deployed 🚀",
        "deployment": "Jenkins CI/CD with Docker",
        "status": "Running",
        "version": "v1.0"
    })

# Secondary Route
@app.route('/hi')
def greeting():
    return "<h1>Hello from Flask & Docker 👋</h1>"

# Health Check Route (Important for DevOps)
@app.route('/health')
def health():
    return jsonify({"status": "OK"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)