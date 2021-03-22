from django.shortcuts import render
from visitantes.models import visitante
#Mostrar no navegador o que é que foi escolhido
#def index(request):
#return HttpResponse("Ola mundo! Camila Adriana")
#Aqui retornou o que eu queria que a mensagem do Httpresponse ola mundo + meu nome

def index(request):
	
	todos_visitantes = visitante.objects.all 

	context = {
		"nome_pagina": "Início da dashboard",
		"todos_visitantes": todos_visitantes
	}
	return render(request, "index.html", context)




