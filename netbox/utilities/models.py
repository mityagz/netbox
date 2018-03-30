from __future__ import unicode_literals

import itertools

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

    @classmethod
    def get_all_tags(cls):
        """
        Return a list of all unique tags for this model.
        """
        queryset = cls.objects.exclude(tags=None).values_list('tags', flat=True)
        return sorted(set(itertools.chain(*queryset)))
