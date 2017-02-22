import csv
import datetime

from django.db import models
from us.congress.models import Senator
from django.shortcuts import render

def index(request):
    return render(request, 'us/index.html', {})