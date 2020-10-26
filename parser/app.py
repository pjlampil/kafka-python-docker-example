import time
import os
from kafka import KafkaConsumer, KafkaProducer

raw_data_topic = os.environ.get("RAW_DATA_TOPIC_NAME")
consumer = KafkaConsumer(raw_data_topic, bootstrap_servers="kafka:9092")
print(f"Listening to topic {raw_data_topic}")
producer = KafkaProducer(bootstrap_servers="kafka:9092")
PARSED_DATA_TOPIC_NAME = os.environ.get("PARSED_DATA_TOPIC_NAME")
for msg in consumer:
    producer.send(PARSED_DATA_TOPIC_NAME, msg.value)
    print(f"{msg.topic}: {msg.value.decode()}")

