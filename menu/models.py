from django.db import models
from django.urls import reverse

# Create your models here.

class Coffee(models.Model):
    title = models.CharField(max_length=100)
    sub_cate = models.CharField(max_length=100, default='')
    photo = models.ImageField(upload_to='coffee/%Y/%m/%d',default='coffee/no_image.png')
    desc = models.TextField()
    
    class Meta:
        ordering = ['title']
        
    def __str__(self):
        return self.title
    
    
class Beverage(models.Model):
    title = models.CharField(max_length=100)
    sub_cate = models.CharField(max_length=100, default='')
    photo = models.ImageField(upload_to='beverage/%Y/%m/%d',default='beverage/no_image.png')
    desc = models.TextField()
    
    class Meta:
        ordering = ['title']
        
    def __str__(self):
        return self.title
    
class Desert(models.Model):
    title = models.CharField(max_length=100)
    sub_cate = models.CharField(max_length=100, default='')
    photo = models.ImageField(upload_to='desert/%Y/%m/%d',default='desert/no_image.png')
    desc = models.TextField()
    
    class Meta:
        ordering = ['title']
        
    def __str__(self):
        return self.title
    
class SeasonMenu(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='seasonmenu/%Y/%m/%d',default='seasonmenu/no_image.png')
    desc = models.TextField()
    
    class Meta:
        ordering = ['title']
        
    def __str__(self):
        return self.title

        
        