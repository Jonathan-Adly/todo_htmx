from django.db import models
from django.contrib.auth import get_user_model


class Task(models.Model):
    user = models.OneToOneField(
        get_user_model(), on_delete=models.CASCADE, related_name="tasks"
    )
    name = models.CharField(max_length=250)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name
