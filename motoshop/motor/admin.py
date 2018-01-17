# -*- coding: utf-8 -*-
from django.contrib import admin
from . import models
from django.forms import Textarea
from django.db.models.fields import TextField


class AddPartOfMotorInline(admin.TabularInline):
    model = models.AddPartOfMotor
    fields = ['nameOwn', 'broken']
    extra = 1
    max_num = 10


@admin.register(models.Motor)
class MotorAdmin(admin.ModelAdmin):
    exclude = ('author',)
    inlines = [AddPartOfMotorInline]
    search_fields = ['name']
    list_per_page = 10
    formfield_overrides = {
        TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 100})},
    }

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()