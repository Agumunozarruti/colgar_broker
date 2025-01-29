from controladores.inversor_controlador import InversorControlador
from accesos.menu_cuenta import ejecutar
from accesos.utils import mostrar_titulo

def ejecutar_menu():
    inversor_ctrl = InversorControlador()

    while True:
        mostrar_titulo("MENU PRINCIPAL")
        print()
        print("1. Registrar inversor")
        print("2. Iniciar sesión")
        print("3. Salir")
        print()
        opcion = input("Seleccione una opción: ")
        print()

        if opcion == '1':
            inversor_ctrl.registrar_nuevo_inversor()
        elif opcion == '2':

            inv_log = inversor_ctrl.iniciar_sesion()
            if inv_log:
                ejecutar(inv_log)

        elif opcion == '3':
            mostrar_titulo("SALIENDO DEL SISTEMA")
            break
        else:
            print("Opción no válida. Intente de nuevo.")