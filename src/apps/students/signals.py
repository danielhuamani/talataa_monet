from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from .models import Student


@receiver(post_save, sender=Student)
def student_create(sender, instance, created, **kwargs):
    if created:
        permission = Permission.objects.filter(
            codename__in=Student.PERMISSION_ADMIN
        )
        instance.user.user_permissions.add(*permission)
