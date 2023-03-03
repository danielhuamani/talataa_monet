# Talataa Challenge


## Before Project Run

copy .env.template paste in docker/ and rename it with .env with their variables
## Project Run

### Build 
```
make build
```

### Run 
```
make run
```

### Run Migrations and Migrate

open other terminal
```
make migrations
```

```
make migrate
```

## Project Run Unit Test

### Run Test
```
make test
```


Image Coverage
![Alt text](./coverage.png "swagger auth")


## Entity Relationship Diagram - Main Entities


```mermaid
erDiagram
    User ||--|| Student: student
    User{
        int id PK
        string email
        string first_name
        string last_name
        string role
        string password
        datetime date_joined
        bool is_active
        bool is_staff
        bool is_superuser
    }

    Student{
        int id PK
        int user_id FK
        string level
    }

    StudentQuiz{
        int id PK
        int quiz_id FK
        int student_id FK
        datetime created_at
        datetime updated_at
        int score
    }

    StudentQuizAnswer{
        int id PK
        int student_quiz_id FK
        int question_id FK
        int question_option_id FK
        datetime created_at
        datetime updated_at
    }

    Student ||--|{ StudentQuiz: student_quizzes

    StudentQuiz ||--|{ StudentQuizAnswer: student_quiz_answers

    Question ||--|{ StudentQuizAnswer: student_quiz_answers

    QuestionOption ||--|{ StudentQuizAnswer: student_quiz_answers

    Quiz ||--|{ StudentQuiz: student_quizzes
    Quiz ||--|{ Question: questions
    Question ||--|{ QuestionOption: question_options
    Quiz{
        int id PK
        string name
        int time_for_quiz
    }
    Question{
        int id PK
        int quiz_id FK
        datetime created_at
        datetime updated_at
        bool is_active
        string name
        string content
        int score
        int position
    }
    QuestionOption{
        int id PK
        int question_id FK
        datetime created_at
        datetime updated_at
        bool is_answer
        string name
        int position
    }
```