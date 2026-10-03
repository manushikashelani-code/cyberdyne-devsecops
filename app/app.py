import os
import json
import base64
from flask import Flask, request, jsonify
import redis

app = Flask(__name__)

# Fetch Redis host and password securely from environment variables
REDIS_HOST = os.getenv('REDIS_HOST', 'broker')
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)

@app.route('/process', methods=['POST'])
def process():
    try:
        data = base64.b64decode(request.json['payload'])
        # VULNERABILITY FIX: Replaced insecure pickle.loads() with safe json.loads()
        obj = json.loads(data.decode('utf-8'))
        
        return jsonify({"status": "processed", "result": obj})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)