''' Companies Models '''

# Natives
import uuid

# Django
from django.db import models


class Company (models.Model):
    ''' Company model that fit the application requirements  '''

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=100, blank=False, null=False)
    ticker = models.CharField(max_length=10, blank=False, null=False)
    values = models.CharField(max_length=255, blank=False, null=False)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ''' Order the results by the date of creation, last appears first '''
        ordering = ['-created_at']

    def __str__(self):
        ''' Return the ticker to identify the company '''
        return self.ticker
