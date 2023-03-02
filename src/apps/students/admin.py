from django.contrib import admin
from apps.users.models import User
from .models import Student, StudentQuiz, StudentQuizAnswer


class StudentAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if form.base_fields.get("user"):
            form.base_fields["user"].queryset = User.objects.filter(
                role=User.RoleChoices.student
            )
        return form


class StudentQuizAnswerInline(admin.TabularInline):
    model = StudentQuizAnswer
    readonly_fields = ["is_answer"]
    extra = 0

    def is_answer(self, obj):
        if obj.question_option.is_answer:
            return "Yes"
        return "No"


class StudentQuizAdmin(admin.ModelAdmin):
    list_display = ["created_at", "get_quiz_name", "score"]
    inlines = [StudentQuizAnswerInline]

    def get_quiz_name(self, obj):
        return obj.quiz.name

    get_quiz_name.short_description = "Quiz"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(student__user=request.user)


admin.site.register(Student, StudentAdmin)
admin.site.register(StudentQuiz, StudentQuizAdmin)
