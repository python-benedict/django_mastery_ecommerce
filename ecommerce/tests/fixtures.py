import pytest

@pytest.fixture
def create_admin_user(django_user_model):
    """
    Return admin User
    """
    return django_user_model.objects.create_superuser('admin', 'admin@gmail.com', 'admin')