import django_filters
from .models import Jobs

class JobsFilter(django_filters.FilterSet):
    class Meta:
        model = Jobs
        fields = {
            'job': ['exact'],
            'Status_Engenharia': ['exact'],
            'Status_Projeto': ['exact'],
            'Responsavel': ['exact'],
            'Corrigido': ['exact'],
            'Data_Alojamento': ['exact'],
            'Data_Detalhamento': ['exact'],
        }
