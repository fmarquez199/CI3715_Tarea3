#!/usr/bin/python3
"""
Titulo: casos_de_prueba.py

Descripcion: Implementacion de casos de prueba para la funcion clase Seguridad.
Los casos de prueba son, por orden de aplicacion:

    1.  test_Seguridad_existe: Verifica que exista la clase Seguridad.

    2.  test_Seguridad_existe_metodo_registrar: Verifica que exista el metodo
                                                registrarUsuario.

    3.  test_Seguridad_email_valido: Verifica que el id de correo sea valido
                                     segun el estandar RFC 822.

    4.  test_Seguridad_clave_long_ocho_min: Verifica que la clave tenga
                                            longitud mayor que 7.

    5.  test_Seguridad_clave_long_dieciseis_max: Verifica que la clave tenga
                                                 longitud menor que 17.

    6.  test_Seguridad_clave_solo_alfanumericos: Verifica que la clave no tenga
                                                 caracteres no alfanumericos.

    7.  test_Seguridad_clave_min_tres_letras: Verifica que la clave tenga al
                                              menos tres letras.

    8.  test_Seguridad_clave_min_una_mayuscula: Verifica que la clave tenga al
                                                menos una mayuscula.

    9.  test_Seguridad_9:

    10. test_Seguridad_10:

    11. test_Seguridad_11:

    12. test_Seguridad_12:

    13. test_Seguridad_13:

    14. test_Seguridad_14:

    15. test_Seguridad_15:

Autores: Andre Cocuera     	12-10660
         Francisco Marquez  12-11163

Equipo: Null Pointer Exception

Fecha: 15/05/2018.
"""

import unittest
from seguridad import Seguridad

class SeguridadTestCase(unittest.TestCase):

    #Verifica que exista la clase Seguridad.
    def test_Seguridad_existe(self) -> 'void':
        valid = Seguridad()
        self.assertNotEqual(valid, None)

    #Verifica que exista el metodo registrarUsuario.
    def test_Seguridad_existe_metodo_registrar(self) -> 'void':
        email = "usbid@usb.ve"
        pswd1 = "U581Dd3pRu384"
        pswd2 = "U581Dd3pRu384"
        valid = self.seguridad.registrarUsuario(email, pswd1, pswd2)
        self.assertNotEqual(valid, None)

    #Verifica que el id de correo sea valido segun el estandar RFC 822.
    def test_Seguridad_email_valido(self) -> 'void':
        email = "usbid!@usb.ve"
        pswd1 = "U581Dd3pRu384"
        pswd2 = "U581Dd3pRu384"
        valid = self.seguridad.registrarUsuario(email, pswd1, pswd2)
        self.assertEqual(valid, False)

    #Verifica que la clave tenga longitud mayor que 7.
    def test_Seguridad_clave_long_ocho_min(self) -> 'void':
        email = "usbid@usb.ve"
        pswd1 = "U5d3"
        pswd2 = "U5d3"
        valid = self.seguridad.registrarUsuario(email, pswd1, pswd2)
        self.assertEqual(valid, False)

    #Verifica que la clave tenga longitud menor que 17.
    def test_Seguridad_clave_long_dieciseis_max(self) -> 'void':
        email = "usbid@usb.ve"
        pswd1 = "U581Dd3pRu384largo"
        pswd2 = "U581Dd3pRu384largo"
        valid = self.seguridad.registrarUsuario(email, pswd1, pswd2)
        self.assertEqual(valid, False)

    #Verifica que la clave no tenga caracteres no alfanumericos.
    def test_Seguridad_clave_solo_alfanumericos(self) -> 'void':
        email = "usbid@usb.ve"
        pswd1 = "U581Dd3pRu384!"
        pswd2 = "U581Dd3pRu384!"
        valid = self.seguridad.registrarUsuario(email, pswd1, pswd2)
        self.assertEqual(valid, False)

    #Verifica que la clave tenga al menos tres letras.
    def test_Seguridad_clave_min_tres_letras(self) -> 'void':
        email = "usbid@usb.ve"
        pswd1 = "1211163121o66o"
        pswd2 = "1211163121o66o"
        valid = self.seguridad.registrarUsuario(email, pswd1, pswd2)
        self.assertEqual(valid, False)

    #Verifica que la clave tenga al menos una mayuscula.
    def test_Seguridad_clave_min_una_mayuscula(self) -> 'void':
        email = "usbid@usb.ve"
        pswd1 = "u581dd3pru384"
        pswd2 = "u581dd3pru384"
        valid = self.seguridad.registrarUsuario(email, pswd1, pswd2)
        self.assertEqual(valid, False)

if __name__ == '__main__':
	unittest.main()