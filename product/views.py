from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, "index.html")


def test(request):
    return render(request, "test.html")


def add(request):
    return render(request, "add.html")


def change(request):
    return render(request, "change.html")


def delete(request):
    return render(request, "delete.html")
