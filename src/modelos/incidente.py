
# Clase base: representa un incidente de ciberseguridad.
class Incidente:

    # Constructor que inicializa los datos generales del incidente.
    def __init__(self, id, descripcion, gravedad):
        self.id = id
        self.descripcion = descripcion

        # La gravedad se asigna mediante el setter para validarla.
        self.gravedad = gravedad

        # El estado inicial del incidente es Abierto.
        self._estado = "Abierto"

        # Inicialmente el incidente no tiene responsable.
        self.responsable = None

    # Propiedad para consultar la gravedad.
    @property
    def gravedad(self):
        return self._gravedad

    # Setter para validar la gravedad.
    @gravedad.setter
    def gravedad(self, valor):
        gravedades_validas = ("Baja", "Media", "Alta", "Critica")

        if valor not in gravedades_validas:
            raise ValueError("Gravedad no permitida")

        self._gravedad = valor

    # Propiedad de solo lectura para consultar el estado.
    @property
    def estado(self):
        return self._estado

    # Método para asignar un responsable al incidente.
    def asignar_responsable(self, usuario):
        self.responsable = usuario

    # Método para generar el reporte general del incidente.
    def generar_reporte(self):
        return (
            f"ID: {self.id} | "
            f"Descripción: {self.descripcion} | "
            f"Gravedad: {self.gravedad} | "
            f"Estado: {self.estado}"
        )

    # Método para cerrar el incidente.
    def cerrar(self):
        self._estado = "Cerrado"

    # Método para reabrir el incidente.
    def reabrir(self):
        self._estado = "Abierto"
