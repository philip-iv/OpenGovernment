# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-05 02:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('us', '0004_auto_20170205_0202'),
    ]

    operations = [
        migrations.CreateModel(
            name='Congressman',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='us.Person')),
                ('state', models.CharField(max_length=2)),
                ('elected', models.DateField(null=True)),
                ('in_office', models.BooleanField(default=False)),
            ],
            bases=('us.person',),
        ),
        migrations.CreateModel(
            name='Representative',
            fields=[
                ('congressman_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='congress.Congressman')),
                ('district', models.IntegerField()),
            ],
            bases=('congress.congressman',),
        ),
        migrations.CreateModel(
            name='Senator',
            fields=[
                ('congressman_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='congress.Congressman')),
                ('seniority', models.CharField(max_length=1)),
            ],
            bases=('congress.congressman',),
        ),
    ]
