from django.http import request, HttpResponse
from django.shortcuts import render
import os
from django.conf import settings


def removepunc(request):
    # return HttpResponse("hi this is home page")
    # print(request.GET.get('text','default'))
    return render(request,'index.html')
    print(text)

def contact(request):
    return HttpResponse("hi this is contact page")

def home(request):
    return HttpResponse('finally done some part')

def hey(request):
    return HttpResponse("")

def __init__ (self):
    removepuc()
