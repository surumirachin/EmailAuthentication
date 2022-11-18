from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=200,default='')
    date=models.DateField()
    attachment = models.FileField(upload_to="media/",blank=True,null=True)
    
    
    def __str__(self):
        return self.title
gender=(
    ('Male','Male'),
    ('Female','Female'),
    ('other','other')
)
class User(AbstractUser):
    email = models.EmailField("Email address", unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=50,choices=gender)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
