from django.db import models



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
		cpf = models.CharField(
		verbose_name = "Número do CPF:",
		max_length = 11,
		)
		placa_do_carro = models.CharField(
		verbose_name = "Placa do veículo:",
		max_length = 7,
		blank=True,
		null=True
		#PERMITE QUE ESSA INFORMAÇÃO RECEBA BRANCO OU VAZIO, CASO O VISITANTE NÃO TENHA CARRO!
		) 
		
		numero_da_casa = models.PositiveSmallIntegerField(
		verbose_name = "Numero da casa que deseja visitar:"
		#POSITIVESMALLINTEGERFILED SIGNIFICA QUE SÓ RECEBE NÚMERO POSITIVO E COMO CASA E APARTAMENTO
		#SÓ EXISTE COM NÚMEROS POSITIVOS.
		)
		
		hora_de_entrada = models.DateTimeField(
		verbose_name = "Horario da entrada do visitante:",
		auto_now_add=True,
		#AQUI JÁ RECEBE TRUE NO AUTO NOW, VISTO QUE É A HORA DE ENTRADA DO VISITANTE NO PRÉDIO, POR ISSO É CONTRABILIZADA NO MESMO INSTANTE
		)
		hora_da_saida = models.DateTimeField(
		verbose_name = "Horario de saída do visitante:",
		auto_now= False,
		blank=True,
		null=True,
		#aqui a data de saida pode receber nada porque isso vai ser algo que vai ser contabilizado
		#pela segunda vez, quando ele sair, por isso na hora da entrada e nulo
		)
		morador = models.CharField(
		verbose_name = "Nome do morador que permitiu a entrada: ",
		max_length = 194,
		blank=True,
		)
		email_morador = models.EmailField(           
		verbose_name="E-mail do visitante:",
		max_length=194,                  
		unique=True,  
		)
					
		horario_altorizacao = models.DateTimeField(
		verbose_name="Horario da autorização da entrada do visitante:",
		auto_now= False,
		blank=True,
		null= True,
		#AQUI O AUTO NOW RECEBE FALSO PORQUE NÃO É PARA COMPLETAR A HORA DA AUTORIZAÇÃO ASSIM QUE ELE FOR
		#CADASTRADO, ELE PODE NEM SER AUTORIZADO OU DEMORAR, POR ISSO ELE RECEBE FALSO, ELE SÓ VAI SER AUTORIZADO 
		#EM UMA SEGUNDA VEZ. BLANK E NULL SIGNIFICA QUE ESSA INFORMAÇÃO DE HORA DE AUTORIZAÇÃO PODE FICAR VAZIA
		#NO PRIMEIRO MOMENTO ATÉ O MORADOR PERMITIR A ENTRADA. É A MESMA LÓGICA DO AUTO NOW, SÓ RETORNA COMPLETO
		#QUANDO É PERMITIDO EM UM SEGUNDO MOMENTO
		)
		registrado_por = models.ForeignKey(
		"porteiros.Porteiro",
		verbose_name = "Porteiro responsável:",
		on_delete= models.PROTECT
		)

		class Meta:
			verbose_name = "Visitante"
			verbose_name_plural="Visitantes"
			db_table="Visitante"

		def __str__(self):
			return self.nome_completo

		