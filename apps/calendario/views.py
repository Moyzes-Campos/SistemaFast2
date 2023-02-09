from django.shortcuts import render
from django.views.generic import TemplateView


class CalendarioView(TemplateView):
    template_name = 'calendario.html'
