
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
