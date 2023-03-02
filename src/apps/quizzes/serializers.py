from rest_framework import serializers
from .models import Quiz, Question, QuestionOption


class QuestionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionOption
        fields = ["id", "name"]


class QuestionSerializer(serializers.ModelSerializer):
    question_options = QuestionOptionSerializer(many=True)

    class Meta:
        model = Question
        fields = ["id", "name", "content", "question_options"]


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = ["id", "name", "questions"]


class QuizAnswerSerializer(serializers.Serializer):
    question = serializers.IntegerField()
    question_option = serializers.IntegerField()

    def validate_question(self, value):
        if not Question.objects.filter(
            id=value, is_active=True, quiz=self.context.get("quiz")
        ).exists():
            raise serializers.ValidationError("Question not found")
        return value

    def validate(self, data):
        question = data["question"]
        question_option = data["question_option"]
        if not QuestionOption.objects.filter(
            id=question_option,
            question__id=question,
            question__is_active=True,
            question__quiz=self.context.get("quiz"),
        ).exists():
            raise serializers.ValidationError(
                {"question_option": "Question Option not found"}
            )
        return data


class QuizAnswersSerializer(serializers.Serializer):
    answers = QuizAnswerSerializer(many=True, required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["answers"].context.update(self.context)

    def validate_answers(self, value):
        question_count = Question.objects.filter(
            is_active=True, quiz=self.context.get("quiz")
        ).count()
        if question_count != len(value):
            raise serializers.ValidationError("incomplete questions")
        return value
