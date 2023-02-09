from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from .models import Regulamento


@method_decorator(login_required, name='dispatch')
class RegulamentoView(TemplateView):
    template_name = 'regulamento_index.html'

    def get_context_data(self, **kwargs):
        context = super(RegulamentoView, self).get_context_data(**kwargs)
        context['pagina'] = 'Regulamento'
        usuario = self.request.user
        context['usuario'] = usuario

        area = self.request.path.split("/")[-1]

        reg = Regulamento.objects.all().filter(area=area)
        context['t1'] = reg.distinct('t1')
        context['t2'] = reg.distinct('t2')
        context['regulamento'] = Regulamento.objects.all().filter(area=area)

        if area == '':
            context['teste'] = 'Geral'
        else:
            context['teste'] = area

        return context

