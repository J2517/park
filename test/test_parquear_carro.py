import unittest
from control import ControlParqueadero
from datos import Parqueadero

class TestParquearCarro(unittest.TestCase):

    def test_parqueo_exitoso(self):
        parqueadero = Parqueadero()
        control = ControlParqueadero(parqueadero)
        
        parqueo = control.parquear_carro("ABC123", "Chevrolet", 2015) 
        
        self.assertTrue(parqueo)  # Debe devolver True si se parqueó correctamente
        self.assertEqual(parqueadero.puestos_disponibles(), 19)  # Se reduce en 1 el número de puestos

    def test_parqueo_sin_espacio(self):
        parqueadero = Parqueadero()
        control = ControlParqueadero(parqueadero)

        # Llenamos el parqueadero con 20 carros
        for i in range(20):
            control.parquear_carro(f"ABC{i:03}", "nn", 2015)

        # Intentamos parquear un carro más (debe fallar)
        resultado = control.parquear_carro("XYZ999", "Honda", 2020)
        
        self.assertFalse(resultado)  # Debe retornar Fals
        self.assertEqual(parqueadero.puestos_disponibles(), 0)

    def test_parqueo_repetido(self):
        parqueadero = Parqueadero()
        control = ControlParqueadero(parqueadero)
        
        control.parquear_carro("ABC123", "Chevrolet", 2015) 
        parqueo_repetido = control.parquear_carro("ABC123", "Chevrolet", 2015)
        
        self.assertFalse(parqueo_repetido)
        self.assertEqual(parqueadero.puestos_disponibles(), 19)  # Se reduce en 1 el número de puestos
    
    def test_modelo_invalido(self):
        """ Intentar parquear un carro con un modelo inválido (string en vez de int) """
        parqueadero = Parqueadero()
        control = ControlParqueadero(parqueadero)

        # Intentamos parquear un carro con un modelo inválido (string)
        resultado = control.parquear_carro("XYZ999", "Honda", "modelo_invalido")

        
        self.assertTrue(resultado)
    
    def test_modelo_negativo(self):
        """ Intentar parquear un carro con un modelo negativo """
        parqueadero = Parqueadero()
        control = ControlParqueadero(parqueadero)

        # Intentamos parquear un carro con modelo negativo
        resultado = control.parquear_carro("XYZ999", "Honda", -2020)

        # Como no hay validación, el carro se agrega con el modelo negativo
        self.assertTrue(resultado)  # Debe retornar True (el carro se parquea)

