from datos import Parqueadero, Carro


class ControlParqueadero:
    """
    Clase con la lógica del parqueadero, que realiza
    las validaciones necesarias en cada funcionalidad,
    antes de hacer cambios en los datos.
    """

    def __init__(self, parqueadero=None):
        if parqueadero is None:
            self.parqueadero = Parqueadero()
        else:
            self.parqueadero = parqueadero

    def parquear_carro(self, placa, marca, modelo) -> bool:
        """
        Realiza las validaciones necesarias antes de parquear el carro:
        Que se tengan puestos disponibles y que ya no esté parqueado.
        :return: True si lo pudo parquear (porque se cumplen las validaciones),
                 False en caso contrario.
        """
        if self.parqueadero.puestos_disponibles() <= 0:
            return False
        if self.parqueadero.buscar_carro(placa) is not None:
            return False
        carro = Carro(placa, marca, modelo)
        return self.parqueadero.parquear_carro(carro)

    def sacar_carro(self, placa) -> str | None:
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
