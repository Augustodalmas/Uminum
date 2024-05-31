from django.urls import path
from Blocos.views import  listaBlocos, detalheBloco, editaBloco, novoBloco

urlpatterns = [
    path('novo/', novoBloco.as_view(), name='novoBloco'),
    path('', listaBlocos.as_view(), name='ListaBloco'),
    path('produto/<int:pk>/', detalheBloco.as_view(), name='DetalheBloco'),
    path('produto/<int:pk>/editar/', editaBloco.as_view(), name='EditaBloco'),
]