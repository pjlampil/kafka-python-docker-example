# views.py
from rest_framework import viewsets

from .serializers import ObservationSerializer
from .models import Observation


class ObservationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Observation.objects.all().order_by("time_stamp")
    serializer_class = ObservationSerializer
