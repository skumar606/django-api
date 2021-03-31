from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=60, unique=True)
    password = models.CharField(max_length=60)
    def __str__(self):
        return self.username

class UserLoginHistory(models.Model):
    userid = models.CharField(max_length=60, null=True)
    login_time = models.DateTimeField(default=datetime.datetime.now())
    ip_address = models.CharField(max_length=60)
    def __str__(self):
        return str(self.userid)
