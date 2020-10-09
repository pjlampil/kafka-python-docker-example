import time
import os
from kafka import KafkaConsumer, KafkaProducer

while True:
    consumer = KafkaConsumer(
        os.environ.get("RAW_DATA_TOPIC_NAME"), bootstrap_servers="kafka:9092"
    )
    producer = KafkaProducer(bootstrap_servers="kafka:9092")
    PARSED_DATA_TOPIC_NAME = os.environ.get("PARSED_DATA_TOPIC_NAME")
    for msg in consumer:
        producer.send(PARSED_DATA_TOPIC_NAME, msg.value)
        print(f"{msg.topic}: {msg.value.decode()}")

