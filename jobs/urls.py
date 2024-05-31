from django.urls import path
from jobs.views import criaJob, listaJobs, detalheJob, editaJob

urlpatterns = [
    path('novo_job/', criaJob.as_view(), name='novoJob'),
    path('', listaJobs.as_view(), name='ListaJob'),
    path('job/<int:pk>/', detalheJob.as_view(), name='DetalheJob'),
    path('job/<int:pk>/editar/', editaJob.as_view(), name='EditaJob'),
]