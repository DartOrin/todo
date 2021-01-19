from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, Book
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


def books(request):
    books_list = Book.objects.all()
    return render(request, "books.html", {"books_list": books_list})


def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)


def add_book(request):
    form = request.POST
    title = form["title"]
    subtitle = form["subtitle"]
    description = form["description"]
    price = float(form["price"])
    genre = form["genre"]
    author = form["author"]
    year = form["year"]
    book = Book(title=title, subtitle=subtitle, description=description,
                price=price, genre=genre, author=author, year=year)
    book.save()
    return redirect(books)


def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)


def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)


def unmark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect(test)


def mark_book(request, id):
    book = Book.objects.get(id=id)
    book.is_favorites = True
    book.save()
    return redirect(books)


def unmark_book(request, id):
    book = Book.objects.get(id=id)
    book.is_favorites = False
    book.save()
    return redirect(books)


def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect(books)
