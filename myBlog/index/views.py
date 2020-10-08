
from django.shortcuts import render,HttpResponse

def index_view(request):
    if request.user.is_authenticated:
        context = {'who':'Admin',}
    else:
        context = {'who': 'Anonymous', }
    return render(request,'index.html',context)
