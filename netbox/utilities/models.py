from __future__ import unicode_literals

from django.contrib.postgres.fields import ArrayField
from django.db import models


class CreatedUpdatedModel(models.Model):
    created = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TaggedModel(models.Model):
    tags = ArrayField(
        base_field=models.CharField(max_length=50),
        blank=True,
        null=True
    )

    class Meta:
        abstract=True
