import re

class Inversor:
    def __init__(self, documento, email, telefono, razon_social, perfil_inversor, tipo_documento, tipo_inversor, contrasena):
        self._documento = documento  # Encapsulamiento: atributos protegidos
        self._email = email
        self._telefono = telefono
        self._razon_social = razon_social
        self._id_perfil_inversor = perfil_inversor
        self._id_tipo_documento = tipo_documento
        self._id_tipo_inversor = tipo_inversor
        self._contrasena = contrasena  # Almacena la contraseña en texto plano

    @property
    def documento(self):
        return self._documento
    
    @property
    def email(self):
        return self._email

    @property
    def telefono(self):
        return self._telefono

    @property
    def razon_social(self):
        return self._razon_social

    @property
    def id_perfil_inversor(self):
        return self._id_perfil_inversor

    @property
    def id_tipo_documento(self):
        return self._id_tipo_documento

    @property
    def id_tipo_inversor(self):
        return self._id_tipo_inversor

    @property
    def contrasena(self):
        return self._contrasena

    # Método para verificar la contraseña
    def verificar_contrasena(self, contrasena):
        return self._contrasena == contrasena
    
    def incrementar_intentos_fallidos(self):
        """Incrementa los intentos fallidos en 1."""
        self._intentos_fallidos += 1

    def resetear_intentos_fallidos(self):
        """Reinicia los intentos fallidos a 0."""
        self._intentos_fallidos = 0

    def esta_bloqueado(self):
        """Indica si el inversor está bloqueado por intentos fallidos."""
        return self._intentos_fallidos >= 3
    
    """VALIDACION DE EMAIL"""
    def validar_email(email):
        # Expresión regular para validar email
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(patron, email) is not None
    
    """VALIDACION DOCUMENTO"""
    def validar_documento(documento, tipo_documento):
        # Define las longitudes esperadas para cada tipo
        longitudes = {1: 11, 2: 11, 3: 9}  # CUIL/CUIT: 11 dígitos, Pasaporte: 9 dígitos
        return documento.isdigit() and len(documento) == longitudes.get(tipo_documento, 0)

    """VALIDACION CONTRASEÑA"""
    def validar_contrasena(contrasena):
        if (len(contrasena) < 8 or
            not re.search(r"[A-Z]", contrasena) or  # Al menos una letra mayúscula
            not re.search(r"[a-z]", contrasena) or  # Al menos una letra minúscula
            not re.search(r"[0-9]", contrasena) or  # Al menos un número
            not re.search(r"[!@#$%^&*(),.?\":{}|<>]", contrasena)):  # Al menos un símbolo
            return False
        return True
    # Método para mostrar información del inversor
    def mostrar_info(self):
        return {
            "Inversor": self.razon_social,
            "Documento": self._documento,
            "Email": self._email,
            "Teléfono": self._telefono,
            "Perfil de Inversor": self._id_perfil_inversor,
            "Tipo de Documento": self._id_tipo_documento,
            "Tipo de Inversor": self._id_tipo_inversor
        }