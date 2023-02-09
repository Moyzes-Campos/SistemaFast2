from django.shortcuts import render
from django.views.generic import TemplateView


class AnaliseView(TemplateView):
    template_name = 'analise_index.html'
