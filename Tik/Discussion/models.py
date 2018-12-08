from django.db import models
from django.urls import reverse

# Create your models here.
class  Discussion(models.Model):
    author=models.CharField(max_length=15)
    title=models.CharField(max_length=50)
    argument=models.CharField(max_length=350)
    slug=models.SlugField(max_length=31,unique=True)
    created_on=models.DateField(auto_now=True)
    def get_absolute_url(self):
        return reverse('discussion_detail',kwargs={'slug':self.slug})
    def __str__(self):
        return self.title

class Comments(models.Model):
    username=models.CharField(max_length=15)
    comment_text=models.TextField(max_length=200)
    discussion=models.ManyToManyField(Discussion)
