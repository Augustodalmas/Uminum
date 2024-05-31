from django import forms
from jobs.models import Jobs
from django.forms import ModelForm

class formJob(forms.ModelForm):
    class Meta():
        model = Jobs
        fields = '__all__'

        Job = forms.IntegerField(required=False),

    def clean(self):
        cleaned_data = super().clean()
        Job = cleaned_data.get("job")
        instance_id = self.instance.ID if self.instance else None

        # Verificar se o item já existe
        if Jobs.objects.filter(job=Job).exclude(ID=instance_id).exists():
            # Adicionar mensagem de erro ao campo
            self.add_error("job", "O item já existe!")
        
        return cleaned_data


class DateInput(forms.DateInput):
    input_type = 'date'
    format = '%Y/%m/%d'

class JobForm(ModelForm):
    Data_Alojamento = forms.DateField(widget=DateInput(format='%Y/%m/%d'))
    Data_Detalhamento = forms.DateField(widget=DateInput(format='%Y/%m/%d'),required=False)


    class Meta:
        model = Jobs
        fields = "__all__"
        widgets = {
            'Data_Alojamento': forms.DateInput(),
            'Data_Detalhamento': forms.DateInput(),
        }

        
    def clean(self):
        cleaned_data = super().clean()
        data_detalhamento = cleaned_data.get('Data_Detalhamento')
        status_projeto = cleaned_data.get('Status_Projeto')

        # Verifica se o campo Status_Projeto está marcado como "Finalizado" e se Data_Detalhamento está vazio
        if status_projeto == 'Finalizado' and not data_detalhamento:
            self.add_error('Data_Detalhamento', 'Você não pode marcar como finalizado sem uma data de detalhamento.')

        return cleaned_data


class JobUpdateForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = "__all__"
        widgets = {
            'Data_Alojamento': forms.DateInput(),
            'Data_Detalhamento': forms.DateInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        data_detalhamento = cleaned_data.get('Data_Detalhamento')
        status_projeto = cleaned_data.get('Status_Projeto')

        if status_projeto == 'Finalizado' and not data_detalhamento:
            self.add_error('Data_Detalhamento', 'Você não pode marcar como finalizado sem uma data de detalhamento.')

        return cleaned_data