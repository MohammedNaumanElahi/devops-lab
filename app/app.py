from flask import Flask, jsonify
import redis, os

app = Flask(__name__)

r = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=6379,
    decode_responses=True
)

@app.route("/")
def index():
    count = r.incr("visits")
    return jsonify({
        "message": "Hello from DevOps Lab!",
        "visits": count
    })

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
