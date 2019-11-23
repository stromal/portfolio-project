from django.shortcuts import render

from .models import Blog1

# Create your views here.
def allblogs1(request):
    return render(request, 'blog/allblogs2.html')
