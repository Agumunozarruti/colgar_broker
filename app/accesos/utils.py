from prettytable import PrettyTable

def mostrar_titulo(titulo, ancho=112):
    """Muestra un título con formato decorativo utilizando PrettyTable."""
    # Crear una tabla solo para el título
    tabla_titulo = PrettyTable()
    tabla_titulo.field_names = [titulo]  # Establece el título como encabezado de la tabla

    # Ajustar el ancho de la tabla
    tabla_titulo.align[titulo] = "c"  # Centrar el texto en la columna
    
    tabla_titulo.min_width[titulo] = ancho

    # Añadir una fila vacía para el estilo
    tabla_titulo.add_row(["ARG BROKER - PROYECTO ABP MODULO PROGRAMADOR"])

    # Mostrar el título decorado
    print(tabla_titulo)
    print()