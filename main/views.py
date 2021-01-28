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

def removeToDo(request):
    return render(request, "removeToDo.html")

def updateToDo(request):
    return render(request, "updateToDo.html")