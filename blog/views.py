from django.shortcuts import render, get_object_or_404

from .models import blog1

# Create your views here.
def allblogs1(request):
    blogs3 = blog1.objects
    return render(request, 'blog/allblogs2.html', {'blogs3':blogs3})

def detail(request, blog_id):
    detailblog = get_object_or_404(blog1, pk=blog_id)
    return render(request, 'blog/detail1.html', {'blog1':detailblog} )
