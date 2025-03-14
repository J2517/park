from control import ControlParqueadero


class MenuParqueadero:
    """
    Representa la interfaz de usuario (simulada con Consola), para
    pedir los datos y mostrar los mensajes al usuario, de acuerdo con
    los resultados de las operaciones.
    """
    def __init__(self, control=None):
        if control is None:
            self.control = ControlParqueadero()
        else:
            self.control = control

    def parquear_carro(self):
        """
        Estaciona un carro en el parqueadero.
        Se piden los datos del carro y se solicita al controlador que lo parquee.
        En caso de no poderlo parquear se muestra un mensaje indicando esto.
        """
        placa = input("Placa del carro: ")
        marca = input("Marca del carro: ")
        modelo = int(input("Modelo del carro: "))

        pudo_parquear = self.control.parquear_carro(placa, marca, modelo)
        if pudo_parquear:
            print(" Carro parqueado exitosamente ")
        else:
            print(" No se pudo parquear el carro - "
                  "No hay disponibilidad o ya hay un carro con esa placa ")

    def sacar_carro(self):
        """
        Permite sacar un carro del parqueadero.
        Para sacar el carro se debe pedir la placa y luego se debe mostrar un mensaje
        indicando si fue posible sacar el carro o si no se encontraba en el parqueadero.
        """
        placa = input("Placa del carro: ")

        datos_carro = self.control.sacar_carro(placa)
        if datos_carro:
            print(f" Carro sale del parqueadero: {datos_carro}")
        else:
            print(" No se pudo sacar el carro - "
                  "No se encontró un carro con esa placa ")

    def menu_principal(self):
        """
        Muestra las opciones del parqueadero al usuario, para que seleccione
        lo que desea realizar: parquear un carro o sacarlo.
        """
        opcion = -1

        print(" ---- PARQUEADERO RAYACARRO---  ")
        while opcion != 0:
            print("\n"
                  "1.Parquear un carro    \n"
                  "2.Sacar un carro       \n"
                  "0.Terminar             \n\n"
                  "Opción: ")
            try:
                opcion = int(input())
            except ValueError:
                print("Por favor, ingrese un número válido.")
                continue

            if opcion == 1:
                self.parquear_carro()
            elif opcion == 2:
                self.sacar_carro()
            elif opcion == 0:
                break
            else:
                print("Opción no disponible")

        print(" - Gracias por confiar en RayaCarro -")


if __name__ == "__main__":
    menu = MenuParqueadero()
    menu.menu_principal()