from apps.quizzes.models import QuestionOption
from .models import StudentQuiz, StudentQuizAnswer


def create_student_quiz_case(student, quiz, answers):
    student_quiz = StudentQuiz.objects.create(
        student=student, quiz=quiz, score=0
    )
    total_score = 0
    for answer in answers["answers"]:
        question_option = QuestionOption.objects.get(
            id=answer["question_option"]
        )
        if question_option.is_answer:
            total_score += question_option.question.score
        StudentQuizAnswer.objects.create(
            student_quiz=student_quiz,
            question_id=answer["question"],
            question_option_id=answer["question_option"],
        )
    student_quiz.score = total_score
    student_quiz.save()
    return student_quiz
