import traceback
import pymysql
from pymysql import Error
import os
from dotenv import load_dotenv

load_dotenv()

class Conexion:
    def __init__(self):
        self.conexion = None
        self.transaccion_activa = False
        self.establecer_conexion()

    def __enter__(self):
        self.cursor = self.conexion.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            self.revertir()
        else:
            self.confirmar()
        self.cerrar_conexion()

    def establecer_conexion(self):
        """Establece la conexión con la base de datos."""
        try:
            self.conexion = pymysql.connect(
                host='bunzgmjcedk0knclch1t-mysql.services.clever-cloud.com',
                user='u0tikbfz0kqzjfuz',
                password='8vBelpDoym9FmQuPdyso',
                database='bunzgmjcedk0knclch1t',
                port=3306  # Añadir puerto con default 3306
            )


            if self.conexion.open:
                print("Conexión exitosa a la base de datos.")

        except Error as e:
            print(f"Error al conectar con la base de datos: {e}")
            self.conexion = None

    def ejecutar_query(self, query, valores=None, mantener_transaccion=False):
        """Ejecuta una consulta en la base de datos."""
        conexion_abierta = True
        if self.conexion is None or not self.conexion.open:
            self.establecer_conexion()
            conexion_abierta = False

        cursor = self.conexion.cursor()
        try:
            if valores:
                cursor.execute(query, valores)
            else:
                cursor.execute(query)

            if query.strip().lower().startswith("select"):
                return cursor.fetchall()

            return cursor.lastrowid

        except Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            traceback.print_exc()
            self.revertir()
            return False

        finally:
            cursor.close()
            if not mantener_transaccion and self.transaccion_activa:
                try:
                    self.confirmar()
                except Exception:
                    self.revertir()
            if not mantener_transaccion and not self.transaccion_activa and not conexion_abierta:
                self.cerrar_conexion()

    def iniciar_transaccion(self):
        """Inicia una transacción manualmente."""
        if self.conexion and self.conexion.open:
            try:
                self.conexion.begin()
                self.transaccion_activa = True
            except Error as e:
                print(f"Error al iniciar la transacción: {e}")

    def verificar_existencia(self, tabla, campo, valor):
        """Verifica si existe un registro en la tabla."""
        query = f"SELECT COUNT(*) FROM {tabla} WHERE {campo} = %s"
        resultado = self.ejecutar_query(query, (valor,))
        return resultado[0][0] > 0 if resultado else False

    def confirmar(self):
        """Confirma los cambios en la base de datos."""
        try:
            if self.conexion and self.conexion.open:
                self.conexion.commit()
                self.transaccion_activa = False
        except Error as e:
            print(f"Error al confirmar la transacción: {e}")
            self.revertir()

    def revertir(self):
        """Revierte la transacción actual."""
        if self.conexion:
            try:
                self.conexion.rollback()
                self.transaccion_activa = False
            except Error as e:
                print(f"Error al hacer rollback: {e}")

    def cerrar_conexion(self):
        """Cierra la conexión solo si no hay una transacción en curso."""
        if not self.transaccion_activa and self.conexion and self.conexion.open:
            self.conexion.close()
        elif self.transaccion_activa:
            print("No se cerró la conexión porque hay una transacción en curso.")

    def obtener_cursor(self):
        """Devuelve un cursor para realizar operaciones en la base de datos."""
        if self.conexion and self.conexion.open:
            return self.conexion.cursor()
        return None
