# Clase Usuario: representa a una persona responsable dentro del sistema.
class Usuario:

    # Constructor que inicializa el objeto con su identificador y nombre.
    def __init__(self, id, nombre):
        self.id = id              # Guarda el identificador del usuario.
        self.nombre = nombre      # Guarda el nombre del usuario.

    # Método que devuelve un resumen de la información del usuario.
    def resumen(self):
        return f"Usuario {self.id}: {self.nombre}"