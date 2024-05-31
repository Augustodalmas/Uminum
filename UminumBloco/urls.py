"""
URL configuration for UminumBloco project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Blocos.views import  listaBlocos, detalheBloco, editaBloco, novoBloco
from jobs.views import listaJobs, detalheJob, editaJob, criaJob
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('novo/', novoBloco.as_view(), name='novoBloco'),
    path('novo_job/', criaJob.as_view(), name='novoJob'),
    path('', listaBlocos.as_view(), name='ListaBloco'),
    path('Jobs', listaJobs.as_view(), name='ListaJob'),
    path('produto/<int:pk>/', detalheBloco.as_view(), name='DetalheBloco'),
    path('job/<int:pk>/', detalheJob.as_view(), name='DetalheJob'),
    path('produto/<int:pk>/editar/', editaBloco.as_view(), name='EditaBloco'),
    path('job/<int:pk>/editar/', editaJob.as_view(), name='EditaJob'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)