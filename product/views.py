from django.shortcuts import render, HttpResponse

def go(request):
    return HttpResponse("This is my first page")