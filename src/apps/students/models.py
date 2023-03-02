from django.db import models
from apps.core.models import TimestampModel

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(
        "users.User", related_name="student", on_delete=models.CASCADE
    )
    level = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return self.user.first_name


class StudentQuiz(TimestampModel):
    student = models.ForeignKey(
        "Student", related_name="student_quizzes", on_delete=models.CASCADE
    )
    quiz = models.ForeignKey(
        "quizzes.Quiz",
        related_name="student_quizzes",
        on_delete=models.CASCADE,
    )
    score = models.PositiveIntegerField()

    def __str__(self):
        pass

    class Meta:
        verbose_name = "StudentQuiz"
        verbose_name_plural = "StudentQuizs"


class StudentQuizAnswer(TimestampModel):
    student_quiz = models.ForeignKey(
        "StudentQuiz",
        related_name="student_quiz_answers",
        on_delete=models.CASCADE,
    )
    question = models.ForeignKey(
        "quizzes.Question",
        related_name="student_quiz_answers",
        on_delete=models.CASCADE,
    )
    question_option = models.ForeignKey(
        "quizzes.QuestionOption",
        related_name="student_quiz_answers",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        pass

    class Meta:
        verbose_name = "StudentQuiz"
        verbose_name_plural = "StudentQuizs"
