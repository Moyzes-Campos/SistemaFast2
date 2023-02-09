from django.urls import path
from .views import BrainstormView

urlpatterns = [
    path('', BrainstormView.as_view(), name='brainstorm_index'),
]
