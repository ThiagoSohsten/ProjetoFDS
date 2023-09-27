from django.contrib import admin
from django.urls import path
from loja.views import registro, nicho  # Importa as views do aplicativo 'loja'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/', registro, name='registro'),  # Usa 'registro' importado de 'loja.views'
    path('nicho/', nicho, name='nicho'),  # Usa 'nicho' importado de 'loja.views'
]
