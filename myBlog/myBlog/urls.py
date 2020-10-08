
from django.contrib import admin
from django.urls import path,include
from index.views import index_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index_view),
    path('post/',include('post.urls'))
]
