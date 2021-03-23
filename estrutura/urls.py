from django.contrib import admin
from django.urls import path
from usuarios.views import index 

from visitantes.views import (
    registrar_visitante, informacoes_visitante
)

urlpatterns = [
    path("admin/", admin.site.urls),

    path(
    	"", #o endereço vazio para entrar no dashboard, é somente o numero do sevidor
    	index, #chamando a função index
    	name="index"
    ),

    path(
        "registrar-visitante/", #endereço para ver a funcionalidade registrar visitante
        registrar_visitante, #chamando a função registrar_visitante que esta na views
        name= "registrar_visitante", #nomeando a função aqui 
    ),

    path (
        "visitantes/<int:id>/",  #esse aqui é o endereço para acessar essa funcionalidade ver informação
        informacoes_visitante, #chamando a função informacoes_visitante que esta na views
        name= "informacoes_visitante" #nomeando a função 
    )
]
