from django.shortcuts import render
from allauth.account.forms import SignupForm
from .models import Task
from .forms import TaskForm


def home(request):
    # if we have a GET request
    if request.method == "GET":
        # retrieve the old tasks if our user is logged in
        if request.user.is_authenticated:
            tasks = Task.objects.filter(user=request.user)
        else:
            tasks = None
        # render the form
        form = TaskForm()
        # Return our home template.
        return render(
            request, "home.html", {"form": form, "tasks": tasks, "errors": None}
        )

    # request method is POST
    else:
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            # we would only return our tasks components with the updated tasks
            tasks = Task.objects.filter(user=request.user)

            return render(
                request,
                "components/tasks.html",
                {
                    "form": TaskForm(),
                    "tasks": tasks,
                    "errors": None,
                },  # a new empty form, since we saved the posted one
            )

        # form is not valid, we have some kind of error
        else:
            errors = form.errors
            tasks = Task.objects.filter(user=request.user)
            # we would return only our tasks components with the old tasks, and the errors
            return render(
                request,
                "components/tasks.html",
                {
                    "form": form,
                    "tasks": tasks,
                    "errors": errors,
                },  # the posted form, since it didn't save
            )


def auth(request):
    return render(request, "components/auth.html")
