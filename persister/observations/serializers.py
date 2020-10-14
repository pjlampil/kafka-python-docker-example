# serializers.py
from rest_framework import serializers

from .models import Observation


class ObservationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Observation
        fields = ("observed_data_type", "time_stamp", "value")

