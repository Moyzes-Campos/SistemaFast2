from django.urls import path
from .views import PlanoView

urlpatterns = [
    path('', PlanoView.as_view(), name='plano_index'),
]
