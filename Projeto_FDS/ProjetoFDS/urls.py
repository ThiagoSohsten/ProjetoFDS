from django.contrib import admin
from django.urls import path, include
from loja.views import registro, nicho, home, avaliacao, login_view, logout_view, carrinho, adicionar_ao_carrinho, remover_do_carrinho, confirmar_compra
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/', registro, name='registro'),  # Usa 'registro' importado de 'loja.views'
    path('nicho/', nicho, name='nicho'),  # Usa 'nicho' importado de 'loja.views'
    path('home/', home, name='home'),
    path('avaliacao/', avaliacao, name='avaliacao'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('carrinho/', carrinho, name='carrinho'),
    path('carrinho/adicionar/<int:produto_id>/', adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('carrinho/remover/<int:produto_id>/', remover_do_carrinho, name='remover_do_carrinho'),
    path('carrinho/confirmar/', confirmar_compra, name='confirmar_compra'),
    path('', home, name='home'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

app_name = 'loja'
