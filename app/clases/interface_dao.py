from abc import ABC, abstractmethod


class InterfaceDAO(ABC):

    def verificar_existencia(self, campo, valor):
        """Verifica si existe un registro según el campo y valor proporcionado"""
        pass

    def obtener_todos(self):
        """Obtiene todos los registros"""
        pass

    def obtener_uno(self, id):
        """Encuentra un registro por su ID"""
        pass

    def eliminar(self, id):
        """Elimina un registro por su ID"""
        pass

    def actualizar(self, id, data):
        """Actualiza un registro existente"""
        pass

    def insertar(self, data):
        """Inserta un nuevo registro"""
        pass