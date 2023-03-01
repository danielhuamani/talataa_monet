from django.db import models
from apps.core.models import TimestampModel

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(
        "users.User", related_name="user_student", on_delete=models.CASCADE
    )
    level = models.CharField(max_length=100, blank=True)

    class Meta:
        """Meta definition for Student."""

        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        """Unicode representation of Student."""
        return self.user.first_name


class StudentQuiz(TimestampModel):
    student = models.ForeignKey(Student, related_name="student_quizzes")
    quiz = models.ForeignKey(
        "quizzes.Quiz", related_name="quiz_student_quizzes"
    )
    score = models.PositiveIntegerField()

    def __str__(self):
        pass

    class Meta:
        verbose_name = "StudentTest"
        verbose_name_plural = "StudentTests"
