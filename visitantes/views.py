from django.contrib import messages
from django.shortcuts import(
    render, redirect, get_object_or_404
)
from visitantes.models import Visitante
from visitantes.forms import VisitanteForm
#nome do arquivo + nome da pasta

def registrar_visitante(request):
    
    form = VisitanteForm()

    if request.method == "POST":
        form = VisitanteForm(request.POST)

        if form.is_valid():
            visitante = form.save(commit = False)

            visitante.registrado_por = request.user.porteiro
            visitante.save()

            messages.success(
                request, 
                "Visitante registrado com sucesso!"
            )

            return redirect("index")
            #Estou importando o pacote sucess dentro da biblioteca "messages" e estou enviando para o porteiro
            # a mensagem "visitante registrado com sucesso" 


    context = {
        "nome_pagina": "Registrar visitante",
        "form": form,
    }
    
    return render (request, "registrar_visitante.html", context)

def informacoes_visitante(request, id):

    visitante = get_object_or_404(
        Visitante,
        id = id
    )

    context = {
        "nome_pagina": "Informações do visitante",
        "visitante": visitante,

    }

    return render (request, "informacoes_visitante.html", context)


#O METODO POST É UTILIZADO SEMPRE QUE PRECISAMOS MANDAR INFORMAÇÕES PARA O SERVIDOR E NESSE CASO
#PRECISAMOS ENVIAR AS INFORMAÇÕES DO NOVO VISITANTE CADASTRADO


#O MÉTODO COMMIT== FALSE SIGNIFICA QUE O PORTEIRO VAI SER AUTOMATICAMENTE PREENCHIDO A PARTIR DO PORTEIRO REGISTARDO NAQUELE MOMENTO
#NESSE CASO, ELE PEGA O PORTEIRO LOGADO, COLOCA ELE AUTOMATICAMENTE COMO RESPONSÁVEL PELO VISITANTE E SALVA NO BANCO DE DADOS
#JÁ O RETURN INDEX SIGINIFICA QUE AS INFORMAÇÕES DO VISITANTE DEVEM ESTAR SENDO EXIBIDAS AUTOMATICAMENTE NA PARTE DA  DASHBOARD