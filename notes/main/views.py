from django.http import HttpResponse
from django.shortcuts import render


def hi(request):
    return HttpResponse("<h1>Hi</h1>")