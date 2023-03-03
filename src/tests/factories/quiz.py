import factory
from apps.quizzes.models import Quiz, Question, QuestionOption


class QuizFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Quiz


class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Question


class QuestionOptionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = QuestionOption
