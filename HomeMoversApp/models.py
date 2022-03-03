from enum import unique
from django.db import models
from django import forms
# Create your models here.

class MessageModel(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length = 24, unique=True)
    message = models.TextField(unique=True);




# class MessageModelForm(forms.ModelForm):
#     pass