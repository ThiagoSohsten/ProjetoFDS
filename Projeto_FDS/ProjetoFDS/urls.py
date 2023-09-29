from django.contrib import admin
from django.urls import path
from loja.views import registro, nicho, home, avaliacao  # Importa as views do aplicativo 'loja'
from django.conf import settings
from django.conf.urls.static import static
from loja.views import registro, nicho, home, avaliacao, login_view, logout_view




urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/', registro, name='registro'),  # Usa 'registro' importado de 'loja.views'
    path('nicho/', nicho, name='nicho'),  # Usa 'nicho' importado de 'loja.views'
    path('home/', home, name='home'),
    path('avaliacao/', avaliacao, name='avaliacao'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),



]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
