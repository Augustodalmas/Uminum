from django.db import models

class Jobs(models.Model):
    ID = models.AutoField(primary_key=True)
    job = models.CharField(max_length=4, blank=False, null=False)
    
    ALOJAMENTO = 'Alojamento'
    DETALHAMENTO = 'Detalhamento'

    STATUS_CHOICES_ENG = [
        (ALOJAMENTO, 'Alojamento'),
        (DETALHAMENTO, 'Detalhamento'),
    ]

    Status_Engenharia = models.CharField(max_length=12, choices=STATUS_CHOICES_ENG)

    ANDAMENTO = 'Andamento'
    REVISAO = 'Revisão'
    REVISAO_SUPERIOR = 'Crestani'
    FINALIZADO = 'Finalizado'

    STATUS_CHOICES_PROJ = [
        (ANDAMENTO, 'Andamento'),
        (REVISAO, 'Revisao'),
        (REVISAO_SUPERIOR, 'Revisao_Crestani'),
        (FINALIZADO, 'Finalizado'),
    ]
    
    Status_Projeto = models.CharField(max_length=10, choices=STATUS_CHOICES_PROJ)

    AUGUSTO = 'Augusto'
    ALESSANDRO = 'Alessandro'
    GUILHERME = 'Guilherme'
    GUSTAVO = 'Gustavo'

    STATUS_CHOICES_RESP = [
        (AUGUSTO, 'Augusto'),
        (ALESSANDRO, 'Alessandro'),
        (GUILHERME, 'Guilherme'),
        (GUSTAVO, 'Gustavo'),
    ]

    Responsavel = models.CharField(max_length=12, blank=False, null=False, choices=STATUS_CHOICES_RESP)
    Corrigido = models.CharField(max_length=12, blank=False, null=False, choices=STATUS_CHOICES_RESP)
    Data_Alojamento = models.DateField(blank=True, null=True)
    Data_Detalhamento = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return self.job