# -*- coding: utf-8 -*-

from django.forms import ModelForm, Textarea
from . import models
from django.forms.models import inlineformset_factory


class MotorForm(ModelForm):

    class Meta:
        model = models.Motor
        exclude = ('date', 'author')
        widgets = {'description': Textarea(attrs={'rows': 2, 'cols': 80})}

AddPartOfMotorFormSet = inlineformset_factory(
    parent_model=models.Motor,
    model=models.AddPartOfMotor,
    max_num=6,
    min_num=0,
    validate_max=False,
    validate_min=True,
    extra=2,
    fields=('nameOwn', 'broken')
)