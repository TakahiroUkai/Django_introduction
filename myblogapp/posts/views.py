from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(request):
    posts = Post.objects.order_by("-published")
    return render(request, "posts/index.html", {"posts":posts})
    # postsのデータを変数に保持した状態でhtmlがよびだされる→呼び出された方で変数の値を取り出す

def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, "posts/post_detail.html",{"post":post})
    # Create your views here.
