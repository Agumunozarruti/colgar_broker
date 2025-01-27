from app.controladores.cuenta_controlador import CuentaControlador
from app.servicios_dao.inversor_dao import InversorDAO
from app.accesos.menu_transacciones import ejecutar_menu_transacciones
from app.accesos.utils import mostrar_titulo


def ejecutar(inversor):
    try:
        
        cuenta_controlador = CuentaControlador()
        inversor_dao = InversorDAO()

        # Obtener información del inversor
        inversor_info = inversor_dao.obtener_uno(inversor.email)
        if not inversor_info:
            raise Exception("No se pudo obtener la información del inversor")

        id_inversor = inversor_info[0]
        while True:
            mostrar_titulo(f" BIENVENIDO {inversor.razon_social} !")
            print()
            print("1. Mostrar datos de la cuenta")
            print("2. Listar activos de la cuenta")
            print("3. Realizar transacciones")
            print("4. Cerrar sesión")
            print()
            opcion = input("Seleccione una opcion: ")
            print()

            if opcion == "1":
                cuenta_controlador.mostrar_datos_cuenta(id_inversor)
            elif opcion == "2":
                cuenta_controlador.mostrar_activos_portafolio(id_inversor)
            elif opcion == "3":
                ejecutar_menu_transacciones(cuenta_controlador, inversor, id_inversor)
            elif opcion == "4":
                break
            else:
                print("Opción no válida")
    except Exception as e:
        print(f"Error durante la ejecución: {e}")


