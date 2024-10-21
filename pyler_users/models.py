from __future__ import annotations

import uuid

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models, transaction
from django.db.models import QuerySet
from rest_framework_simplejwt.tokens import RefreshToken

from core.models import BaseModel
from core.queryset import BaseQuerySet


class PylerUserManager(UserManager):
    def get_queryset(self) -> QuerySet:
        return BaseQuerySet(self.model, using=self._db).filter(is_active=True, deleted_at__isnull=True)

    def create_user(self, username: str, email: str = None, password: str = None, **extra_fields) -> PylerUser:
        with transaction.atomic():
            user = super().create_user(username, email, password, **extra_fields)
            token = RefreshToken.for_user(user)
            setattr(user, "token", {
                "refresh": str(token),
                "access": str(token.access_token)
            })
        return user


class PylerUser(BaseModel, AbstractUser):
    identifier = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    groups = None
    user_permissions = None

    objects = PylerUserManager()
