from django.shortcuts import render, HttpResponse
from .models import ToDo

def homepage(request):
    return render(request,"index.html")
    
def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list" : todo_list})

def addToDo(request):
    return render(request, "addToDo.html")

def removeToDo(request):
    return render(request, "removeToDo.html")

def updateToDo(request):
    return render(request, "updateToDo.html")