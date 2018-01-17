# -*- coding: utf-8 -*-

# from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from . import models
from . import forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.views.generic import DetailView


def index(request):
    """Strona główna"""
    kontekst = {'komunikat': 'Witaj w aplikacji Motor!'}
#    return render(request, 'motor/index.html', kontekst)
    return TemplateResponse(request, 'motor/index.html', kontekst)


@method_decorator(login_required, 'dispatch')
class MotorCreate(CreateView):

    model = models.Motor
    form_class = forms.MotorForm
    success_url = reverse_lazy('motor:lista')
    def get_context_data(self, **kwargs):
        context = super(MotorCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            context['addtionName'] = forms.AddPartOfMotorFormSet(self.request.POST)
        else:
            context['addtionName'] = forms.AddPartOfMotorFormSet()
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        addition = forms.AddPartOfMotorFormSet(self.request.POST)
        if form.is_valid() and addition.is_valid():
            return self.form_valid(form, addition)
        else:
            return self.form_invalid(form, addition)

    def form_valid(self, form, addition):
        form.instance.author = self.request.user
        self.object = form.save()
        addition.instance = self.object
        addition.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, addition):
        return self.render_to_response(
            self.get_context_data(form=form, addtionName=addition)
        )


@method_decorator(login_required, 'dispatch')
class MotorUpdate(UpdateView):
    model = models.Motor
    form_class = forms.MotorForm
    success_url = reverse_lazy('motor:lista')

    def get_context_data(self, **kwargs):
        context = super(MotorUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            context['addtionName'] = forms.AddPartOfMotorFormSet(
                self.request.POST,
                instance=self.object)
        else:
            context['addtionName'] = forms.AddPartOfMotorFormSet(instance=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        addition = forms.AddPartOfMotorFormSet(
            self.request.POST,
            instance=self.object)
        if form.is_valid() and addition.is_valid():
            return self.form_valid(form, addition)
        else:
            return self.form_invalid(form, addition)

    def form_valid(self, form, addition):
        form.instance.autor = self.request.user
        self.object = form.save()
        addition.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, addition):
        return self.render_to_response(
            self.get_context_data(form=form, addtionName=addition)
        )


@method_decorator(login_required, 'dispatch')
class MotorDelete(DeleteView):
    model = models.Motor
    success_url = reverse_lazy('motor:lista')

    def get_context_data(self, **kwargs):
        context = super(MotorDelete, self).get_context_data(**kwargs)
        addition = models.AddPartOfMotor.objects.filter(motor=self.object)
        context['addtionName'] = addition
        return context


@method_decorator(login_required, 'dispatch')
class MotorDetailView(DetailView):
    model = models.Motor

    def get_context_data(self, **kwargs):
        context = super(MotorDetailView, self).get_context_data(**kwargs)
        addition = models.AddPartOfMotor.objects.filter(motor=self.object)
        context['addtionName'] = addition
        return context
