# Importa las clases necesarias para gestionar los incidentes.
from src.modelos.usuario import Usuario
from src.modelos.incidente import Incidente
from src.modelos.gestor_incidentes import GestorIncidentes
from src.servicios.notificador import Notificador

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