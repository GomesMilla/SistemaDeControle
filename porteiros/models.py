from django.db import models

class Porteiro(models.Model): 
#dois pontos quando abrir uma classe ou uma função
#criando classe porteiro com seguintes atributos:
	

	usuario = models.OneToOneField(
		"usuarios.usuario",
		verbose_name = "Usuario",
		on_delete = models.PROTECT
		#models.PROTECT impede que seja excluido um usuario do sistema
	)

	
	nome_completo = models.CharField(
		verbose_name = "Nome completo",
		max_length = 194,
	)

	cpf = models.CharField(
		verbose_name = "CPF",
		max_length = 11,
	)

	telefone = models.CharField(
		verbose_name = "Telefone para contato",
		max_length = 11,
	)
	data_nascimento = models.DateField(
		verbose_name = "Data de aniversario",
		auto_now = False,
		auto_now_add = False,
	)

	class Meta():
		verbose_name = "Porteiro"
		verbose_name_plural = "Porteiros"	
		db_table = "porteiro"
		#Sem virgula, vai dar erra, vai entender que esta criando uma tupla
		#aqui é banco
	def __str__(self):
		return self.nome_completo
	

# Create your models here.
