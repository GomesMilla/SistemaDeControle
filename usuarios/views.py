from django.shortcuts import render
from django.http import HttpResponse
#Mostrar no navegador o que é que foi escolhido
#def index(request):
#return HttpResponse("Ola mundo! Camila Adriana")
#Aqui retornou o que eu queria que a mensagem do Httpresponse ola mundo + meu nome

def index(request):

	context = {
		"nome_pagina": "Início da dashboard",
	}
	return render(request, "index.html", context)




