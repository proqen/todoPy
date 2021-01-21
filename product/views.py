from django.shortcuts import render, HttpResponse

def go(request):
    return HttpResponse("This is my first page")

def third(request):
    return HttpResponse("This is page test3")