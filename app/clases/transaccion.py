class Transaccion:
    def __init__(self, id_accion, simbolo, razon_social, monto_total, comision, tipo):
        self._id_accion = id_accion
        self._simbolo = simbolo
        self._razon_social = razon_social
        self._monto_total = monto_total
        self._comision = comision
        self._tipo = tipo

    # Propiedad para id_accion
    @property
    def id_accion(self):
        return self._id_accion

    @id_accion.setter
    def id_accion(self, value):
        self._id_accion = value

    # Propiedad para simbolo
    @property
    def simbolo(self):
        return self._simbolo

    @simbolo.setter
    def simbolo(self, value):
        self._simbolo = value

    # Propiedad para razon_social
    @property
    def razon_social(self):
        return self._razon_social

    @razon_social.setter
    def razon_social(self, value):
        self._razon_social = value

    # Propiedad para monto_total
    @property
    def monto_total(self):
        return self._monto_total

    @monto_total.setter
    def monto_total(self, value):
        self._monto_total = value

    # Propiedad para comision
    @property
    def comision(self):
        return self._comision

    @comision.setter
    def comision(self, value):
        self._comision = value

    # Propiedad para tipo
    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, value):
        self._tipo = value
