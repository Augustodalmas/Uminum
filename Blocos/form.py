from django import forms
from Blocos.models import Produto

class formProduto(forms.ModelForm):
    class Meta():
        model = Produto
        fields = '__all__'

        Job = forms.IntegerField(required=False),

    def clean(self):
        cleaned_data = super().clean()
        Job = cleaned_data.get("Job")
        instance_id = self.instance.id if self.instance else None

        # Verificar se o item já existe
        if Produto.objects.filter(Job=Job).exclude(id=instance_id).exists():
            # Adicionar mensagem de erro ao campo
            self.add_error("Job", "O item já existe!")
        
        return cleaned_data
