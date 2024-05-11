from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse('hello , bomacat')


def login_view(request):
    return HttpResponse('login plaease')