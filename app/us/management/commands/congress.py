import requests
import urllib
import csv
from datetime import datetime
import django
import os

from django.db import models
from django.core.management.base import BaseCommand, CommandError
from us.models import Person
from us.congress.models import Congressman, Senator, Representative

def get_csv(file_name):
    urllib.urlretrieve('http://unitedstates.sunlightfoundation.com/legislators/legislators.csv', file_name)

def get_person(row):
    try:
        bioguide_id = row['bioguide_id']
        person = Congressman.objects.get(bioguide_id=bioguide_id)
    except:
        office = row['title']
        per = None
        if office == 'Sen':
            per = Senator()
            per.seniority = row['district'][0]
        else:
            per = Representative()
            per.district = int(row['district'])
        per.bioguide_id = row['bioguide_id']
        per.birth = datetime.strptime(row['birthdate'], '%Y-%m-%d').date()
        per.first_name = row['firstname']
        per.middle_name = row['middlename']
        per.suffix = row['name_suffix']
        per.gender = row['gender']
        per.state = row['state']
        return per
    
    try:
        return person.senator
    except:
        pass
    try:
        return person.representative
    except:
        pass
    return person
        
def read_csv(file_name):
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            person = get_person(row)
            person.last_name = row['lastname']
            person.party = row['party']
            person.in_office = bool(int(row['in_office']))
            person.save()
            
class Command(BaseCommand):
    def handle(self, *args, **options):
        Senator.objects.all().delete()
        Representative.objects.all().delete()
        Person.objects.all().delete()
        file_name = 'legislators.csv'
        #get_csv(file_name)
        read_csv(file_name)
        #os.remove(file_name)