# Importa las clases necesarias para gestionar los incidentes.
from modelos.usuario import Usuario
from modelos.incidente import Incidente
from servicios.notificador import Notificador


# Clase GestorIncidentes: coordina las operaciones sobre los incidentes.
class GestorIncidentes:

    # Cierra un incidente y utiliza temporalmente un notificador.
    def cerrar_incidente(self, incidente, notificador):
        incidente.cerrar()          # Cambia el estado del incidente a Cerrado.
        notificador.enviar(incidente)  # Notifica el cierre del incidente.


# Programa principal.
if __name__ == "__main__":

    # Crear dos usuarios ficticios.
    usuario1 = Usuario(1, "Daniel")
    usuario2 = Usuario(2, "Laura")

    # Crear tres incidentes ficticios.
    incidente1 = Incidente(101, "Acceso sospechoso", "Alta")
    incidente2 = Incidente(102, "Alerta de seguridad", "Media")
    incidente3 = Incidente(103, "Modificacion no autorizada", "Alta")

    # Asignar responsables a los incidentes.
    incidente1.asignar_responsable(usuario1)
    incidente2.asignar_responsable(usuario2)
    incidente3.asignar_responsable(usuario1)

    # Mostrar información de los usuarios.
    print("=== USUARIOS ===")
    print(usuario1.resumen())
    print(usuario2.resumen())

    # Mostrar información de los incidentes.
    print("\n=== INCIDENTES ===")

    for incidente in [incidente1, incidente2, incidente3]:
        if incidente.responsable is not None:
            nombre_responsable = incidente.responsable.nombre
        else:
            nombre_responsable = "Sin asignar"

        print(
            f"ID: {incidente.id} | "
            f"Descripción: {incidente.descripcion} | "
            f"Gravedad: {incidente.gravedad} | "
            f"Estado: {incidente.estado} | "
            f"Responsable: {nombre_responsable}"
        )

    # Crear el gestor y el notificador.
    gestor = GestorIncidentes()
    notificador = Notificador()

    # Cerrar el primer incidente y notificar la operación.
    print("\n=== CIERRE DEL INCIDENTE ===")
    gestor.cerrar_incidente(incidente1, notificador)

    # Mostrar el estado actualizado del incidente.
    print(f"Estado final del incidente {incidente1.id}: {incidente1.estado}")