from django.db import models
from apps.core.models import TimestampModel, ActiveModel


class Quiz(TimestampModel):
    name = models.CharField(max_length=255)
    time_for_quiz = models.PositiveIntegerField(help_text="time in minutes")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizs"


class Question(TimestampModel, ActiveModel):
    quiz = models.ForeignKey(
        "Quiz", related_name="questions", on_delete=models.CASCADE
    )
    score = models.PositiveIntegerField(default=1)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"


class QuestionOption(TimestampModel):
    question = models.ForeignKey("Question", related_name="question_options")
    name = models.CharField(max_length=255)
    is_answer = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
