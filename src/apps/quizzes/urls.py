from django.urls import path
from .apis import QuizRetrieveAPI, QuizStarAPI

urlpatterns = [
    path("quiz/<int:pk>/", QuizRetrieveAPI.as_view(), name="quiz_detail"),
    path("quiz/<int:pk>/start/", QuizStarAPI.as_view(), name="quiz_start"),
]
