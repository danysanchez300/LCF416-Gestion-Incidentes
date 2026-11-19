# Importa la clase base Incidente.
from .incidente import Incidente


# Clase hija que representa un incidente de acceso.
class IncidenteAcceso(Incidente):

    # Constructor con los datos generales y específicos.
    def __init__(self, id, descripcion, gravedad,
                 usuario_afectado, intentos_detectados):

        # Reutiliza el constructor de la clase padre.
        super().__init__(id, descripcion, gravedad)

        # Guarda los datos específicos del incidente de acceso.
        self.usuario_afectado = usuario_afectado
        self.intentos_detectados = intentos_detectados

    # Sobrescribe el método generar_reporte().
    def generar_reporte(self):

        # Obtiene el reporte general de la clase padre.
        reporte = super().generar_reporte()

        # Agrega el usuario y los intentos detectados.
        return (
            f"{reporte} | "
            f"Usuario: {self.usuario_afectado} | "
            f"Intentos: {self.intentos_detectados}"
        )