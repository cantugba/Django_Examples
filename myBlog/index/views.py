from django.shortcuts import render,HttpResponse
#python kodlarının yazılacağı yerdir
# Create your views here.

def index_view(request):
    if request.user.is_authenticated: context = {"who":"Admin"}#Kullanıcı oturumu açmış mı açmamış mı kontrolü
    else: context = {"who": "Anonymous",}
    return render(request,"index.html",context)