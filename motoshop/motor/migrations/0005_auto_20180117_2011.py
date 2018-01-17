# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-01-17 19:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('motor', '0004_auto_20180117_1938'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addpartofmotor',
            old_name='name',
            new_name='nameOwn',
        ),
        migrations.AlterField(
            model_name='addpartofmotor',
            name='motor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dodki', to='motor.Motor'),
        ),
        migrations.AlterField(
            model_name='motor',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='dodano'),
        ),
        migrations.AlterField(
            model_name='motor',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Motor'),
        ),
    ]