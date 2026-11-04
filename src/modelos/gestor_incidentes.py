# Importa la clase Incidente para validar los objetos recibidos.
from .incidente import Incidente

# Clase GestorIncidentes: administra incidentes que ya existen.
class GestorIncidentes:

    # Inicializa la lista interna de incidentes.
    def __init__(self):
        self._incidentes = []

    # Agrega un incidente existente a la colección.
    def agregar(self, incidente):
        # Verificar que el objeto sea un Incidente.
        if not isinstance(incidente, Incidente):
            raise TypeError("Se requiere un objeto Incidente.")

        # Evitar que existan IDs duplicados.
        for existente in self._incidentes:
            if existente.id == incidente.id:
                raise ValueError(f"ID duplicado: {incidente.id}")

        # Guardar la referencia al incidente.
        self._incidentes.append(incidente)

    # Devuelve una copia de la lista de incidentes.
    def listar(self):
        return list(self._incidentes)

    # Quita un incidente por su ID y devuelve el objeto.
    def quitar(self, id):
        for incidente in self._incidentes:
            if incidente.id == id:
                self._incidentes.remove(incidente)
                return incidente        

        # Si el ID no existe, devuelve None.
        return None

    # Cuenta cuántos incidentes hay de cada nivel de gravedad.
    def contar_por_gravedad(self):
        # Crear un contador para cada una de las cuatro gravedades.
        conteo = {
            "Critica": 0,  # Inicializa el contador de gravedad crítica.
            "Alta": 0,     # Inicializa el contador de gravedad alta.
            "Media": 0,    # Inicializa el contador de gravedad media.
            "Baja": 0      # Inicializa el contador de gravedad baja.
        }

        # Recorrer todos los incidentes guardados en la colección.
        for incidente in self._incidentes:
            # Aumentar en uno el contador de la gravedad correspondiente.
            conteo[incidente.gravedad] += 1

        # Devolver el diccionario con los totales calculados.
        return conteo
