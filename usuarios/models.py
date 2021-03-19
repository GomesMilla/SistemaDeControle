#from django.db import models
from django.db import models
from django.contrib.auth.models import(   #quando tiver escrito deriva subtitua por sub-class
	 BaseUserManager,                        
	 AbstractBaseUser,                        
	 PermissionsMixin
)

class UsuarioManager(BaseUserManager):
	#O usuario Manager ele deriva da classe BaseUSerManager.
	def create_user(self, email, password = None):
		usuario = self.model(
			email = self.normalize_email(email)
			)
		#os metodos normalize email são usados e muito importante porque é ele quem evita que o email seje salvo com letras maiusculas e caracteres especiais!
		usuario.is_active = True
		usuario.is_superuser = False
		usuario.is_staff = False

		if password:
			usuario.set_password(password)

		usuario.save()
		return usuario

	def create_superuser(self, email, password):
		usuario = self.create_user(
		email = self.normalize_email(email),
		password = password
		)


		usuario.is_staff = True
		usuario.is_active = True
		usuario.is_superuser = True

		usuario.set_password(password)


		usuario.save()

		return usuario

class Usuario(AbstractBaseUser, PermissionsMixin): #criação da classe usuario
	#A classe usuario ele deriva da classe abstractBAeUser e PermissionsMixin, ou seja ele tem 
	#atributos dessas duas classses.
	
	email = models.EmailField(           
		verbose_name="E-mail do usuario",
		max_length=194,                  
		unique=True,                     
    #criação dos atributos da classe usuario
    #verbose_name recebe o email
    #max_lenght diz que o tamanho maximo  do email é 194.  
    #Ao usar 'unique' afirmo para o django que não pode existir dois usuarios com o mesmo email, ou seja, ele(Django) valida se existe aquele email no banco de dados dele.                       
    ) 

	is_active = models.BooleanField(     
		verbose_name= "Usuario esta ativo",
		default = True,                      
    )
    #Aqui também um atributo que diz o seguinte que quando ele cria uma
    #conta o usuario agora esta ativo, porque eu informei "TRUE"

	is_staff = models.BooleanField(
		verbose_name = "usuario é da equipe de desenvolvimento", 
		default = False,                                        
	)   
    #outro atributo, mas diferente do segundo,ele vai receber falso porque nem todos 
    #vão fazer parte da equipe de desenvolvimento.

	is_superuser = models.BooleanField(                        
		verbose_name = "Usuario é super usuario",              
		default = False,                                       
    )
    # É o mesmo caso da equipe de desenvolvimento, nem todos vão ser super usuarios e é por isso que ele recebe falso logo ao cadastrar
    ##Acredito que para ele receber o TRUE ele deve ser validado lá no ADMIN. Para ser reconhecido como administrador 
    
    
	USERNAME_FIELD = "email" # ele  é para validação por meio do email  

	objects = UsuarioManager()  

    
    
    
	
	class Meta:
		verbose_name = "Usuario"
		verbose_name_plural = "usuarios" #literalmente o plural do nosso verbose_name
		db_table = "usuario" 

	#esse db_table modifica o nome do banco de dados que por padrão seria o nome do projeto_o nome da classe principal do model, ou seja, no meu caso ia chamar "tiago_usuario"
    #mas como eu alterei o banco de dados agora vai ser chamar "usuario" como foi declarado nessa variavel da frente.
  	
	def __str__(self):        
		return self.email 
  	#Retornar o email que o usuario entrou quando precisar retornar os emails de todos os cadastrados, assim fica mais facil indentificar
  	#porque se fosse pedir para retornar somente o objeto, iria aparecer somente o numero do cadastro





# Create your models here.

#from django.contrib.auth.models import= Importação para personalizar 
#a criação do usuario diferente do nome e senha e sim por meio de 
#email e senha. É tipo uma biblioteca
#Atributo email 
#

##########################################################################################
###  PELO QUE EU ENTENDI ESSE É A CRIAÇÃO DO USUARIO COMUM/ MORADORES DO PRÉDIO        ###
##########################################################################################

# Create your models here.
