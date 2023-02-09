from django.urls import path
from .views import AnaliseView

urlpatterns = [
    path('', AnaliseView.as_view(), name='analise_index'),
]
