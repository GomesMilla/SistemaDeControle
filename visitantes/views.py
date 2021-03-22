from django.shortcuts import render
from visitantes.forms import VisitanteForm
#nome do arquivo + nome da pasta

def registrar_visitante(request):
    form = VisitanteForm()

    if request.method== "POST":
        #O METODO POST É UTILIZADO SEMPRE QUE PRECISAMOS MANDAR INFORMAÇÕES PARA O SERVIDOR E NESSE CASO
        #PRECISAMOS ENVIAR AS INFORMAÇÕES DO NOVO VISITANTE CADASTRADO
    
    context = {
        "nome_pagina": "Registrar visitante",
        "form": form,
    }
    
    return render (request, "registrar_visitante.html", context)


