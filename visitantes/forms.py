from django import forms
from visitantes.models import visitante

class VisitanteForm(forms.ModelForm):
    
    class Meta:
        model = visitante
        fields = (
            "nome_completo", "cpf", "email_morador", 
            "data_nascimento", "numero_da_casa", "morador"
        )