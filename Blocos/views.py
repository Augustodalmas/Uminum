from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from Blocos.models import Produto
from Blocos.form import formProduto
from django.urls import reverse_lazy
from django.http import HttpResponseBadRequest
from django.db.models import Q
from django_filters.views import FilterView
from .filters import ProdutoFilter

class listaBlocos(ListView):
    model = Produto
    template_name = 'lista_bloco.html'
    context_object_name = 'produto'

    def get_queryset(self):
        queryset = Produto.objects.all()
        self.filterset = ProdutoFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context


class novoBloco(CreateView):
    model = Produto
    form_class = formProduto
    template_name = 'novo_bloco.html'
    success_url = '/'


class detalheBloco(DetailView):
    model = Produto
    template_name = 'detalha_job.html'
    context_object_name = 'object'
    pk_url_kwarg = 'pk' #Utilizar pk pois 'pk' é o valor do ID do objeto


class editaBloco(UpdateView):
    model = Produto
    template_name = 'edita_bloco.html'
    form_class = formProduto

    def get_success_url(self):
        return reverse_lazy('DetalheBloco', kwargs={'pk': self.object.pk})