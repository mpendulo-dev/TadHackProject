from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from users.models import *


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class CareerInfo(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(default='default.jpg', upload_to="profile_pic")
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

