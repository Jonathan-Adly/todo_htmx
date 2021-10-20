from django import forms
from django.forms import ModelForm
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("name",)
        labels = {
            "name": "Add new task:",
        }
