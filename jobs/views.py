from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from jobs.models import Jobs
from jobs.filters import JobsFilter
from django.urls import reverse_lazy
from jobs.form import formJob, JobForm, JobUpdateForm

class listaJobs(ListView):
    model = Jobs
    template_name = 'lista_jobs.html'
    context_object_name = 'job'

    def get_queryset(self):
        # Obtém todos os objetos de Jobs e os ordena por algum campo
        queryset = super().get_queryset().order_by('job')
        self.filterset = JobsFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context


class criaJob(CreateView):
    model = Jobs
    template_name = 'cria_jobs.html'
    form_class = JobForm
    success_url = reverse_lazy("ListaJob")


class detalheJob(DetailView):
    model = Jobs
    template_name = 'detalha_job.html'
    context_object_name = 'object'
    pk_url_kwarg = 'pk' #Utilizar pk pois 'pk' é o valor do ID do objeto


class editaJob(UpdateView):
    model = Jobs
    template_name = 'edita_job.html'
    form_class = JobUpdateForm

    def get_object(self, queryset=None):
        # Obtém o objeto Job que será editado
        return Jobs.objects.get(pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse_lazy('DetalheJob', kwargs={'pk': self.object.pk})