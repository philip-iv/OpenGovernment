from __future__ import unicode_literals

from django.db import models
from us.models import Person

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
