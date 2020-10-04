from django.contrib import admin
from .models import Post
#admin.site.unregister(Post)
#admin.site.register(Post) #modeli admin paneline bağlamak için

#Yönetim panellerinin ayarlarıyla ilgilidir. OLuşturacağımız modeller burada tanımlı olmalıdır.
# Register your models here.
class Customize(admin.ModelAdmin):
    list_display = ["title","author","created_date"] # admin panelinde post edilmiş veride gösterilecek ayarlar
    list_filter = ["created_date"] # filtrelereme yapılacak alanlar için kullanılır.
    search_fields = ["title"] #arama çubuğu ekleyip arancak ayarlar.
    list_display_links = ["author"]
    list_editable = ["title","created_date"] #istenilen alanları güncellemek için kullanılır. Bu komutta uygulanacak alanlar link olarak verilmemiş alanlar olmalı.
    #Yani eğer  list_display_links (atanmış alanlarda belirlenmiş yerlere link vermek için kullanılır.) bölümüne verilen alan ile bu bölüme veirlen alan bir olursa hata verir.


    class Meta:
        model = Post

admin.site.register(Post,Customize)
