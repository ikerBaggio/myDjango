# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Motor(models.Model):
    CHOPPER = 'CHOPPER'
    CLASSIC = 'CLASSIC'
    CROSS = 'CROSS'
    CRUISER = 'CRUISER'
    ENDURO = 'ENDURO'
    NAKED = 'NAKED'
    SKUTER = 'SKUTER'
    SPORT = 'SPORT'
    TURIST = 'TURIST'
    CUSTOM = 'CUSTOM'
    TYPES = (
        (CHOPPER, 'Chopper'),
        (CLASSIC, 'Klasyk'),
        (CROSS, 'Cross'),
        (CRUISER, 'Cruiser'),
        (ENDURO, 'Enduro'),
        (NAKED, 'Naked'),
        (SKUTER, 'Skuter'),
        (SPORT, 'Sportowy'),
        (TURIST,'Turystyczny'),
        (CUSTOM, 'Inny')
    )
    name = models.CharField(verbose_name='Motor', max_length=30)
    description = models.TextField(max_length=1000, blank=True, verbose_name='Opis')
    types = models.CharField(max_length=15, verbose_name='Typ motocykla', choices=TYPES, default=CUSTOM)
    price = models.DecimalField(max_digits=7, verbose_name='Cena', decimal_places=1)
    date = models.DateField(verbose_name='Data dodania postu', auto_now_add=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return u'%s' % (self.name)

    class Meta:
        verbose_name_plural = 'motocykle'

class AddPartOfMotor(models.Model):
    motor = models.ForeignKey(Motor, on_delete=models.CASCADE, related_name='addtionName')
    nameOwn = models.CharField(verbose_name="Dodatek do motocykla", null=True, max_length=30, blank=True)
    broken = models.BooleanField(default=False, verbose_name="Zepsute", help_text=u"Zaznacz, jeżeli dodatkowa część jest uszkodzona")
    delete_part = models.BooleanField(default=False, verbose_name="Usuń")

    def brokenPart(self):
        if self.broken:
            return 'Uszkodzona część'
        return 'Sprawna część'

    def deletePart(self):
        if self.delete_part:
            self.delete()

    def __unicode__(self):
        return u'%s' % (self.name)

    class Meta:
        verbose_name = "dodatek"
        verbose_name_plural = "Dodadki"



