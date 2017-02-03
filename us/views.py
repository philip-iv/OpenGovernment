import csv
import datetime

from django.db import models
from us.models import Senator
from django.shortcuts import render

def index(request):
    with open('scraping/legislators.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in [p for p in reader if p['title'] == 'Sen']:
            sen = Senator()
            sen.first_name = row['firstname']
            sen.middle_name = row['middlename']
            sen.last_name = row['lastname']
            sen.suffix = row['name_suffix']
            sen.gender = row['gender']
            sen.party = row['party']
            sen.state = row['state']
            sen.birth = datetime.datetime.strptime(row['birthdate'], '%Y-%m-%d').date()
            sen.seniority = row['district'][0]
            sen.save()
    return render(request, 'us/index.html', {})