from app.accesos.utils import mostrar_titulo

def ejecutar_menu_transacciones(cuenta_controlador, inversor, id_inversor):
    while True:
        mostrar_titulo("TRANSACCIONES")

        print()
        print("1. Comprar acciones")
        print("2. Vender acciones")
        print("3. Volver al menú principal")
        print()

        opcion = input("Seleccione una opción: ")
        print()

        if opcion == "1":
            cuenta_controlador.comprar_acciones(id_inversor)
        elif opcion == "2":
            cuenta_controlador.vender_acciones(id_inversor)
        elif opcion == "3":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida.")
