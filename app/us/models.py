from __future__ import unicode_literals

from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    suffix = models.CharField(max_length=2)
    gender = models.CharField(max_length=1)
    hometown = models.CharField(max_length=100)
    party = models.CharField(max_length=10)
    birth = models.DateField(null=True)
    image = models.FileField()