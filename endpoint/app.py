import time
import os
import json
from kafka import KafkaProducer
from flask import Flask, request

app = Flask(__name__)
RAW_DATA_TOPIC_NAME = os.environ.get("RAW_DATA_TOPIC_NAME")


@app.route("/", methods=["POST"])
def hello_world():
    value = request.form.get("value").encode()
    producer.send(RAW_DATA_TOPIC_NAME, value)
    return "OK"


if __name__ == "__main__":
    producer = KafkaProducer(bootstrap_servers="kafka:9092")
    app.debug = True
    print("Starting server...")
    app.run(debug=True, host="0.0.0.0")
