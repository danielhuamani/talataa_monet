from django.apps import AppConfig
from django.db.models.signals import post_save


class StudentsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.students"

    def ready(self):
        from . import signals

        post_save.connect(signals.student_create, sender=self)
