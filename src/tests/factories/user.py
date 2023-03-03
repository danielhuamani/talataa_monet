import factory
from apps.users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
