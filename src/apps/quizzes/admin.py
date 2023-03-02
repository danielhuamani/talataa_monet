from django.contrib import admin
import nested_admin
from .models import Quiz, Question, QuestionOption

# Register your models here.


class QuestionOptionInline(nested_admin.NestedTabularInline):
    extra = 1
    model = QuestionOption


class QuestionInline(nested_admin.NestedStackedInline):
    extra = 1
    model = Question
    inlines = [QuestionOptionInline]


class QuizAdmin(nested_admin.NestedModelAdmin):
    inlines = [QuestionInline]


admin.site.register(Quiz, QuizAdmin)
