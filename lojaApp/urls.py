from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('dashboard', dashboard, name='dashboard'),
    path('adicionar', addProduto, name='addProduto'),
    path('editar/<int:id_produto>', editarProduto, name='editarProduto'),
    path('excluir/<int:id_produto>', excluirProduto, name='excluirProduto'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
