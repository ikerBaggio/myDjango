# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views  # import widoków aplikacji
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from .models import Motor

app_name = 'motor'  # przestrzeń nazw aplikacji
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^lista/', login_required(ListView.as_view(model=Motor)),
        name='lista'),
    url(r'^dodaj/$', views.MotorCreate.as_view(), name='dodaj'),
    url(r'^edytuj/(?P<pk>\d+)/', views.MotorUpdate.as_view(), name='edytuj'),
    url(r'^usun/(?P<pk>\d+)/', views.MotorDelete.as_view(), name='usun'),
    url(r'^info/(?P<pk>\d+)/', views.MotorDetailView.as_view(), name='info'),
]
