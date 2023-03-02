from django.contrib import admin
from apps.users.models import User
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["user"].queryset = User.objects.filter(
            role=User.RoleChoices.student
        )
        return form


admin.site.register(Student, StudentAdmin)
