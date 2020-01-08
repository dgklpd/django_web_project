#coding=utf-8
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#Create your models here.
class Entry(models.Model):
    """类比"""
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
	    verbose_name_plural = 'entries'
		
    def _str_(self):
        return self.text[:50] + "..."

