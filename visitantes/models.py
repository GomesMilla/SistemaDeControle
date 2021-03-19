from django.db import models

#ele vai pedir: cpf, 
# nome completo, 
# data de nascimento, 
# placa do carro(opcional), 
# numero da casa que deseja visitar, 
# os horarios de chagada e saida 
# a autorização de entrada 
# o nome do morador que autorizou a entrada do visitante 
# o nome do porteiro que foi registrado o registro

	class visitante(models.Model):


		nome_completo = models.CharField(
		verbose_name = "Nome completo:",
		max_length = 194,
		)
		data_nascimento = models.DateField(
		verbose_name = "Data de aniversario:",
		auto_now = False,
		auto_now_add = False,
		)
		placa_do_carro = models.CharField(

			) 
		numero_da_casa = models.CharField(
			verbose_name = "Numero da casa que deseja visitar:"


		)
		
		hora_de_entrada_e_saida = models.DateField(
			verbose_name = "Hora da entrada e saida do vistante:"
		)

		morador = models.CharField(
			verbose_name = "Nome do morador que permitiu a entrada: "
			max_length = 194
		)
		email_morador = models.EmailField(           
			verbose_name="E-mail do morador:",
			max_length=194,                  
			unique=True,  
		)
		porteiro = models.CharField(
			verbose_name = "Porteiro responsável pelo registro:  "
			max_length = 194
		)
