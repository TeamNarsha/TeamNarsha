from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 30)
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
