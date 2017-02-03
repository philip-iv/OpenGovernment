import requests
import csv
from datetime import datetime
import django

from django.db import models
from us.models import Senator, Representative, Person

django.setup()

getPerson(first, last, dob):
    try:
        person = Person.objects.get(first_name=first, last_name=last, birth=dob)
    except:
        return None
    if person.senator:
        return person.senator
    else if person.representative:
        return person.representative
    else:
        return person
        
readCsv(file):
    with open('legislators.csv', 'r') as file:
    reader = csv.DictReader(file)
    count = 0
    for row in reader:
        per = getPerson(row['firstname'], row['lastname'], row[''])
        if row['title']=='Sen':
            per = s if (s=Senator.objects.get())
            per.seniority = row['district'][0]
        else:
            per = Representative()
            per.district = int(row['district'])
        per.first_name = row['firstname']
        per.middle_name = row['middlename']
        per.last_name = row['lastname']
        per.suffix = row['name_suffix']
        per.gender = row['gender']
        per.party = row['party']
        per.state = row['state']
        per.birth = datetime.strptime(row['birthdate'], '%Y-%m-%d').date()
        per.save()