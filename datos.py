class Carro:
    """
    Un vehículo particular que puede hacer uso del parqueadero.
    """

    def __init__(self, placa: str, marca: str, modelo: int):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return "placa=" + self.placa + ", marca=" + self.marca + ", modelo=" + str(self.modelo)


class Parqueadero:
    """
    Clase que simula la persistencia de los datos del parqueadero.
    Tiene el registro de los espacios disponibles y de los carros parqueados.
    """

    def __init__(self):
        self.__carros = [None] * 20

    def buscar_carro(self, placa: str) -> Carro | None:
        """
        Busca un carro en el parqueadero por la placa (sin sacarlo).
        :param placa: La placa (identificador) del carro que se desea buscar.
        :return: Una referencia al carro, en caso de encontrarlo en el parqueadero,
                 o 
                 None en caso contrario.
        """
        for carro in self.__carros:
            if carro and carro.placa == placa:
                return carro
        return None

    def sacar_carro(self, placa):
        """
        Saca un carro del parqueadero.
        :param placa: La placa (identificador) del carro que se desea sacar.
        :return: True si pudo sacar el carro porque se encontraba parqueado,
                 False en caso contrario.
        """
        for i, carro in enumerate(self.__carros):
            if carro and carro.placa == placa:
                self.__carros[i] = None
                return True
        return False

    def parquear_carro(self, carro):
        """
        Ubica un carro en el primer espacio disponible que encuentre
        en el parqueadero.
        :param carro: El carro que se desea parquear.
        :return: True si lo pudo parquear (porque hay un espacio),
                 False en caso contrario.
        """
        for i, espacio in enumerate(self.__carros):
            if espacio is None:
                self.__carros[i] = carro
                return True
        return False

    def puestos_disponibles(self):
        """
        Contabiliza los espacios disponibles en el parqueadero.
        :return: La cantidad de puestos o espacios donde es posible
                 ubicar un carro en el parqueadero.
        """
        return self.__carros.count(None)
