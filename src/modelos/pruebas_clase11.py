# Importa las clases necesarias para realizar las pruebas.
from .incidente import Incidente
from .gestor_incidentes import GestorIncidentes


# PRUEBA 1: verificar que los incidentes se ordenen por gravedad.
def probar_orden_prioridad():
    gestor = GestorIncidentes()

    # Registra incidentes con diferentes niveles de gravedad.
    gestor.agregar(Incidente("I-101", "Incidente medio", "Media"))
    gestor.agregar(Incidente("I-102", "Incidente crítico", "Critica"))
    gestor.agregar(Incidente("I-103", "Incidente bajo", "Baja"))
    gestor.agregar(Incidente("I-104", "Incidente alto", "Alta"))

    # Consulta los incidentes y obtiene sus identificadores.
    resultado = gestor.pendientes_priorizados()
    observado = [incidente.id for incidente in resultado]

    # Define el orden correcto que se espera obtener.
    esperado = ["I-102", "I-104", "I-101", "I-103"]

    # Compara el resultado obtenido con el esperado.
    assert observado == esperado
    print("PRUEBA 1: Orden de prioridad - CORRECTA")


# PRUEBA 2: verificar que los incidentes cerrados no aparezcan.
def probar_exclusion_cerrados():
    gestor = GestorIncidentes()

    # Crea un incidente abierto y otro que será cerrado.
    abierto = Incidente("I-201", "Incidente abierto", "Alta")
    cerrado = Incidente("I-202", "Incidente cerrado", "Critica")

    cerrado.cerrar()  # Cambia el estado del incidente a Cerrado.

    gestor.agregar(abierto)
    gestor.agregar(cerrado)

    # Consulta únicamente los incidentes pendientes.
    resultado = gestor.pendientes_priorizados()
    observado = [incidente.id for incidente in resultado]

    # Comprueba que solamente aparezca el incidente abierto.
    assert observado == ["I-201"]
    print("PRUEBA 2: Exclusión de cerrados - CORRECTA")


# PRUEBA 3: verificar el resultado cuando no existen incidentes.
def probar_lista_vacia():
    gestor = GestorIncidentes()

    # Consulta el gestor sin haber agregado incidentes.
    resultado = gestor.pendientes_priorizados()

    # Comprueba que la consulta devuelva una lista vacía.
    assert resultado == []
    print("PRUEBA 3: Lista vacía - CORRECTA")


# PRUEBA 4: verificar que se respete el orden cuando hay empates.
def probar_empate_estable():
    gestor = GestorIncidentes()

    # Registra tres incidentes Alta y uno Crítica.
    gestor.agregar(Incidente("I-301", "Incidente alto 1", "Alta"))
    gestor.agregar(Incidente("I-302", "Incidente alto 2", "Alta"))
    gestor.agregar(Incidente("I-303", "Incidente crítico", "Critica"))
    gestor.agregar(Incidente("I-304", "Incidente alto 3", "Alta"))

    # Obtiene los incidentes ordenados por prioridad.
    resultado = gestor.pendientes_priorizados()
    observado = [incidente.id for incidente in resultado]

    # La prioridad cambia, pero los empates conservan su orden original.
    esperado = ["I-303", "I-301", "I-302", "I-304"]

    assert observado == esperado
    print("PRUEBA 4: Empate estable - CORRECTA")


# PRUEBA 5: verificar que la consulta no modifique la lista original.
def probar_lista_original():
    gestor = GestorIncidentes()

    # Agrega incidentes en un orden diferente al de prioridad.
    gestor.agregar(Incidente("I-401", "Incidente medio", "Media"))
    gestor.agregar(Incidente("I-402", "Incidente crítico", "Critica"))
    gestor.agregar(Incidente("I-403", "Incidente alto", "Alta"))

    # Guarda el orden original antes de realizar la consulta.
    orden_original = [x.id for x in gestor.listar()]

    # Ejecuta la consulta de incidentes pendientes.
    gestor.pendientes_priorizados()

    # Obtiene nuevamente el orden de la colección original.
    orden_final = [x.id for x in gestor.listar()]

    # Comprueba que el orden original permanezca sin cambios.
    assert orden_original == orden_final
    print("PRUEBA 5: Lista original conservada - CORRECTA")


# PRUEBA 6: verificar que se rechacen gravedades no permitidas.
def probar_gravedad_invalida():
    try:
        # Intenta crear un incidente con una gravedad no válida.
        Incidente("I-501", "Incidente inválido", "Urgente")

    except ValueError:
        # Confirma que la validación rechazó el dato.
        print("PRUEBA 6: Gravedad inválida rechazada - CORRECTA")

    else:
        # Genera un error si se acepta la gravedad incorrecta.
        raise AssertionError("Se aceptó una gravedad no permitida.")


# Ejecuta las seis pruebas al iniciar este archivo.
if __name__ == "__main__":
    probar_orden_prioridad()
    probar_exclusion_cerrados()
    probar_lista_vacia()
    probar_empate_estable()
    probar_lista_original()
    probar_gravedad_invalida()

    print("\nTODAS LAS PRUEBAS FINALIZARON CORRECTAMENTE.")
