from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = 'Sistema UTFAST'  # Muda o nome do nosso sistema de Administração.
admin.site.site_title = 'UTFAST'
admin.site.index_title = 'Sistema de Gerenciamento - UTFAST'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('apps.core.urls')),
    path('dash/', include('apps.dash_index.urls')),
    path('dash/analise', include('apps.analise.urls')),
    path('dash/brainstorm', include('apps.brainstorm.urls')),
    path('dash/calendario', include('apps.calendario.urls')),
    path('dash/licoes', include('apps.licoes.urls')),
    path('dash/plano', include('apps.plano_de_acao.urls')),
    path('dash/regulamento/', include('apps.regulamento.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
