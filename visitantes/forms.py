from django import forms
from visitantes.models import visitante

class VisitanteForm(forms.ModelForm):
    
    class Meta:
        model = visitante
        fields = "__all__"