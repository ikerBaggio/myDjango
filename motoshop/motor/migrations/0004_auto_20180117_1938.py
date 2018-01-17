# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-01-17 18:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('motor', '0003_auto_20180117_1823'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddPartOfMotor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='dodatek')),
                ('broken', models.BooleanField(default=False, help_text='Zaznacz, jeżeli dodatkowa część jest uszkodzona', verbose_name='broken')),
                ('motor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dodatki', to='motor.Motor')),
            ],
            options={
                'verbose_name': 'dodatek',
                'verbose_name_plural': 'dodatki',
            },
        ),
        migrations.RemoveField(
            model_name='partofmotor',
            name='motor',
        ),
        migrations.DeleteModel(
            name='PartOfMotor',
        ),
    ]