# Importa las clases necesarias para gestionar los incidentes.
from src.modelos.usuario import Usuario
from src.modelos.incidente import Incidente
from src.modelos.gestor_incidentes import GestorIncidentes
from src.servicios.notificador import Notificador
from src.servicios.exportador_csv import ExportadorCSV
import csv

# Programa principal.
if __name__ == "__main__":

    # Crea dos usuarios ficticios.
    usuario1 = Usuario(1, "Daniel")
    usuario2 = Usuario(2, "Laura")

    # Crea tres incidentes ficticios.
    incidente1 = Incidente(101, "Acceso sospechoso", "Alta")
    incidente2 = Incidente(102, "Alerta de seguridad", "Media")
    incidente3 = Incidente(103, "Modificacion no autorizada", "Alta")

    # Asigna responsables a los incidentes.
    incidente1.asignar_responsable(usuario1)
    incidente2.asignar_responsable(usuario2)
    incidente3.asignar_responsable(usuario1)

    # Muestra la información de los usuarios.
    print("=== USUARIOS ===")
    print(usuario1.resumen())
    print(usuario2.resumen())

    # Crea el gestor y registra los incidentes.
    gestor = GestorIncidentes()
    gestor.agregar(incidente1)
    gestor.agregar(incidente2)
    gestor.agregar(incidente3)


    # Prueba del ejercicio 7: construcción de filas.
    print("\n=== EJERCICIO 7: CONSTRUCCIÓN DE FILAS ===")

    # Guarda los datos originales para comprobar que no se modifiquen.
    originales = [
        (incidente.id, incidente.descripcion,
         incidente.gravedad, incidente.estado)
        for incidente in gestor.listar()
    ]

    # Crea el exportador y construye las filas.
    exportador = ExportadorCSV()
    filas = exportador.construir_filas(gestor.listar())

    # Muestra las filas generadas.
    for fila in filas:
        print(fila)

    # Verifica los cuatro campos y sus tipos.
    assert all(tuple(fila.keys()) == ExportadorCSV.CAMPOS for fila in filas)
    assert all(
        isinstance(fila["id"], int)
        and isinstance(fila["descripcion"], str)
        and isinstance(fila["gravedad"], str)
        and isinstance(fila["estado"], str)
        for fila in filas
    )

    # Comprueba que se conserva el orden de los incidentes.
    assert [fila["id"] for fila in filas] == [101, 102, 103]

    # Comprueba que los objetos originales no fueron modificados.
    actuales = [
        (incidente.id, incidente.descripcion,
         incidente.gravedad, incidente.estado)
        for incidente in gestor.listar()
    ]

    assert originales == actuales

    print("Verificación de cuatro campos: CORRECTA")
    print("Verificación de tipos de datos: CORRECTA")
    print("Verificación del orden: CORRECTA")
    print("Verificación de objetos originales: CORRECTA")


    # Prueba del ejercicio 8: escritura de archivos CSV.
    print("\n=== EJERCICIO 8: ESCRITURA DE CSV ===")

    # Exporta los tres incidentes registrados.
    ruta_csv = exportador.exportar(
        gestor.listar(),
        "incidentes.csv"
    )

    # Muestra la ubicación del archivo generado.
    print(f"Archivo CSV generado: {ruta_csv.resolve()}")

    # Comprueba la creación del archivo.
    assert ruta_csv.exists()

    # Comprueba que el archivo contiene los cuatro encabezados.
    with ruta_csv.open("r", encoding="utf-8-sig", newline="") as archivo:
        lector = csv.DictReader(archivo)
        assert lector.fieldnames == list(ExportadorCSV.CAMPOS)
        registros_csv = list(lector)

    # Comprueba que se exportaron los tres incidentes.
    assert len(registros_csv) == 3

    print("Verificación de archivo CSV: CORRECTA")
    print("Verificación de encabezados: CORRECTA")
    print("Verificación de registros: CORRECTA")

    # Comprueba que también se escriban encabezados sin registros.
    ruta_vacia = exportador.exportar([], "incidentes_vacio.csv")

    with ruta_vacia.open("r", encoding="utf-8-sig", newline="") as archivo:
        lector_vacio = csv.DictReader(archivo)
        assert lector_vacio.fieldnames == list(ExportadorCSV.CAMPOS)
        assert list(lector_vacio) == []

    print("Verificación de CSV sin registros: CORRECTA")


    # Prueba del ejercicio 9: integración con Clase 11.
    print("\n=== EJERCICIO 9: INCIDENTES PRIORIZADOS ===")

    # Crea un gestor independiente para esta prueba.
    gestor9 = GestorIncidentes()

    # Crea seis incidentes con diferentes prioridades.
    incidente201 = Incidente(201, "Alerta media", "Media")
    incidente202 = Incidente(202, "Amenaza critica", "Critica")
    incidente203 = Incidente(203, "Acceso sospechoso", "Alta")
    incidente204 = Incidente(204, "Incidente cerrado", "Critica")
    incidente205 = Incidente(205, "Actividad sospechosa", "Alta")
    incidente206 = Incidente(206, "Software desactualizado", "Baja")

    # Cierra el incidente 204 para comprobar que sea excluido.
    incidente204.cerrar()

    # Registra los seis incidentes.
    for incidente in [
        incidente201, incidente202, incidente203,
        incidente204, incidente205, incidente206,
    ]:
        gestor9.agregar(incidente)

    # Guarda el orden original de la colección.
    orden_original = [incidente.id for incidente in gestor9.listar()]

    # Obtiene los incidentes abiertos ordenados por prioridad.
    pendientes = gestor9.pendientes_priorizados()

    # Muestra los resultados.
    for incidente in pendientes:
        print(
            f"ID: {incidente.id} | "
            f"Gravedad: {incidente.gravedad} | "
            f"Estado: {incidente.estado}"
        )

    # Comprueba el orden de prioridades y la estabilidad de empates.
    assert [incidente.id for incidente in pendientes] == [202, 203, 205, 201, 206]

    # Comprueba que no aparezcan incidentes cerrados.
    assert all(incidente.estado == "Abierto" for incidente in pendientes)

    # Comprueba que la colección original conserve su orden.
    assert [incidente.id for incidente in gestor9.listar()] == orden_original

    # Exporta únicamente los incidentes abiertos y priorizados.
    ruta_priorizados = exportador.exportar(
        pendientes,
        "incidentes_priorizados.csv"
    )

    print("Verificación de prioridades: CORRECTA")
    print("Verificación de incidentes abiertos: CORRECTA")
    print("Verificación de empates: CORRECTA")
    print("Verificación de lista original: CORRECTA")
    print(f"CSV generado: {ruta_priorizados.resolve()}")


    # Muestra los incidentes registrados en el gestor.
    print("\n=== INCIDENTES ===")

    for incidente in gestor.listar():

        # Obtiene el nombre del responsable si existe.
        if incidente.responsable is not None:
            nombre_responsable = incidente.responsable.nombre
        else:
            nombre_responsable = "Sin asignar"

        # Muestra los datos del incidente.
        print(
            f"ID: {incidente.id} | "
            f"Descripción: {incidente.descripcion} | "
            f"Gravedad: {incidente.gravedad} | "
            f"Estado: {incidente.estado} | "
            f"Responsable: {nombre_responsable}"
        )

    # Crea el servicio encargado de enviar notificaciones.
    notificador = Notificador()

    # Cierra el primer incidente y envía una notificación.
    print("\n=== CIERRE DEL INCIDENTE ===")
    gestor.cerrar_incidente(incidente1, notificador)

    # Muestra el estado actualizado del incidente.
    print(f"Estado final del incidente {incidente1.id}: {incidente1.estado}")