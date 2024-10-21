import pytest

from pyler_users.models import PylerUser


@pytest.mark.django_db
def test_my_user():
    user = PylerUser.objects.create_superuser(username='admin', password="test1234")
    assert user.is_superuser