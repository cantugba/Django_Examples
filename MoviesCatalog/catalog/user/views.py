from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth #gönderilen bilgilerle eşleşen kayıtlaarın varlığının sorgulamasını yapıyor
# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user= auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            print('login başarılı')
            return redirect('index')
        else:
            return redirect('login')
            
    else:
        return render(request,'user/login.html')

def register(request):
    if request.method == 'POST':
      #user kayıt
      username = request.POST['username']
      email = request.POST['email']
      password = request.POST['password']
      repassword = request.POST['repassword']
      
      if password == repassword:
          if User.objects.filter(username=username).exists():
              print('Bu kullanıcı adı daha önce alınmıştır')
              return redirect('register')
          else:
              if User.objects.filter(email=email).exists():
                  print('Bu mail daha önce alınmış')
                  return redirect('register')
              else:
                   #everything is fine
                   user = User.objects.create_user(username=username, email=email, password=password)
                   user.save()
                   print('Kullanıcı oluşturuldu')
                   return redirect('login')
      else:
        print('parolalar eşleşmiyor')
        return redirect('register')
      
    else:
        return render(request,'user/register.html')

def logout(request):
    return render(request,'user/logout.html')