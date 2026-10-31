# Importar la clase Incidente para crear los objetos de prueba.
from src.modelos.incidente import Incidente

# Importar el gestor que administra la colección de incidentes.
from src.modelos.gestor_incidentes import GestorIncidentes

# Crear el gestor donde se almacenarán los incidentes.
gestor = GestorIncidentes()

# Crear seis incidentes ficticios con diferentes gravedades.
incidentes = [
    Incidente(301, "Equipo infectado con malware", "Critica"),  # Incidente crítico.
    Incidente(302, "Acceso no autorizado", "Alta"),             # Incidente de gravedad alta.
    Incidente(303, "Intentos fallidos de acceso", "Media"),     # Incidente de gravedad media.
    Incidente(304, "Software desactualizado", "Baja"),          # Incidente de gravedad baja.
    Incidente(305, "Filtración de información", "Critica"),    # Segundo incidente crítico.
    Incidente(306, "Cuenta comprometida", "Alta")               # Segundo incidente de gravedad alta.
]
# Recorrer la lista para agregar cada incidente al gestor.
for incidente in incidentes:
    gestor.agregar(incidente)  # Guardar el incidente en la colección.

# Obtener el total de incidentes agrupados por gravedad.
conteo = gestor.contar_por_gravedad()

# Mostrar un título para identificar los resultados.
print("Resumen de incidentes por gravedad:")

# Recorrer el diccionario respetando el orden de las gravedades.
for gravedad, cantidad in conteo.items():
    # Mostrar cada gravedad junto con la cantidad de incidentes.
    print(f"{gravedad}: {cantidad}")
