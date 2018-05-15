#!/usr/bin/python3
"""
Titulo: seguridad.py

Descripcion: Implementacion de la clase Seguridad.

Autores: Andre Cocuera     	12-10660
         Francisco Marquez  12-11163

Equipo: Null Pointer Exception

Fecha:11/05/2018.
"""

"""
La clase Seguridad representa un objeto para la validacion de usuarios en una
aplicacion web.

Los metodos son de inicializacion (init), registrarUsuario e ingresarUsuario.
"""

class Seguridad():
	def __init__(self):
		pass

	def registrarUsuario(self, email: str, pswd1: str, pswd2: str) -> bool:
		id_email = self.email_format.match(email) != None
		plen_min = len(pswd1) > 7
		password = plen_min
		try:
			assert(id_email)
			assert(password)
		except:
			if not id_email:
				print("Correo electrónico inválido")
			if not password:
				print("Clave inválida")
			if not plen_min:
				print("La clave tiene menos de 8 caracteres")
		finally:
			return id_email and password