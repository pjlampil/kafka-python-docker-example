import time
import os
import json

from django.core.management.base import BaseCommand
from observations.serializers import ObservationSerializer
from kafka import KafkaConsumer


class Command(BaseCommand):

    def handle(self, *args, **options):
        parsed_data_topic = os.environ.get("PARSED_DATA_TOPIC_NAME")
        consumer = KafkaConsumer(parsed_data_topic, bootstrap_servers="kafka:9092")
        print(f"Listening to topic {parsed_data_topic}")
        for msg in consumer:
            print(f"{msg.topic}: {msg.value.decode()}")
            serializer = ObservationSerializer(
                data=json.loads(msg.value.decode())["data"]
            )
            serializer.is_valid()
            serializer.save()
