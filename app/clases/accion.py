class Accion:
    def __init__(self, id_accion, simbolo, nombre_empresa):
        """Inicializa los atributos de la clase Accion."""
        self._id_accion = id_accion
        self._simbolo = simbolo
        self._nombre_empresa = nombre_empresa

    # Getters y Setters (Encapsulamiento)
    @property
    def id_accion(self):
        return self._id_accion

    @id_accion.setter
    def id_accion(self, id_accion):
        self._id_accion = id_accion

    @property
    def simbolo(self):
        return self._simbolo

    @simbolo.setter
    def simbolo(self, simbolo):
        self._simbolo = simbolo

    @property
    def nombre_empresa(self):
        return self._nombre_empresa

    @nombre_empresa.setter
    def nombre_empresa(self, nombre_empresa):
        self._nombre_empresa = nombre_empresa

    def __str__(self):
        """Devuelve una representación en cadena de la acción."""
        return f"ID: {self._id_accion}, Símbolo: {self._simbolo}, Empresa: {self._nombre_empresa}"

    def actualizar_simbolo(self, nuevo_simbolo):
        """Permite actualizar el símbolo de la acción."""
        self.simbolo = nuevo_simbolo

    def actualizar_nombre_empresa(self, nuevo_nombre):
        """Permite actualizar el nombre de la empresa."""
        self.nombre_empresa = nuevo_nombre
