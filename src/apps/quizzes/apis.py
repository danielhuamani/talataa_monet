from django.db.models import Prefetch
from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from apps.core.mixins import LoginRequiredMixin, LoginStudentRequiredMixin
from apps.students.use_cases import create_student_quiz_case
from rest_framework import status
from .serializers import QuizSerializer, QuizAnswersSerializer
from .models import Quiz, Question


class QuizRetrieveAPI(LoginRequiredMixin, RetrieveAPIView):
    model = Quiz
    serializer_class = QuizSerializer

    def get_queryset(self):
        queryset = Quiz.objects.all().prefetch_related(
            Prefetch(
                "questions",
                queryset=Question.objects.prefetch_related("question_options")
                .filter(is_active=True)
                .order_by("position"),
            ),
        )
        return queryset


class QuizStarAPI(LoginStudentRequiredMixin, APIView):
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        student = request.user.student
        quiz = get_object_or_404(Quiz, pk=kwargs.get("pk"))
        serializer = QuizAnswersSerializer(
            data=request.data, context={"quiz": quiz, "request": request}
        )
        serializer.is_valid(raise_exception=True)
        serializer_data = serializer.data
        student_quiz = create_student_quiz_case(student, quiz, serializer_data)
        return Response(
            {
                "id": student_quiz.id,
                "student_score": student_quiz.score,
                "total": quiz.get_total_score_by_all_questions(),
            },
            status.HTTP_201_CREATED,
        )
