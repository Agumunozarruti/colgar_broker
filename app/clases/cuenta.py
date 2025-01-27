class Cuenta:
    def __init__(self, id_cuenta, numero_cuenta, saldo, fecha_creacion):
        self._id_cuenta = id_cuenta
        self._numero_cuenta = numero_cuenta
        self._saldo = saldo
        self._fecha_creacion = fecha_creacion

    # Propiedad para id_cuenta
    @property
    def id_cuenta(self):
        return self._id_cuenta

    @id_cuenta.setter
    def id_cuenta(self, value):
        self._id_cuenta = value

    # Propiedad para numero_cuenta
    @property
    def numero_cuenta(self):
        return self._numero_cuenta

    @numero_cuenta.setter
    def numero_cuenta(self, value):
        self._numero_cuenta = value

    # Propiedad para saldo
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, value):
        self._saldo = value

    # Propiedad para fecha_creacion
    @property
    def fecha_creacion(self):
        return self._fecha_creacion

    @fecha_creacion.setter
    def fecha_creacion(self, value):
        self._fecha_creacion = value


