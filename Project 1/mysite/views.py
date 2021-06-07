from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'home.html')


def about(request):
    return HttpResponse("<h1>About<h1>")


def contact(request):
    return HttpResponse("<h1>Contact<h1>")