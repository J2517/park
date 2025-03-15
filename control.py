from datos import Parqueadero, Carro
from datetime import datetime  # Importar módulo para obtener el año actual
import re  # Importar módulo para expresiones regulares


class ControlParqueadero:
    """
    Clase con la lógica del parqueadero, que realiza
    las validaciones necesarias en cada funcionalidad,
    antes de hacer cambios en los datos.
    """

    def __init__(self, parqueadero=None):
        self.parqueadero = parqueadero if parqueadero else Parqueadero()

    def parquear_carro(self, placa: str, marca: str, modelo: int) -> bool:
        """
        Realiza las validaciones necesarias antes de parquear el carro:
        1. Que el modelo sea un número entero y válido.
        2. Que la marca no esté vacía.
        3. Que la placa tenga el formato correcto.
        4. Que haya puestos disponibles.
        5. Que el carro no esté ya parqueado.
        :return: True si lo pudo parquear (porque se cumplen las validaciones),
                 False en caso contrario.
        """
        # Obtener el año actual
        anio_actual = datetime.now().year

        # Validaciones
        if not isinstance(modelo, int):  # Validar que el modelo sea un número entero
            return False
        if modelo > anio_actual or modelo < 0:  # Validar rango del modelo
            return False
        if not marca.strip():  # Validar que la marca no sea una cadena vacía
            return False
        if not re.match(r"^[A-Z]{3}[0-9]{3}$", placa):  # Validar formato de la placa
            return False
        if self.parqueadero.puestos_disponibles() <= 0:
            return False
        if self.parqueadero.buscar_carro(placa) is not None:
            return False
        
        carro = Carro(placa, marca, modelo)
        return self.parqueadero.parquear_carro(carro)

    def sacar_carro(self, placa: str) -> str | None:
        """
        Verifica que efectivamente esté en el parqueadero para sacarlo.
        :return: Una cadena con los datos del carro, si se pudo sacar,
                 None si no estaba parqueado.
        """
        carro = self.parqueadero.buscar_carro(placa)
        if carro is None:
            return None
        pudo_sacar = self.parqueadero.sacar_carro(placa)
        if not pudo_sacar:
            return None
        return str(carro)

