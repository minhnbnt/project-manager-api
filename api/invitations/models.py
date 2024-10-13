from django.contrib.auth.models import User
from django.db import models

from api.models import Project


class Invitation(models.Model):
    title = models.CharField(max_length=50)
    context = models.CharField(max_length=200)
    status = models.BooleanField(default=False)

    receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="receiver",
        default=1,
    )

    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="sender",
        default=1,
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        blank=False,
        null=True,
        related_name="project",
    )
