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
    birth = models.DateField()
    image = models.FileField()

class Congressman(Person):
    state = models.CharField(max_length=2)
    elected = models.DateField(null=True)
    in_office = models.BooleanField(default=False)
    
    def __unicode__(self):
        return u'%s %s (%s-%s)' % (self.first_name, self.last_name, self.party, self.state)

class Senator(Congressman):
    seniority = models.CharField(max_length=1)

class Representative(Congressman):
    district = models.IntegerField()
