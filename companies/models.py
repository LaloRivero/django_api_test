''' Companies Models '''

# Natives
import uuid

# Django
from django.db import models
from django.contrib.postgres.fields import ArrayField


class Company (models.Model):
    ''' Company model that fit the application requirements  '''

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    ticker = models.CharField(max_length=10, blank=True, null=True)
    values = ArrayField(models.IntegerField(), size=50)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ''' Order the results by the date of creation, last appears first '''
        ordering = ['-created_at']

    def __str__(self):
        ''' Return the ticker to identify the company '''
        return self.ticker
