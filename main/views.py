from django.shortcuts import render, HttpResponse

def homepage(request):
    return render(request,"index.html")
    
def test(request):
    return render(request, "test.html")

def addToDo(request):
    return render(request, "addToDo.html")

def removeToDo(request):
    return render(request, "removeToDo.html")

def updateToDo(request):
    return render(request, "updateToDo.html")