from django.db import models

class Formato(models.Model):
    id = models.AutoField(primary_key=True)
    formato = models.CharField(max_length=2, blank=False, null=False)

    def __str__(self):
        return str(self.formato)
    

class Serie(models.Model):
    id = models.AutoField(primary_key=True)
    Serie = models.CharField(max_length=1, blank=False, null=False)

    def __str__(self):
        return str(self.Serie)
    

class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    Job = models.CharField(max_length=4 ,blank=False, null=False)
    Serie = models.ForeignKey(Serie, on_delete=models.PROTECT, related_name='serieBlocos')
    qtdPontos = models.IntegerField(blank=False, null=False)
    qtdResistencia = models.IntegerField(blank=False, null=False)
    formatoBloco = models.ForeignKey(Formato, on_delete=models.PROTECT, related_name='formasBlocos')
    entreCentrosX = models.IntegerField(blank=False, null=False)
    entreCentrosY = models.IntegerField(blank=False, null=False)
    pdf = models.FileField(upload_to='', default='ola.pdf', blank=False, null=False)
    obs = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self) -> str:
        return self.Job