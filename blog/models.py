from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 30)
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    abcd = models.CharField(max_length = 10, default = '')
    simple = models.CharField(max_length=20)
    gh = models.CharField(max_length=10)
    k_01 = models.CharField(max_length=20)
    k_02 = models.CharField(max_length=20)
    k_03 = models.CharField(max_length=20)
    k_04 = models.CharField(max_length=20)
    ability = models.TextField()
    past = models.TextField()
    future = models.TextField()
    
    def __str__(self):
        return f'[{self.pk}] {self.title}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
