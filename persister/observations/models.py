from django.db import models


class Observation(models.Model):
    observed_data_type = models.CharField(max_length=255, db_index=True)
    time_stamp = models.DateTimeField(db_index=True)
    value = models.FloatField()
