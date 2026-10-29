# Importa la clase Usuario para utilizarla como responsable del incidente.
from .usuario import Usuario


# Clase Incidente: representa un incidente de ciberseguridad.
class Incidente:

    # Constructor que inicializa los datos del incidente.
    def __init__(self, id, descripcion, gravedad):
        # Definir las cuatro gravedades permitidas por el sistema
        gravedades_validas = ("Baja", "Media", "Alta", "Critica")

        # Comprobar que la gravedad recibida sea válida
        if gravedad not in gravedades_validas:
            # Generar un error si la gravedad no está permitida
            raise ValueError(
                f"Gravedad no válida: {gravedad}. "
                f"Utiliza una de estas opciones: {', '.join(gravedades_validas)}"
            )

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
        # Comprobar si el incidente ya está cerrado.
        if self.estado == "Cerrado":
            print(f"El incidente {self.id} ya está cerrado.")
            return

        # Actualizar el estado del incidente.
        self.estado = "Cerrado"