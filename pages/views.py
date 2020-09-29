from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>You're welcome to my homepage</h1>")

