from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Привет, мы рады вас видеть, группа PY100")


