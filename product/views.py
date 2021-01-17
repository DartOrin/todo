from django.shortcuts import render
from .models import ToDo
# Create your views here.


def homepage(request):
    return render(request, "index.html")


def add(request):
    return render(request, "add.html")


def change(request):
    return render(request, "change.html")


def delete(request):
    return render(request, "delete.html")


def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})
