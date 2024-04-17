# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, UserManager
from django.contrib.auth.hashers import make_password
import random
import string
from django.conf import settings
import random
import string
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.models import AbstractUser, UserManager


def generate_random_password():
    # Generate a random password with 10 characters
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))


class CustomUserManager(UserManager):
    def authenticate(self, username=None, password=None):
        try:
           # user = self.get(username=username, password=password)
            user = CustomUser.objects.filter(username=username).first()
            if user and user.check_password(password):
                return user
            else:
                return None
        except self.model.DoesNotExist:
            return None
        
    def getDetails(self, username=None):
        try:
           # user = self.get(username=username, password=password)
            user = CustomUser.objects.filter(username=username).first()
            if user is not None:
                new_password = generate_random_password()
                user.set_password(new_password)
                user.save()
                details = [user.email,user.first_name,new_password]
                return details
            else:
                return None
        except self.model.DoesNotExist:
            return None

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    username = models.CharField(max_length=100,unique=True)
    phone_number = models.IntegerField(unique=True)
    password = models.CharField(max_length=100)
    status = models.CharField(max_length=20,default='Regular')
    bio = models.TextField(default="ADD BIO")
    
    groups = models.ManyToManyField(Group, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users')

    objects = CustomUserManager()  # Use the custom manager






class graphDetails(models.Model):
    year = models.IntegerField()
    month = models.CharField(max_length=100)
    customerCount = models.IntegerField()