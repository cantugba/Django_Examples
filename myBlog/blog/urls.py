from  django.urls import path
from .views import *

urlpatterns = [
    path("index/", postIndex),
    path("index/", postDetail),
    path("index/", postCreate),
    path("index/", postDelete),
    path("index/", postUpdate),


]