from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import FluxodeCX, Lembrete, Integrantes, Atividade, ObjetivosArea


@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
    template_name = 'index_dash.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['fluxo'] = FluxodeCX.objects.all().order_by('data')
        context['lembretes'] = Lembrete.objects.all()
        context['pagina'] = 'Home'
        usuario = self.request.user
        context['usuario'] = usuario
        areas = ["Aerodinâmica", "Direção e Suspenção", "Elétrica", "Estrutura", "Freio e Ergonomia", "Powertrain",
                 "Comercial", "Financeiro", "Gestão de Pessoas", "Marketing"]
        tam_areas = []
        for a in areas:
            b = Integrantes.objects.filter(area=a).count()
            tam_areas.append(b)
        context['tam_areas'] = tam_areas

        area = self.request.path.split("/")[-1]

        context['atividades'] = Atividade.objects.all().filter(area=area)
        context['objetivos'] = ObjetivosArea.objects.all().filter(area=area)
        context['integrantes'] = Integrantes.objects.all().filter(area=area)

        if area == '':
            context['teste'] = 'Geral'
        else:
            context['teste'] = area

        tamanho = Atividade.objects.filter(area=area).count()
        if tamanho > 0:
            tam_AF = Atividade.objects.filter(area=area).filter(situacao='AF').count() / tamanho
            tam_AF = int(tam_AF * 100)
            tam_FA = Atividade.objects.filter(area=area).filter(situacao='FA').count() / tamanho
            tam_FA = int(tam_FA * 100)
            tam_FE = Atividade.objects.filter(area=area).filter(situacao='FE').count() / tamanho
            tam_FE = int(tam_FE * 100)
            context['tamanhos'] = (tam_AF, tam_FA, tam_FE)

        return context
