from typing import Union

from django.db import models
from django.utils.timezone import now


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]

    def delete(self, using=None, keep_parents=False) -> None:
        self.deleted_at = now()
        self.save()

    def hard_delete(self, using=None, keep_parents=False) -> Union[int, dict]:
        return super().delete(using, keep_parents)

    def restore(self) -> None:
        self.deleted_at = None
        self.save()
