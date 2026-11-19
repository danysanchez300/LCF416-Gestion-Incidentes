# Módulo para escribir archivos CSV.
import csv

# Clase para trabajar con rutas y archivos.
from pathlib import Path

# Importamos la clase Incidente para identificar los objetos recibidos.
from src.modelos.incidente import Incidente

# Clase encargada de preparar la información para exportarla a CSV.
class ExportadorCSV:

    # Define los cuatro campos que tendrá cada fila.
    CAMPOS = ("id", "descripcion", "gravedad", "estado")

    # Convierte una lista de incidentes en una lista de diccionarios.
    def construir_filas(self, incidentes):

        # Verifica que se reciba una lista.
        if not isinstance(incidentes, list):
            raise TypeError("Se esperaba una lista de incidentes")

        # Aquí almacenaremos las filas construidas.
        filas = []

        # Recorremos los incidentes respetando su orden original.
        for incidente in incidentes:

            # Verifica que cada elemento sea un objeto Incidente.
            if not isinstance(incidente, Incidente):
                raise TypeError("Todos los elementos deben ser objetos Incidente")

            # Construimos un diccionario con los cuatro campos.
            fila = {
                "id": incidente.id,
                "descripcion": incidente.descripcion,
                "gravedad": incidente.gravedad,
                "estado": incidente.estado
            }

            # Agregamos la fila a la lista de resultados.
            filas.append(fila)

        # Devolvemos la lista sin modificar los incidentes originales.
        return filas


    # Exporta los incidentes a un archivo CSV.
    def exportar(self, incidentes, destino):

        # Convierte los incidentes en filas de diccionarios.
        filas = self.construir_filas(incidentes)

        # Convierte el destino en una ruta de archivo.
        ruta = Path(destino)

        # Abre el archivo para escritura con codificación UTF-8.
        with ruta.open("w", newline="", encoding="utf-8-sig") as archivo:

            # Crea el escritor CSV utilizando los cuatro campos.
            escritor = csv.DictWriter(
                archivo,
                fieldnames=self.CAMPOS
            )

            # Escribe los encabezados, incluso si no hay registros.
            escritor.writeheader()

            # Escribe los datos de los incidentes.
            escritor.writerows(filas)

        # Devuelve la ruta del archivo generado.
        return ruta
