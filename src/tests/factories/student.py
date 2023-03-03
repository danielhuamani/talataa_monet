import factory
from apps.students.models import Student


class StudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Student
