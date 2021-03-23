from django import forms
from visitantes.models import visitante

class VisitanteForm(forms.ModelForm):
    
    class Meta:
        model = visitante
        fields = (
            "nome_completo", "cpf", "email_morador", 
            "data_nascimento", "numero_da_casa", "morador"
        )

        #NESSE FIELDS, ANTES ESTAVA DIZENDO "__ALL__", ISSO SIGNIFICA QUE IRÁ APARECER NO FORMULÁRIO DE UM NOVO VISITANTE PARA
        #PREENCHER, TODAS AS INFORMAÇÕES QUE NÓS CADASTRAMOS DESDE NOME A HORA DE SAÍDA.

        #PORÉM HORA DE SAÍDA E OUTRAS INFORMAÇÕES, NÃO SÃO NECESSÁRIAS NA PRIMEIRA VEZ, AFINAL SÓ SERÃO 
        #PRENCHIDAS MEDIANTE A AUTORIZAÇÃO DO MORADOR, POR ISSO VÃO SER PRENCHIDAS EM UMA SEGUNDA VEZ
        #POR ISSO ALTERAMOS O "FIELDS" PARA MOSTRAR SOMENTE OQUE PODE SER PREENCHIDO NA PRIMEIRA VEZ