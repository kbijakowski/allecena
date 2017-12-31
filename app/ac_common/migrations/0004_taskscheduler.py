# coding: utf-8
# Generated by Django 1.9 on 2016-01-09 21:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djcelery', '0001_initial'),
        ('ac_common', '0003_user_auth_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskScheduler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodic_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djcelery.PeriodicTask')),
            ],
        ),
    ]