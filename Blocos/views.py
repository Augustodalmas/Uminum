from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from Blocos.models import Produto
from Blocos.form import formProduto
from django.urls import reverse_lazy
from django.http import HttpResponseBadRequest
from django.db.models import Q

class listaBlocos(ListView):
    model = Produto
    template_name = 'lista_bloco.html'
    context_object_name = 'produto'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('Job')
        search_term = self.request.GET.get('search')
        filter_by = self.request.GET.get('filter_by')

        if search_term and filter_by:
            # Verifica qual campo o usuário deseja pesquisar e filtra o queryset
            if filter_by == 'entreCentrosX':
                queryset = queryset.filter(entreCentrosX__icontains=search_term)
            elif filter_by == 'entreCentrosY':
                queryset = queryset.filter(entreCentrosY__icontains=search_term)
            elif filter_by == 'formatoBloco':
                queryset = queryset.filter(formatoBloco__formato__icontains=search_term)
            elif filter_by == 'qtdPontos':
                queryset = queryset.filter(qtdPontos__icontains=search_term)
            elif filter_by == 'Job':
                queryset = queryset.filter(Job__icontains=search_term)

        return queryset


class novoBloco(CreateView):
    model = Produto
    form_class = formProduto
    template_name = 'novo_bloco.html'
    success_url = '/'


class detalheBloco(DetailView):
    model = Produto
    template_name = 'detalha_bloco.html'
    context_object_name = 'object'
    pk_url_kwarg = 'pk' #Utilizar pk pois 'pk' é o valor do ID do objeto


class editaBloco(UpdateView):
    model = Produto
    template_name = 'edita_bloco.html'
    form_class = formProduto

    def get_success_url(self):
        return reverse_lazy('DetalheBloco', kwargs={'pk': self.object.pk})