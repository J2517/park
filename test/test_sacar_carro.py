import unittest
from datos import Carro, Parqueadero

class TestSacarCarro(unittest.TestCase):

    def test_sacar_carro_existente(self):
        parqueadero = Parqueadero()
        carro = Carro("ABC123", "Toyota", 2020)
        parqueadero.parquear_carro(carro)
        
        resultado = parqueadero.sacar_carro("ABC123")
        self.assertTrue(resultado)
    
    def test_sacar_carro_inexistente(self):
        parqueadero = Parqueadero()
        resultado = parqueadero.sacar_carro("XYZ769")
        self.assertFalse(resultado)
    
    def test_sacar_carro_liberar_espacio(self):
        parqueadero = Parqueadero()
        carro = Carro("ABC123", "Toyota", 2020)
        parqueadero.parquear_carro(carro)
        
        puestos_antes = parqueadero.puestos_disponibles()
        parqueadero.sacar_carro("ABC123")
        puestos_despues = parqueadero.puestos_disponibles()
        
        self.assertEqual(puestos_despues, puestos_antes + 1)
    
    def test_sacar_carro_multiples_veces(self):
        parqueadero = Parqueadero()
        carro = Carro("ABC123", "Toyota", 2020)
        parqueadero.parquear_carro(carro)
        
        resultado_primera_vez = parqueadero.sacar_carro("ABC123")
        resultado_segunda_vez = parqueadero.sacar_carro("ABC123")
        
        self.assertTrue(resultado_primera_vez)
        self.assertFalse(resultado_segunda_vez)

if __name__ == "__main__":
    unittest.main()