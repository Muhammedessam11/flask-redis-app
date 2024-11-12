import os
from flask import Flask
import redis

app = Flask(__name__)
redis_host = os.getenv("REDIS_HOST", "redis")  # Using 'redis' as the hostname for Docker Compose networking
redis_port = 6379

# Connect to Redis
client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/')
def index():
    # Increment the counter
    client.incr('counter')
    counter = client.get('counter')
    return f"Hello! This page has been visited {counter} times."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

