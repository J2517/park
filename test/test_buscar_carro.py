import unittest
from datos import Carro, Parqueadero

class TestBuscarCarro(unittest.TestCase):
    
    def test_buscar_carro_existente(self):
        parqueadero = Parqueadero()
        carro = Carro("ABC123", "Toyota", 2020)
        parqueadero.parquear_carro(carro)
        
        carro_encontrado = parqueadero.buscar_carro("ABC123")
        self.assertIsNotNone(carro_encontrado)
        self.assertEqual(carro_encontrado.placa, "ABC123")
    
    def test_buscar_carro_inexistente(self):
        parqueadero = Parqueadero()
        carro = Carro("ABC123", "Toyota", 2020)
        parqueadero.parquear_carro(carro)
        
        carro_encontrado = parqueadero.buscar_carro("XYZ769")
        self.assertIsNone(carro_encontrado)
    
if __name__ == "__main__":
    unittest.main()