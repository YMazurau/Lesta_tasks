from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)

redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_client = redis.Redis(host=redis_host, port=6379, db=0, decode_responses=True)

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"status": "ok"})

@app.route("/count", methods=["GET"])
def count():
    try:
        value = redis_client.incr("counter")
        return jsonify({"count": value})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
