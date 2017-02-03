import requests
import csv
from datetime import date
import django

from django.db import models
from us.models import Senator

django.setup()

with open('legislators.csv', 'r') as file:
    reader = csv.DictReader(file)
    count = 0
    for row in [p for p in reader if p['title'] == 'Sen']:
        sen = Senator()
        sen.first_name = row['firstname']
        sen.middle_name = row['middlename']
        sen.last_name = row['lastname']
        sen.suffix = row['name_suffix']
        sen.gender = row['gender']
        sen.party = row['party']
        sen.state = row['state']
        sen.birth = date.strptime(row['birthdate'], '%Y-%m-%d')
        sen.seniority = row['district'][0]
        sen.save()