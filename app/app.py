import os, pickle, base64
from flask import Flask, request, jsonify
import redis

app = Flask(__name__)

r = redis.Redis(host='localhost', port=6379, password='admin_password_123')

@app.route('/process', methods=['POST'])
def process():
    try:
        data = base64.b64decode(request.json['payload'])
        obj = pickle.loads(data) 
        
        return jsonify({"status": "processed", "result": str(obj)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)