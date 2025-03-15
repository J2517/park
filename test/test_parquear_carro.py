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
        parqueadero = Parqueadero()
        control = ControlParqueadero(parqueadero)

        # Intentamos parquear un carro con un modelo inválido (string)
        resultado = control.parquear_carro("XYZ999", "Honda", "modelo_invalido")
        
        self.assertFalse(resultado)
        self.assertEqual(parqueadero.puestos_disponibles(), 20)
    
    def test_modelo_negativo(self):
        parqueadero = Parqueadero()
        control = ControlParqueadero(parqueadero)

        # Intentamos parquear un carro con modelo negativo
        resultado = control.parquear_carro("XYZ999", "Honda", -2020)

        self.assertFalse(resultado)
        self.assertEqual(parqueadero.puestos_disponibles(), 20)  

    def test_ingresar_modelo_futuro(self):
        parqueadero = Parqueadero()
        control = ControlParqueadero(parqueadero)

        # Suponiendo que estamos en 2025, intentamos parquear un carro modelo 2030
        resultado = control.parquear_carro("XYZ999", "Toyota", 2030)

        self.assertFalse(resultado)
        self.assertEqual(parqueadero.puestos_disponibles(), 20)

    def test_parqueo_placa_invalida(self):
        parqueadero = Parqueadero()
        control = ControlParqueadero(parqueadero)

        resultado = control.parquear_carro("", "Toyota", 2022)  # Placa vacía
        self.assertFalse(resultado)

        resultado = control.parquear_carro("12345", "Toyota", 2022)  # Placa sin formato válido
        self.assertFalse(resultado)

    def test_parqueo_marca_vacia(self):
        parqueadero = Parqueadero()
        control = ControlParqueadero(parqueadero)

        resultado = control.parquear_carro("ABC123", "", 2022)  # Marca vacía
        self.assertFalse(resultado)
