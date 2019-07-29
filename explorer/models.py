from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField
from django.contrib.auth.models import User


class Dataset(models.Model):
    name = models.CharField(max_length=25)
    columns = JSONField()
    data = JSONField()

    def __str__(self):
        return self.name
