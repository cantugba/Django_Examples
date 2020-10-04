from django.db import models
#veri tabanıyla ilgili sorgulamalarımızın yapılacağı yerdir.
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE)
    title = models.CharField(max_length=150,verbose_name="Başlık")
    content = models.TextField(verbose_name="İçerik")
    created_date = models.DateTimeField(verbose_name="Yayınlanma Tarihi") #verbose name kullancılar tarafında görünecek isimdir.

    def __str__(self):
        return self.title