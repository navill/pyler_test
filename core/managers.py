from django.db import models
from django.db.models import QuerySet

from core.queryset import BaseQuerySet


class BaseManager(models.Manager):
    def get_queryset(self: models.Manager) -> QuerySet:
        return BaseQuerySet(self.model, using=self._db).filter(deleted_at__isnull=True)
