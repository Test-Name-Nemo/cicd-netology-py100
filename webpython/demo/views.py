from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Python in WEB Development by Netology!!!")