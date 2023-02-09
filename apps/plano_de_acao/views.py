from django.shortcuts import render
from django.views.generic import TemplateView


class PlanoView(TemplateView):
    template_name = 'plano_index.html'
