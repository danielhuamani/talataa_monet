import pytest
from tests.factories.user import UserFactory
from tests.factories.student import StudentFactory


@pytest.fixture
def user_main():
    user = UserFactory(
        email="user@example.com", first_name="John", last_name="Smith"
    )
    user.set_password("password1")
    return user


@pytest.fixture
def student_user(db):
    user = UserFactory(
        email="student@example.com", first_name="John", last_name="Smith"
    )
    user.set_password("password2")
    StudentFactory(user=user, level="1 grado")
    return user
