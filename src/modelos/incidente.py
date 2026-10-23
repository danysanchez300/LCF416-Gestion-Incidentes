# Importa la clase Usuario para utilizarla como responsable del incidente.
from modelos.usuario import Usuario


# Clase Incidente: representa un incidente de ciberseguridad.
class Incidente:

    # Constructor que inicializa los datos del incidente.
    def __init__(self, id, descripcion, gravedad):
        self.id = id                          # Identificador del incidente.
        self.descripcion = descripcion        # Descripción del incidente.
        self.gravedad = gravedad              # Nivel de gravedad.
        self.estado = "Abierto"               # Estado inicial del incidente.
        self.responsable = None               # Inicialmente no tiene responsable.

    # Método para asignar un usuario como responsable del incidente.
    def asignar_responsable(self, usuario):
        self.responsable = usuario            # Guarda la referencia al objeto Usuario.

    # Método para cerrar el incidente.
    def cerrar(self):
        self.estado = "Cerrado"               # Actualiza el estado del incidente.