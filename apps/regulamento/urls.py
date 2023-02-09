from django.urls import path
from .views import RegulamentoView

urlpatterns = [
    path('', RegulamentoView.as_view(), name='regulamento_index'),
    path('Aerodinâmica', RegulamentoView.as_view(), name='regulamento_indexAE'),
    path('Elétrica', RegulamentoView.as_view(), name='regulamento_indexEL'),
    path('Direção', RegulamentoView.as_view(), name='regulamento_indexDS'),
    path('Estrutura', RegulamentoView.as_view(), name='regulamento_indexES'),
    path('Freio', RegulamentoView.as_view(), name='regulamento_indexFR'),
    path('Powertrain', RegulamentoView.as_view(), name='regulamento_indexPW'),
    path('Comercial', RegulamentoView.as_view(), name='regulamento_indexCM'),
    path('Gestão', RegulamentoView.as_view(), name='regulamento_indexGS'),
    path('Financeiro', RegulamentoView.as_view(), name='regulamento_indexFN'),
    path('Marketing', RegulamentoView.as_view(), name='regulamento_indexMK'),
]
