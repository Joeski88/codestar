from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.

def my_blog(request):
    return HttpResponse("Hello, Blog")
