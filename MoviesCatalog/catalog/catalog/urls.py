from django.contrib import admin
from django.urls import path ,include

#http://127.0.0.1:8000/
urlpatterns = [
    path('',include('pages.urls')),
    path('admin/', admin.site.urls),

]
