import time
import os
import json

from django.core.management.base import BaseCommand
from observations.serializers import ObservationSerializer
from kafka import KafkaConsumer


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def handle(self, *args, **options):

        consumer = KafkaConsumer(
            os.environ.get("PARSED_DATA_TOPIC_NAME"), bootstrap_servers="kafka:9092"
        )
        for msg in consumer:
            print(f"{msg.topic}: {msg.value.decode()}")
            serializer = ObservationSerializer(
                data=json.loads(msg.value.decode())["data"]
            )
            serializer.is_valid()
            serializer.save()
