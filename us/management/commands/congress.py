import requests
import urllib
import csv
from datetime import datetime
import django

from django.db import models
from django.core.management.base import BaseCommand, CommandError
from us.models import Senator, Representative, Person

def get_csv(file_name):
    urllib.urlretrieve('http://unitedstates.sunlightfoundation.com/legislators/legislators.csv', file_name)

def get_person(row):
    try:
        first = row['firstname']
        last = row['lastname']
        dob = datetime.strptime(row['birthdate'], '%Y-%m-%d').date()
        person = Person.objects.get(first_name=first, last_name=last, birth=dob)
    except:
        office = row['title']
        middle = row['middlename']
        suffix = row['name_suffix']
        gender = row['gender']
        state = row['state']
        per = None
        if office == 'Sen':
            per = Senator()
            per.seniority = row['district'][0]
        else:
            per = Representative()
            per.district = row['district']
        per.first_name = first
        per.middle_name = middle
        per.last_name = last
        per.suffix = suffix
        per.gender = gender
        per.birth = dob
        per.state = state
        return per
    
    try:
        return person.congressman.senator
    except:
        pass
    try:
        return person.congressman.representative
    except:
        pass
    return person
        
def read_csv(file_name):
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            person = get_person(row)
            person.party = row['party']
            person.in_office = bool(row['in_office'])
            person.save()
            
class Command(BaseCommand):
    def handle(self, *args, **options):
        #Senator.objects.all().delete()
        #Representative.objects.all().delete()
        file_name = 'legislators.csv'
        get_csv(file_name)
        read_csv(file_name)