from django.db import models
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
def __str__(self):
    return self.name

# Create your models here.
class Person(models.Model):
    names=models.CharField(max_length=300)
    imgs=models.ImageField(upload_to='pics')
    descr=models.TextField()
def __str__(self):
    return self.names