from django.urls import reverse
from rest_framework import status


class TestQuizStartAPI:

    def test_quiz_incomplete_question_error(
        self,
        api_client,
        quiz_main_1,
        question_1,
        question_option_1_1,
        question_2,
        question_option_2_1,
        question_3,
    ):
        data = {
            "answers": [
                {
                    "question": question_1.id,
                    "question_option": question_option_1_1.id,
                },
                {
                    "question": question_2.id,
                    "question_option": question_option_2_1.id,
                },
            ]
        }
        url = reverse("quizzes:quiz_start", kwargs={"pk": quiz_main_1.id})
        response = api_client.post(url, data=data, format="json")
        response_json = response.json()
        assert response_json["answers"] == ["incomplete questions"]
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_quiz_duplicated_error(
        self,
        api_client,
        quiz_main_1,
        question_1,
        question_option_1_1,
        question_2,
        question_option_2_1,
        question_3,
        question_option_3_1,
    ):
        data = {
            "answers": [
                {
                    "question": question_1.id,
                    "question_option": question_option_1_1.id,
                },
                {
                    "question": question_2.id,
                    "question_option": question_option_2_1.id,
                },
                {
                    "question": question_2.id,
                    "question_option": question_option_2_1.id,
                },
            ]
        }
        url = reverse("quizzes:quiz_start", kwargs={"pk": quiz_main_1.id})
        response = api_client.post(url, data=data, format="json")
        response_json = response.json()
        assert response_json["answers"] == ["question duplicated"]
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_question_option_invalid_error(
        self,
        api_client,
        quiz_main_1,
        question_1,
        question_option_1_1,
        question_2,
        question_option_2_1,
        question_3,
        question_option_3_1,
    ):
        data = {
            "answers": [
                {
                    "question": question_1.id,
                    "question_option": question_option_1_1.id,
                },
                {
                    "question": question_2.id,
                    "question_option": question_option_2_1.id,
                },
                {
                    "question": question_3.id,
                    "question_option": question_option_2_1.id,
                },
            ]
        }
        url = reverse("quizzes:quiz_start", kwargs={"pk": quiz_main_1.id})
        response = api_client.post(url, data=data, format="json")
        response_json = response.json()
        assert response_json["answers"][2] == {
            "question_option": ["Question Option not found"]
        }
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_question_not_found_error(
        self,
        api_client,
        quiz_main_1,
        question_1,
        question_option_1_1,
        question_2,
        question_option_2_1,
        question_3,
        question_option_3_1,
    ):
        data = {
            "answers": [
                {
                    "question": question_1.id,
                    "question_option": question_option_1_1.id,
                },
                {
                    "question": question_2.id,
                    "question_option": question_option_2_1.id,
                },
                {
                    "question": 1000,
                    "question_option": question_option_2_1.id,
                },
            ]
        }
        url = reverse("quizzes:quiz_start", kwargs={"pk": quiz_main_1.id})
        response = api_client.post(url, data=data, format="json")
        response_json = response.json()
        assert response_json["answers"][2] == {
            "question": ["Question not found"]
        }
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_question_option_not_found_error(
        self,
        api_client,
        quiz_main_1,
        question_1,
        question_option_1_1,
        question_2,
        question_option_2_1,
        question_3,
        question_option_3_1,
    ):
        data = {
            "answers": [
                {
                    "question": question_1.id,
                    "question_option": question_option_1_1.id,
                },
                {
                    "question": question_2.id,
                    "question_option": question_option_2_1.id,
                },
                {
                    "question": question_3.id,
                    "question_option": 100,
                },
            ]
        }
        url = reverse("quizzes:quiz_start", kwargs={"pk": quiz_main_1.id})
        response = api_client.post(url, data=data, format="json")
        response_json = response.json()
        assert response_json["answers"][2] == {
            "question_option": ["Question Option not found"]
        }
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_quiz_completed_score_zero_success(
        self,
        api_client,
        quiz_main_1,
        question_1,
        question_option_1_1,
        question_2,
        question_option_2_1,
        question_3,
        question_option_3_1,
    ):
        data = {
            "answers": [
                {
                    "question": question_1.id,
                    "question_option": question_option_1_1.id,
                },
                {
                    "question": question_2.id,
                    "question_option": question_option_2_1.id,
                },
                {
                    "question": question_3.id,
                    "question_option": question_option_3_1.id,
                },
            ]
        }
        url = reverse("quizzes:quiz_start", kwargs={"pk": quiz_main_1.id})
        response = api_client.post(url, data=data, format="json")
        response_json = response.json()
        assert response_json["total"] == 3
        assert response_json["student_score"] == 0
        assert response.status_code == status.HTTP_201_CREATED

    def test_quiz_completed_score_one_success(
        self,
        api_client,
        quiz_main_1,
        question_1,
        question_option_1_1,
        question_2,
        question_option_2_1,
        question_3,
        question_option_3_3,
    ):
        data = {
            "answers": [
                {
                    "question": question_1.id,
                    "question_option": question_option_1_1.id,
                },
                {
                    "question": question_2.id,
                    "question_option": question_option_2_1.id,
                },
                {
                    "question": question_3.id,
                    "question_option": question_option_3_3.id,
                },
            ]
        }
        url = reverse("quizzes:quiz_start", kwargs={"pk": quiz_main_1.id})
        response = api_client.post(url, data=data, format="json")
        response_json = response.json()
        assert response_json["total"] == 3
        assert response_json["student_score"] == 1
        assert response.status_code == status.HTTP_201_CREATED
