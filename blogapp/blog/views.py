from multiprocessing import context
from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import Blog
# Create your views here.
def index(request):
    context={
        "blogs": Blog.objects.all()
    }
    return render(request, "blog/index.html", context)

def blogs(request):
    context={
        "blogs": Blog.objects.filter(is_active=True)
    }
    return render(request,"blog/blogs.html",context)