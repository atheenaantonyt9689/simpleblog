from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Entry(models.Model):
    title= models.CharField(max_length=225)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.TextField()
    def _str_(self):
        return self.title