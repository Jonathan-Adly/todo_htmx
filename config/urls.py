from django.contrib import admin
from django.urls import path, include

# delete
# from django.http import HttpResponse

# delete
# def home(request):
# return HttpResponse("Hello, world. This is a django boilerplate!")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("todo.urls")),  # new
    # path("", home, name="home"), - old line
]
