from django.db import models
from django.contrib.auth.models import User
from Blogs import settings
User=settings.AUTH_USER_MODEL
# Create your models here.
class Post(models.Model):
    titel = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.titel