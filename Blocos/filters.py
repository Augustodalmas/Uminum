import django_filters
from .models import Produto

class ProdutoFilter(django_filters.FilterSet):
    class Meta:
        model = Produto
        fields = {
            'Serie': ['exact'],
            'qtdPontos': ['exact'],
            'qtdResistencia': ['exact'],
            'formatoBloco__formato': ['exact'],
            'entreCentrosX': ['exact'],
            'entreCentrosY': ['exact'],
            'Job': ['exact'],
        }
