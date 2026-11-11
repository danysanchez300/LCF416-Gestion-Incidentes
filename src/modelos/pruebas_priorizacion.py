# Importa las clases del proyecto.
from .incidente import Incidente
from .gestor_incidentes import GestorIncidentes

# Crea el gestor de incidentes.
gestor = GestorIncidentes()

# Crea seis incidentes con diferentes gravedades.
incidentes = [
    Incidente("I-101", "Incidente de gravedad Media", "Media"),
    Incidente("I-102", "Incidente de gravedad Alta", "Alta"),
    Incidente("I-103", "Incidente de gravedad Critica", "Critica"),
    Incidente("I-104", "Incidente de gravedad Alta", "Alta"),
    Incidente("I-105", "Incidente de gravedad Baja", "Baja"),
    Incidente("I-106", "Incidente de gravedad Critica", "Critica")
]

# Agrega todos los incidentes al gestor.
for incidente in incidentes:
    gestor.agregar(incidente)

# Cierra dos incidentes para comprobar que se excluyen.
incidentes[4].cerrar()
incidentes[5].cerrar()

# Consulta los incidentes pendientes priorizados.
resultado = gestor.pendientes_priorizados()

# Muestra los resultados.
print("INCIDENTES PENDIENTES PRIORIZADOS")

for incidente in resultado:
    print(incidente.id, "-", incidente.gravedad, "-", incidente.estado)

# Comprueba que la colección original conserva su orden.
print("\nORDEN ORIGINAL CONSERVADO:")

for incidente in gestor.listar():
    print(incidente.id, "-", incidente.gravedad, "-", incidente.estado)
