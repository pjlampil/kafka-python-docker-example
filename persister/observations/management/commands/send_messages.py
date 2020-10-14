import time
import datetime
import json
import random
import sys
from django.core.management.base import BaseCommand
import requests


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument("sleep", type=int)

    def handle(self, *args, **kwargs):
        value = 15.0
        while True:
            value = round(value + random.sample([-0.2, -0.1, 0.0, 0.1, 0.2], 1)[0], 1)
            time_stamp = str(datetime.datetime.utcnow())
            try:
                data = {
                    "data": {
                        "observed_data_type": "swim_water_temperature",
                        "time_stamp": time_stamp,
                        "value": value,
                    }
                }
                requests.post("http://endpoint:5000", json=json.dumps(data))
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Sent a message with a value {value} @ {time_stamp}"
                    )
                )
                time.sleep(kwargs["sleep"])
            except KeyboardInterrupt:
                self.stdout.write(self.style.SUCCESS("Bye"))
                sys.exit()
