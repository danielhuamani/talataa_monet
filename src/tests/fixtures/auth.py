import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.fixture(autouse=True)
def api_client(student_user):
    client = APIClient()
    refresh = RefreshToken.for_user(student_user)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
    return client


@pytest.fixture
def quiz_start_url():
    return reverse("quizzes:quiz_start")
