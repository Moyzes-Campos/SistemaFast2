from django.shortcuts import render
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'index.html'


class History(TemplateView):
    template_name = 'our_history.html'


class Contato(TemplateView):
    template_name = 'contato.html'
