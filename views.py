from django.shortcuts import render
from .models import Post
from .forms import PostForm

def home(request):
    form=PostForm()
    return render(request,'HtmlEditor/home.html',{'form':form})
