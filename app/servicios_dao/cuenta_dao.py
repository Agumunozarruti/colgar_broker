from mysql.connector import Error
from app.base_de_datos.conexion import Conexion
from app.clases.interface_dao import InterfaceDAO
from app.clases.transaccion import Transaccion


class CuentaDAO(InterfaceDAO):
    
    def obtener_datos_cuenta(self, id_cuenta):
        with Conexion() as conexion:
            try:
                query = """
                SELECT numero_cuenta, saldo, fecha_creacion 
                FROM cuentas 
                WHERE id_inversor = %s
                """
                resultado = conexion.ejecutar_query(query, (id_cuenta,))
                return resultado[0] if resultado else None

            except Error as e:
                print(f"Error al acceder a la base de datos: {e}")
                raise
                # return None


    def verificar_existencia(self, campo, valor):
        """Verifica si existe un registro según el campo y valor proporcionado"""
        raise NotImplementedError("El método verificar_existencia no está implementado.")

    def obtener_todos(self):
        """Obtiene todos los registros"""
        raise NotImplementedError("El método obtener_todos no está implementado.")


    def obtener_transacciones_por_cuenta(self, id_cuenta):
        with Conexion() as conexion:
            query = """
                SELECT a.id_accion, a.simbolo, i.razon_social, 
                    SUM(t.monto_total) AS monto_total, 
                    SUM(t.comision) AS total_comision,
                    t.id_tipo_transaccion
                FROM transacciones t
                INNER JOIN cuentas c ON t.numero_cuenta = c.numero_cuenta
                INNER JOIN acciones a ON t.id_accion = a.id_accion
                INNER JOIN inversores i ON i.id_inversor = c.id_inversor
                WHERE c.id_inversor = %s
                GROUP BY a.id_accion, a.simbolo, i.razon_social, t.id_tipo_transaccion
            """
            resultado = conexion.ejecutar_query(query, (id_cuenta,))

            return [
                Transaccion(id_accion, simbolo, razon_social, monto_total, total_comision, tipo)
                for id_accion, simbolo, razon_social, monto_total, total_comision, tipo in resultado
            ] if resultado else []


    def obtener_uno(self, id):
        """Encuentra un registro por su ID"""
        raise NotImplementedError("El método obtener_uno no está implementado.")

    def eliminar(self, id):
        """Elimina un registro por su ID"""
        raise NotImplementedError("El método eliminar no está implementado.")

    def actualizar(self, id, data):
        """Actualiza un registro existente"""
        raise NotImplementedError("El método actualizar no está implementado.")

    def insertar(self, data):
        """Inserta un nuevo registro"""
        raise NotImplementedError("El método insertar no está implementado.")
