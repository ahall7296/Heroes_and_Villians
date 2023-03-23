from django.db import models

# Create your models here.
class SuperType(models.Model):
    """this is a super type model hereo, villain"""
    type = models.CharField(max_length=250)