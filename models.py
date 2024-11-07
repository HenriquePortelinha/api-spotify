from django.db import models
from django.contrib.auth import get_user_model, authenticate
from django import forms
from django.contrib.auth.forms import UserCreationForm
import uuid
from django.utils.translation import gettext_lazy as _
from django.utils import timezone 



# Create your models here.

class Users(models.Model):
    class Meta:
        db_table = 'users'
    
    id_user = models.UUIDField(primary_key="True", default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
class Livros(models.Model):
    class Meta:
        db_table = 'books'
    id_books = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    

    def __str__(self):
        return self.title