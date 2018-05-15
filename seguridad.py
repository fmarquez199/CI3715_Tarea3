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

class Seguridad():
	def __init__(self):
		self.users = {}
		self.email_format = re.compile(
			'([a-zA-Z0-9]+)@([a-zA-Z0-9]+)(\.)([a-zA-Z0-9]+)')
		self.no_alfan = re.compile('.*[^a-zA-Z0-9]+.*')
		self.letras_3 = re.compile('.*[a-zA-Z].*[a-zA-Z].*[a-zA-Z].*')
		self.mayus_01 = re.compile('.*[A-Z].*')

	def registrarUsuario(self, email: str, pswd1: str, pswd2: str) -> bool:
		id_email = self.email_format.match(email) != None
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
			assert(password)
			assert(samepass)
			self.users[email] = pswd1
		except:
			if not id_email:
				print("Correo electrónico inválido")
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
			return id_email and password and samepass