# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-05 02:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('us', '0003_auto_20170203_0244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='congressman',
            name='person_ptr',
        ),
        migrations.RemoveField(
            model_name='representative',
            name='congressman_ptr',
        ),
        migrations.RemoveField(
            model_name='senator',
            name='congressman_ptr',
        ),
        migrations.DeleteModel(
            name='Congressman',
        ),
        migrations.DeleteModel(
            name='Representative',
        ),
        migrations.DeleteModel(
            name='Senator',
        ),
    ]
