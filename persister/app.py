import time
import os
from kafka import KafkaConsumer

while True:
    consumer = KafkaConsumer(
        os.environ.get("PARSED_DATA_TOPIC_NAME"), bootstrap_servers="kafka:9092"
    )
    for msg in consumer:
        print(f"{msg.topic}: {msg.value.decode()}")

