
# Importa las clases necesarias para realizar las pruebas.
from src.modelos.incidente import Incidente
from src.modelos.gestor_incidentes import GestorIncidentes


# Punto de inicio de las pruebas.
if __name__ == "__main__":

    # PRUEBA 1: Crear un incidente con gravedad válida.
    print("--- PRUEBA DE GRAVEDAD VÁLIDA ---")

    incidente1 = Incidente(501, "Acceso sospechoso", "Alta")
    print(f"Incidente creado correctamente: {incidente1.gravedad}")

    # PRUEBA 2: Intentar utilizar una gravedad no permitida.
    print("\n--- PRUEBA DE ERROR EN GRAVEDAD ---")

    try:
        incidente2 = Incidente(502, "Alerta de seguridad", "Urgente")

    except ValueError as error:
        print(f"Error controlado: {error}")

    # PRUEBA 3: Intentar registrar dos incidentes con el mismo ID.
    print("\n--- PRUEBA DE ID DUPLICADO ---")

    gestor = GestorIncidentes()

    incidente3 = Incidente(503, "Malware detectado", "Critica")
    incidente4 = Incidente(503, "Acceso no autorizado", "Media")

    # Registra correctamente el primer incidente.
    gestor.agregar(incidente3)
    print("Primer incidente registrado correctamente")

    try:
        # Intenta registrar el segundo incidente con el mismo ID.
        gestor.agregar(incidente4)

    except ValueError as error:
        print(f"Error controlado: {error}")

    # Comprueba que el primer incidente sigue registrado.
    print(f"Incidentes registrados: {len(gestor.listar())}")
