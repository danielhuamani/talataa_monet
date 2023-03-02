from django.db import models
from django.db.models import Sum
from apps.core.models import TimestampModel, ActiveModel


class Quiz(TimestampModel):
    name = models.CharField(max_length=255)
    time_for_quiz = models.PositiveIntegerField(help_text="time in minutes")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizs"

    def total_score_by_all_questions(self):
        result = self.questions.all().aggregate(total_score=Sum("score"))
        if result:
            return result.get("total_score")
        return 0


class Question(TimestampModel, ActiveModel):
    quiz = models.ForeignKey(
        "Quiz", related_name="questions", on_delete=models.CASCADE
    )
    score = models.PositiveIntegerField(default=1)
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    position = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
        ordering = ["position"]


class QuestionOption(TimestampModel):
    question = models.ForeignKey(
        "Question", related_name="question_options", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    is_answer = models.BooleanField()
    position = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Question Option"
        verbose_name_plural = "Question Options"
        ordering = ["position"]
