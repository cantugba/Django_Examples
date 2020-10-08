from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import Post
def postIndex(request):
    posts = Post.objects.all()
    return render(request,"post/index-post.html",{'posts':posts})

def postDetail(request,id):
    post = get_object_or_404(Post,id =id)
    return render(request, 'post/detail-post.html', {'post':post})

def postCreate(request):
    return HttpResponse('<center><h1>POST</h1></center>')

def postDelete(request):
    return HttpResponse('<center><h1>POST</h1></center>')


def postUpdate(request):
    return HttpResponse('<center><h1>POST</h1></center>')