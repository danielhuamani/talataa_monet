import pytest
from tests.factories.quiz import (
    QuizFactory,
    QuestionFactory,
    QuestionOptionFactory,
)


@pytest.fixture
def quiz_main_1():
    return QuizFactory(name="Test Python", time_for_quiz=20)


@pytest.fixture
def question_1(quiz_main_1):
    return QuestionFactory(
        quiz=quiz_main_1,
        name="1. ¿Cuál de las opciones nos permite obtener una lista con los siguientes valores : [9,16,25]?",
        score=1,
    )


@pytest.fixture
def question_2(quiz_main_1):
    return QuestionFactory(
        quiz=quiz_main_1,
        name="2. Completa la linea de código faltante para obtener los textos en mayúscula a partir de la siguiente lista:",
        score=1,
    )


@pytest.fixture
def question_3(quiz_main_1):
    return QuestionFactory(
        quiz=quiz_main_1,
        name="3. ¿Cuál de las opciones nos permite obtener una lista con los siguientes elementos: [2, 3, 3, 4]?",
        score=1,
    )


@pytest.fixture
def question_option_1_1(question_1):
    return QuestionOptionFactory(
        question=question_1,
        name="a. output = [n * 2 for n in lst_num]",
        is_answer=False,
    )


@pytest.fixture
def question_option_1_2(question_1):
    return QuestionOptionFactory(
        question=question_1,
        name="b. output = [n ** 2 for n in lst_num]",
        is_answer=False,
    )


@pytest.fixture
def question_option_1_3(question_1):
    return QuestionOptionFactory(
        question=question_1,
        name="c. output = [n ** 2 for lst_num in n]",
        is_answer=True,
    )


@pytest.fixture
def question_option_2_1(question_2):
    return QuestionOptionFactory(
        question=question_2,
        name="output = [lp.lower() for lp in lst_lp]",
        is_answer=False,
    )


@pytest.fixture
def question_option_2_2(question_2):
    return QuestionOptionFactory(
        question=question_2,
        name="output = [lp.upper() for lp in lst_lp]",
        is_answer=True,
    )


@pytest.fixture
def question_option_2_3(question_2):
    return QuestionOptionFactory(
        question=question_2,
        name="False = [lp.capitalize() for lp in lst_lp]",
        is_answer=False,
    )


@pytest.fixture
def question_option_3_1(question_3):
    return QuestionOptionFactory(
        question=question_3,
        name="output = [n + 1 if n < 4 else n for n in lst_num]",
        is_answer=False,
    )


@pytest.fixture
def question_option_3_2(question_3):
    return QuestionOptionFactory(
        question=question_3,
        name="output = [n + 1 if n < 2 else n for n in lst_num]",
        is_answer=False,
    )


@pytest.fixture
def question_option_3_3(question_3):
    return QuestionOptionFactory(
        question=question_3,
        name="output = [n + 1 if n <= 2 else n for n in lst_num]",
        is_answer=True,
    )
