# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-06 23:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('us', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Representative',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='us.Person')),
                ('state', models.CharField(max_length=2)),
                ('elected', models.DateField(null=True)),
                ('in_office', models.BooleanField(default=False)),
                ('bioguide_id', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('district', models.IntegerField(null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('us.person',),
        ),
        migrations.CreateModel(
            name='Senator',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='us.Person')),
                ('state', models.CharField(max_length=2)),
                ('elected', models.DateField(null=True)),
                ('in_office', models.BooleanField(default=False)),
                ('bioguide_id', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('seniority', models.CharField(max_length=1)),
            ],
            options={
                'abstract': False,
            },
            bases=('us.person',),
        ),
    ]
