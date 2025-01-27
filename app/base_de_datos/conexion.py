import traceback
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv
load_dotenv()

class Conexion:
    def __init__(self):
        self.conexion = None
        self.transaccion_activa = False
        self.establecer_conexion()#agrego

    def __enter__(self):
        self.cursor = self.conexion.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            self.revertir()  # Rollback si ocurre un error
        else:
            self.confirmar()  # Commit si todo sale bien
        self.cerrar_conexion()  # Cerrar la conexión

    def establecer_conexion(self):
        """Establece la conexión con la base de datos."""
        try:

            self.conexion = mysql.connector.connect(
                host=os.getenv("HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME")
            )
            # self.conexion = mysql.connector.connect(
            #     host="localhost",
            #     user="root",
            #     password="admin",
            #     database="arg_broker",
            #     port=3307  # Especifica el puerto aquí
            # )

            if self.conexion.is_connected():
                print("Conexión exitosa a la base de datos.")

        except Error as e:
            print(f"Error al conectar con la base de datos: {e}")
            self.conexion = None

    def ejecutar_query(self, query, valores=None, mantener_transaccion=False):
        """Ejecuta una consulta en la base de datos, manejando transacciones."""
        conexion_abierta = True
        if self.conexion is None or not self.conexion.is_connected():
            self.establecer_conexion()
            conexion_abierta = False
            

        cursor = self.conexion.cursor()
        try:
            if valores:
                cursor.execute(query, valores)
            else:
                cursor.execute(query)
            
            # Si es un SELECT, devuelve los resultados
            if query.strip().lower().startswith("select"):
                return cursor.fetchall()

            # Devuelve el ID de la última fila insertada para INSERT, UPDATE, DELETE
            return cursor.lastrowid

        except Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            traceback.print_exc()
            self.revertir()  # Hace rollback si ocurre un error
            return False
    
        finally:
            cursor.close()
            # Si no se debe mantener la transacción, confirma o revierte según corresponda
            if not mantener_transaccion:
                if self.transaccion_activa:
                    try:
                        self.confirmar()
                    except Exception as e:
                        self.revertir()
            if not mantener_transaccion and not self.transaccion_activa and not conexion_abierta:
                self.cerrar_conexion()

    def iniciar_transaccion(self):
        """Inicia una transacción manualmente."""
        if self.conexion and self.conexion.is_connected():
            try:
                self.conexion.start_transaction()
                self.transaccion_activa = True
            except Error as e:
                print(f"Error al iniciar la transacción: {e}")

    def verificar_existencia(self, tabla, campo, valor):
        """Verifica si existe un registro en la tabla según el campo y valor proporcionados."""
        query = f"SELECT COUNT(*) FROM {tabla} WHERE {campo} = %s"
        resultado = self.ejecutar_query(query, (valor,))
        return resultado[0][0] > 0 if resultado else False

    def confirmar(self):
        """Confirma los cambios en la base de datos."""
        try:
            if self.conexion and self.conexion.is_connected():
                self.conexion.commit()
                self.transaccion_activa = False
        except Error as e:
            print(f"Error al confirmar la transacción: {e}")
            self.revertir()

    def revertir(self):
        """Revierte la transacción actual."""
        if self.conexion:
            self.conexion.rollback()
        """Confirma los cambios en la base de datos."""
        if self.conexion and self.conexion.is_connected():
            try:
                self.conexion.commit()
                self.transaccion_activa = False
            except Error as e:
                print(f"Error al confirmar la transacción: {e}")
                self.revertir()

    def cerrar_conexion(self):
        """Cierra la conexión solo si no hay una transacción en curso."""
        if not self.transaccion_activa and self.conexion and self.conexion.is_connected():
            self.conexion.close()
        elif self.transaccion_activa:
            print("No se cerró la conexión porque hay una transacción en curso.")

    def obtener_cursor(self):
        """Devuelve un cursor para realizar operaciones en la base de datos."""
        if self.conexion and self.conexion.is_connected():
            return self.conexion.cursor(buffered=True)
        else:
            return None

