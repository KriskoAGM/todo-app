from django.db import models

from todo_app.auth_user.models import Profile

# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    title = models.CharField(
        max_length=100
    )
    description = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    due_date = models.DateField(
        null=True,
        blank=True
    )

    completed = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.title
