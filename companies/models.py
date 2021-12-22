''' Companies Models '''

# Natives
import uuid

# Django
from django.db import models
from django.db.models.fields import IntegerField


class Company (models.Model):
    ''' Company model that fit the application requirements  '''

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    ticker = models.CharField(max_length=10, blank=True, null=True)


