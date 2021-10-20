from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("auth", views.auth, name="auth"),
    path("<int:task_id>/complete", views.complete, name="complete"),
]
