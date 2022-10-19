from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=40)
    image=models.CharField(max_length=40)
    description=models.TextField()
    is_active=models.BooleanField(default=False)

class Category(models.Model):
    name=models.CharField(max_length=50)