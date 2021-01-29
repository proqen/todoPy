from django.shortcuts import render, HttpResponse, redirect
from .models import *

def homepage(request):
    return render(request,"index.html")
    
def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list" : todo_list})

def bookGetAll(request):
    book_list = Book.objects.all()
    return render(request, "books.html", {"book_list" : book_list})

def addToDo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)

def removeToDo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def markToDo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)

def unmarkToDo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect(test)

def checkedToDo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(test)

def bookIsFarovite(request, id):
    book = Book.objects.get(id=id)
    book.is_favorite= not book.is_favorite
    book.save()
    return redirect(bookGetAll)

def deleteBook(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect(bookGetAll)

def bookDetails(request, id):
    book = Book.objects.get(id=id)
    return render(request, "book_detail.html", {"book" : book})

def bookAdd(request):
    form = request.POST
    book = Book(title = form["book_title"],
    subtitle=form["book_subtitle"],
    description=form["book_description"],
    price=form["book_price"],
    genre=form["book_genre"],
    author=form["book_author"],
    year=form["book_year"])
    print(book)
    book.save()
    return redirect(bookGetAll)

def book_add(request):
    return render(request, "book_add.html")

def updateToDo(request):
    return render(request, "updateToDo.html")