
# Pruebas de aceptación del Sistema de Gestión de Incidentes.

import csv
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from src.modelos.incidente import Incidente
from src.modelos.gestor_incidentes import GestorIncidentes
from src.servicios.exportador_csv import ExportadorCSV


class PruebasAceptacion(unittest.TestCase):

    # Crea un gestor con incidentes ficticios para las pruebas.
    def crear_gestor(self):
        gestor = GestorIncidentes()

        incidentes = [
            Incidente(301, "Alerta media", "Media"),
            Incidente(302, "Amenaza crítica", "Critica"),
            Incidente(303, "Acceso sospechoso", "Alta"),
            Incidente(304, "Incidente cerrado", "Critica"),
            Incidente(305, "Actividad sospechosa", "Alta"),
            Incidente(306, "Alerta baja", "Baja")
        ]

        # Cierra dos incidentes para comprobar el filtrado.
        incidentes[3].cerrar()
        incidentes[5].cerrar()

        for incidente in incidentes:
            gestor.agregar(incidente)

        return gestor

    # Prueba 1: solamente deben aparecer incidentes abiertos.
    def test_filtrado(self):
        gestor = self.crear_gestor()

        pendientes = gestor.pendientes_priorizados()

        self.assertTrue(
            all(i.estado == "Abierto" for i in pendientes)
        )

        self.assertEqual(
            [i.id for i in pendientes],
            [302, 303, 305, 301]
        )

    # Prueba 2: verifica el orden de prioridades.
    def test_prioridad(self):
        gestor = self.crear_gestor()

        pendientes = gestor.pendientes_priorizados()

        gravedades = [i.gravedad for i in pendientes]

        self.assertEqual(
            gravedades,
            ["Critica", "Alta", "Alta", "Media"]
        )

    # Prueba 3: los empates conservan el orden de registro.
    def test_orden_estable(self):
        gestor = self.crear_gestor()

        pendientes = gestor.pendientes_priorizados()

        ids_alta = [
            i.id for i in pendientes
            if i.gravedad == "Alta"
        ]

        self.assertEqual(ids_alta, [303, 305])

    # Prueba 4: un gestor vacío debe devolver una lista vacía.
    def test_lista_vacia(self):
        gestor = GestorIncidentes()

        pendientes = gestor.pendientes_priorizados()

        self.assertEqual(pendientes, [])
        self.assertIsInstance(pendientes, list)

    # Prueba 5: verifica que los acentos se conserven en el CSV.
    def test_acentos(self):
        incidente = Incidente(
            307,
            "Actividad crítica: información de seguridad",
            "Critica"
        )

        exportador = ExportadorCSV()

        with TemporaryDirectory() as carpeta:
            ruta = Path(carpeta) / "prueba_acentos.csv"

            exportador.exportar([incidente], ruta)

            with ruta.open(
                "r",
                newline="",
                encoding="utf-8-sig"
            ) as archivo:
                lector = csv.DictReader(archivo)
                filas = list(lector)

        self.assertEqual(
            filas[0]["descripcion"],
            "Actividad crítica: información de seguridad"
        )


            # Prueba adicional: conserva las comas dentro de las descripciones.
    def test_comas_en_csv(self):
        incidente = Incidente(
            308,
            "Acceso sospechoso, requiere investigación",
            "Alta"
        )

        exportador = ExportadorCSV()

        with TemporaryDirectory() as carpeta:
            ruta = Path(carpeta) / "prueba_comas.csv"

            exportador.exportar([incidente], ruta)

            with ruta.open(
                "r",
                newline="",
                encoding="utf-8-sig"
            ) as archivo:
                lector = csv.DictReader(archivo)
                filas = list(lector)

        self.assertEqual(len(filas), 1)
        self.assertEqual(
            filas[0]["descripcion"],
            "Acceso sospechoso, requiere investigación"
        )

    # Prueba 6: la consulta no debe modificar la lista original.
    def test_no_mutacion(self):
        gestor = self.crear_gestor()

        originales = gestor.listar()
        orden_original = [i.id for i in originales]
        estados_originales = [i.estado for i in originales]

        pendientes = gestor.pendientes_priorizados()

        # Comprueba que se devuelva una lista diferente.
        self.assertIsNot(pendientes, originales)

        # Comprueba que no cambie el orden de la lista interna.
        self.assertEqual(
            [i.id for i in gestor.listar()],
            orden_original
        )

        # Comprueba que no cambien los estados originales.
        self.assertEqual(
            [i.estado for i in gestor.listar()],
            estados_originales
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
