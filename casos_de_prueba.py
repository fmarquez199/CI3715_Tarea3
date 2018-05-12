#!/usr/bin/python3
"""
Titulo: casos_de_prueba.py

Descripcion: Implementacion de casos de prueba para la funcion clase Seguridad.
Los casos de prueba son, por orden de aplicacion:

    1.  test_Seguridad_1: Verifica que exista la clase Seguridad.

    2.  test_Seguridad_2:

    3.  test_Seguridad_3:

    4.  test_Seguridad_4:

    5.  test_Seguridad_5:

    6.  test_Seguridad_6:

    7.  test_Seguridad_7:

    8.  test_Seguridad_8:

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

Fecha: 11/05/2018.
"""

import unittest
from seguridad import Seguridad

class SeguridadTestCase(unittest.TestCase):

    #Verifica que exista la clase Seguridad.
    def test_Seguridad_1(self) -> 'void':
        valid = Seguridad()
        self.assertNotEqual(valid, None)

if __name__ == '__main__':
	unittest.main()