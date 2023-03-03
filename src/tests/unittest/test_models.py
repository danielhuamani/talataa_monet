class TestQuizModel:
    def test_quiz_score_zero_without_questions(self, quiz_main_1):
        print(quiz_main_1.get_total_score_by_all_questions(), "sdsds")
        assert quiz_main_1.get_total_score_by_all_questions() == 0

    def test_quiz_with_score_value(self, quiz_main_1, question_1, question_2):
        assert quiz_main_1.get_total_score_by_all_questions() == 2


class TestStudentModel:
    def test_student_signals_post_save_with_permission(self, student_user):
        student_permissions = student_user.user_permissions.all()
        assert student_permissions.count() == 2
        assert student_permissions.filter(codename="view_studentquiz").exists()
        assert student_permissions.filter(
            codename="view_studentquizanswer"
        ).exists()
