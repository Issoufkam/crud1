import email
from email.mime import image
from turtle import update
from django.db import models

# Create your models here.
class User(models.Model):
    fisrt_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=50)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    created_at = models.DateTimeField( auto_now_add = True)
    update_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "utilisateurs"