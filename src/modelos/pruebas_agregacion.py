
from src.modelos.incidente import Incidente
from src.modelos.gestor_incidentes import GestorIncidentes

# Crear un incidente independiente del gestor.
incidente = Incidente(201, "Equipo con malware", "Critica")

# Crear el gestor y agregar el incidente.
gestor = GestorIncidentes()
gestor.agregar(incidente)

print("Incidentes en el gestor:", len(gestor.listar()))

# Quitar el incidente de la colección.
gestor.quitar(201)

print("Incidentes después de quitarlo:", len(gestor.listar()))

# Comprobar que el objeto todavía existe.
print("El objeto sigue existiendo:", incidente.id)
print("Descripción:", incidente.descripcion)
print("Estado:", incidente.estado)

# Probar que el gestor no permite agregar incidentes con IDs duplicados.
print("\nPrueba de ID duplicado:")

# Crear un gestor independiente para esta prueba.
gestor_prueba = GestorIncidentes()

# Crear dos incidentes con el mismo ID.
incidente_1 = Incidente(301, "Acceso sospechoso", "Alta")
incidente_duplicado = Incidente(301, "Intento de acceso no autorizado", "Media")

# Agregar el primer incidente correctamente.
gestor_prueba.agregar(incidente_1)

try:
    # Intentar agregar el segundo incidente con el mismo ID.
    gestor_prueba.agregar(incidente_duplicado)
except ValueError as error:
    # Mostrar el mensaje generado al detectar el ID duplicado.
    print("ID duplicado rechazado:", error)