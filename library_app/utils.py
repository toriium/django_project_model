from django.contrib.admin.models import ADDITION, LogEntry
from django.contrib.auth.models import User


def log_admin_addition(user: User, instance, change_message: str):
    if not user.is_authenticated:
        return

    LogEntry.objects.log_actions(
        user_id=user.pk,
        queryset=instance.__class__.objects.filter(pk=instance.pk),
        action_flag=ADDITION,
        change_message=change_message,
        single_object=True,
    )
