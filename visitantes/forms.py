from django import forms
from visitantes.models import Visitante

class VisitanteForm(forms.ModelForm):
    
    class Meta:
        model = Visitante
        fields = (
            "nome_completo", "cpf", "email_morador", 
            "data_nascimento", "numero_da_casa", "morador", "visitar",
        )

        error_messages = {
            "nome_completo":{
                "required": "Nome completo do visitante é obrigatório!"
            },
            "cpf":{
                "required": "CPF é obrigatório para fins de identificação!"
            },
            "email_morador":{
                "required": "E-mail do visitante é obrigatório para fins de contato, caso haja algum problema!",
                "invalid": "Insira um email válido! Ex: adalovelace@gmail.com"
            },
            "data_nascimento":{
                "required": "Data de nascimento é obrigatório!",
                "invalid": "Por favor, insira em um formato válido (DD/MM/AAAA)"
            },
            "numero_da_casa":{
                "required": "Número da casa é obrigatório para fins de identificação!"
            },
            "visitar":{
                "required": "Nome do morador que deseja visitar é obrigatório para fins de segurança!"
            }
            

            
        }


        

        #NESSE FIELDS, ANTES ESTAVA DIZENDO "__ALL__", ISSO SIGNIFICA QUE IRÁ APARECER NO FORMULÁRIO DE UM NOVO VISITANTE PARA
        #PREENCHER, TODAS AS INFORMAÇÕES QUE NÓS CADASTRAMOS DESDE NOME A HORA DE SAÍDA.

        #PORÉM HORA DE SAÍDA E OUTRAS INFORMAÇÕES, NÃO SÃO NECESSÁRIAS NA PRIMEIRA VEZ, AFINAL SÓ SERÃO 
        #PRENCHIDAS MEDIANTE A AUTORIZAÇÃO DO MORADOR, POR ISSO VÃO SER PRENCHIDAS EM UMA SEGUNDA VEZ
        #POR ISSO ALTERAMOS O "FIELDS" PARA MOSTRAR SOMENTE OQUE PODE SER PREENCHIDO NA PRIMEIRA VEZ