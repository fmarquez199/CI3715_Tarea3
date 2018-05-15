#!/usr/bin/python3
"""
Titulo: seguridad.py

Descripcion: Implementacion de la clase Seguridad.

Autores: Andre Cocuera     	12-10660
         Francisco Marquez  12-11163

Equipo: Null Pointer Exception

Fecha:15/05/2018.
"""

"""
La clase Seguridad representa un objeto para la validacion de usuarios en una
aplicacion web.

Los metodos son de inicializacion (init), registrarUsuario e ingresarUsuario.
"""
import re

class Seguridad():
	# Metodo de inicializacion de la clase Seguridad. Fija el valor de los
	# atributos:
	# 	1. users en {} (el diccionario vacio).
	#	2. email_format en la expresion regular correspondiente aun email
	#	aceptado por el RFC 822.
	#	3. no_alfan en la expresion regular para detectar un caracter no
	#	alfanumerico.
	#	4. letras_3 en la expresion regular para detectar 3 letras.
	#	5. mayus_01 en la expresion regular para detectar una mayuscula.
	#	6. minus_01 en la expresion regular para detectar una minuscula.
	#	7. digit_01 en la expresion regular para detectar un digito.
	def __init__(self):
		self.users = {}
		self.email_format = re.compile(
			'([a-zA-Z0-9]+)@([a-zA-Z0-9]+)(\.)([a-zA-Z0-9]+)')
		self.no_alfan = re.compile('.*[^a-zA-Z0-9]+.*')
		self.letras_3 = re.compile('.*[a-zA-Z].*[a-zA-Z].*[a-zA-Z].*')
		self.mayus_01 = re.compile('.*[A-Z].*')
		self.minus_01 = re.compile('.*[a-z].*')
		self.digit_01 = re.compile('.*[0-9].*')

	# Metodo que toma tres string, apuntados por email, pswd1 y pswd2 y retorna
	# True si y solo si:
	#	1. email es una direccion de correo electronico que cumple con el
	#	   estandar RFC 822.
	#	2. email no existe en el atributo users.
	#	3. La longitud de pswd1 esta entre 8 y 16, ambos inclusive.
	#	4. pswd1 solo posee caracteres alfanumericos.
	#	5. pswd1 posee al menos 3 caracteres alfabeticos.
	#	6. pswd1 posee al menos un caracter alfabetico en Upper Case.
	#	7. pswd1 posee al menos un caracter alfabetico en Lower Case.
	#	8. pswd1 posee al menos un digito.
	#	9. pswd1 y pswd2 son iguales.
	# En caso contrario, se retorna False y se muestran mensajes de error
	# correspondientes a las condiciones violadas.
	def registrarUsuario(self, email: str, pswd1: str, pswd2: str) -> bool:
		id_email = self.email_format.match(email) != None
		nw_email = email not in self.users
		plen_min = len(pswd1) > 7
		plen_max = len(pswd1) < 17
		pnoalfan = self.no_alfan.match(pswd1) == None
		p3letras = self.letras_3.match(pswd1) != None
		pmayus01 = self.mayus_01.match(pswd1) != None
		pminus01 = self.minus_01.match(pswd1) != None
		pdigit01 = self.digit_01.match(pswd1) != None
		password = plen_min and plen_max and pnoalfan and p3letras and pmayus01
		password = password and pminus01 and pdigit01
		samepass = pswd1 == pswd2
		try:
			assert(id_email)
			assert(nw_email)
			assert(password)
			assert(samepass)
			self.users[email] = pswd1
		except:
			if not id_email:
				print("Correo electrónico inválido")
			if not nw_email:
				print("Correo electrónico ya existe")
			if not password:
				print("Clave inválida")
			if not plen_min:
				print("La clave tiene menos de 8 caracteres")
			if not plen_max:
				print("La clave tiene mas de 16 caracteres")
			if not pnoalfan:
				print("La clave tiene algun caracter especial: !,*,...")
			if not p3letras:
				print("La clave tiene menos de 3 letras")
			if not pmayus01:
				print("La clave no tiene mayusculas")
			if not pminus01:
				print("La clave no tiene minusculas")
			if not pdigit01:
				print("La clave no tiene numeros")
			if not samepass:
				print("Las claves no coinciden")
		finally:
			return id_email and nw_email and password and samepass

	# Metodo que toma dos strings apuntados por email y pswd y devuelve True y 
	# muestra el mensaje "Usuario aceptado" si y solo si:
	#	1. email se encuentra en el atributo users.
	#	2. pswd es igual al dato asociado a la clave email del atributo users.
	# Caso contrario, se retorna False y le da mensajes al usuario
	# correspondientes al error ocurrido.
	def ingresarUsuario(self, email: str, pswd: str) -> bool:
		valid_email = email in self.users
		if valid_email:
			valid_psswd = self.users[email] == pswd
		try:
			assert(valid_email and valid_psswd)
			print("Usuario aceptado")
		except:
			if not valid_email:
				print("Usuario inválido")
			if valid_email and not valid_psswd:
				print("Clave inválida")
		finally:
			return valid_email and valid_psswd