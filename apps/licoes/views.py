from django.shortcuts import render
from django.views.generic import TemplateView


class LicoesView(TemplateView):
    template_name = 'licoes_index.html'
