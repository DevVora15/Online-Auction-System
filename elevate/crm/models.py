from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission

# Create your models here.
class CustomUser(AbstractUser):
    birthday = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True, null=True)  # Add the 'address' field
    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, related_name='customuser_groups')
    user_permissions = models.ManyToManyField(Permission, verbose_name='user permissions', blank=True, related_name='customuser_permissions')

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    message = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self) :
        return 'Message from ' + self.first_name + ' - ' + self.email
    