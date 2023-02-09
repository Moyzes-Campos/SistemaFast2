from django.urls import path
from .views import LicoesView

urlpatterns = [
    path('', LicoesView.as_view(), name='licoes_index'),
]
