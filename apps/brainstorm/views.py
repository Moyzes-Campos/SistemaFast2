from django.shortcuts import render
from django.views.generic import TemplateView


class BrainstormView(TemplateView):
    template_name = 'brainstorm_index.html'
