from datetime import datetime

from django.db.models import QuerySet


class BaseQuerySet(QuerySet):
    def delete(self) -> tuple[int, dict]:
        now = datetime.now()
        for obj in self:
            obj.deleted_at = now
        deleted_count = self.bulk_update(self, ["deleted_at"])
        return len(self), {self.model._meta.label: deleted_count}

    def hard_delete(self) -> tuple[int, dict]:
        return super().delete()
