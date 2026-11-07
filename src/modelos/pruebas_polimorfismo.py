
# Importar las clases que se van a utilizar.
from src.modelos.incidente import Incidente
from src.modelos.incidente_malware import IncidenteMalware
from src.modelos.incidente_acceso import IncidenteAcceso


# Crear una lista con cuatro incidentes de diferentes tipos.
incidentes = [

    # Crear dos incidentes generales.
    Incidente(401, "Equipo con actividad sospechosa", "Media"),

    Incidente(402, "Software desactualizado", "Baja"),

    # Crear un incidente de tipo Malware.
    IncidenteMalware(
        403,
        "Malware detectado en equipo",
        "Critica",
        "Troyano"
    ),

    # Crear un incidente de tipo Acceso.
    IncidenteAcceso(
        404,
        "Intento de acceso no autorizado",
        "Alta",
        "usuario_demo",
        8
    )
]


# Mostrar el título de los reportes.
print("REPORTES DE INCIDENTES")
print("----------------------")


# Recorrer la lista y generar el reporte de cada incidente.
# Todos utilizan el mismo método, pero muestran información diferente.
for incidente in incidentes:
    print(incidente.generar_reporte())


# Indicar que la prueba terminó.
print("----------------------")
print("Prueba finalizada.")
