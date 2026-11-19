# Importa la clase Incidente para validar los objetos recibidos.
from .incidente import Incidente

# Clase que administra una colección de incidentes.
class GestorIncidentes:

    # Constructor que inicializa la lista de incidentes.
    def __init__(self):
        self._incidentes = []  # Guarda las referencias a los incidentes.

    # Método para agregar un incidente al catálogo.
    def agregar(self, incidente):

        # Comprueba que el objeto recibido sea un Incidente.
        if not isinstance(incidente, Incidente):
            raise TypeError("Se requiere un objeto Incidente.")

        # Revisa que no exista otro incidente con el mismo ID.
        for existente in self._incidentes:
            if existente.id == incidente.id:
                raise ValueError(f"ID duplicado: {incidente.id}")

        self._incidentes.append(incidente)  # Agrega el incidente.

    # Método que devuelve una copia de la lista de incidentes.
    def listar(self):
        return list(self._incidentes)

    # Método para quitar un incidente mediante su ID.
    def quitar(self, id):
        for incidente in self._incidentes:
            if incidente.id == id:
                self._incidentes.remove(incidente)  # Lo quita de la lista.
                return incidente  # Devuelve el objeto eliminado.

        return None  # Indica que el ID no fue encontrado.

    # Método que cuenta los incidentes por gravedad.
    def contar_por_gravedad(self):

        # Crea un contador para cada nivel de gravedad.
        conteo = {
            "Critica": 0,
            "Alta": 0,
            "Media": 0,
            "Baja": 0
        }

        # Recorre los incidentes y cuenta cada gravedad.
        for incidente in self._incidentes:
            conteo[incidente.gravedad] += 1

        return conteo  # Devuelve el total por gravedad.

    # Método que cierra un incidente y utiliza un notificador.
    def cerrar_incidente(self, incidente, notificador):

        # Cambia el estado del incidente a Cerrado.
        incidente.cerrar()

        # Envía una notificación utilizando el servicio recibido.
        notificador.enviar(incidente)

    
    # Método que devuelve los incidentes abiertos ordenados por prioridad.
    def pendientes_priorizados(self):

        # Define el orden de prioridad de las gravedades.
        prioridad = {
            "Critica": 0,
            "Alta": 1,
            "Media": 2,
            "Baja": 3
        }

        # Crea una lista nueva únicamente con incidentes abiertos.
        abiertos = [
            incidente
            for incidente in self._incidentes
            if incidente.estado == "Abierto"
        ]

        # Ordena la lista nueva sin modificar la colección original.
        # sorted() conserva el orden de registro cuando hay empates.
        return sorted(
            abiertos,
            key=lambda incidente: prioridad[incidente.gravedad]
        )
