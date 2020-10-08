from django.contrib import admin
from .models import Post

class Customize(admin.ModelAdmin):
    list_display = ['title','author','created_date']
    list_filter = ['created_date']
    list_editable = ['title','created_date']
    search_fields = ['title']
    list_display_links = ['author']
    class Meta:
        model = Post

admin.site.register(Post,Customize)
# Register your models here.
