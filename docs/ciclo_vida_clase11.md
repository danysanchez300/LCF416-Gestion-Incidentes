
# Ciclo de Vida del Software - Clase 11

## 1. Descripción del proyecto

El proyecto consiste en un Sistema de Gestión de Incidentes
de Ciberseguridad desarrollado en Python mediante programación
orientada a objetos.

En esta etapa se incorpora una consulta que permite identificar
y ordenar los incidentes abiertos según su nivel de gravedad.

## 2. Etapas del ciclo de vida

| Etapa | Actividad realizada | Responsable simulado | Evidencia |
|---|---|---|---|
| Análisis | Identificar la necesidad de priorizar incidentes abiertos. | Analista | Análisis de necesidades. |
| Requisitos | Definir los requisitos funcionales y no funcionales. | Analista de sistemas | requisitos_clase11.md |
| Diseño | Determinar la responsabilidad de GestorIncidentes y su relación con Incidente. | Diseñador | Diagrama UML. |
| Implementación | Incorporar el método pendientes_priorizados() utilizando sorted(). | Desarrollador | gestor_incidentes.py |
| Pruebas | Verificar el orden, la exclusión de cerrados, los empates y la conservación de la lista original. | Tester | pruebas_clase11.py |
| Entrega | Registrar los cambios y preparar el Pull Request en GitHub. | Desarrollador | Commits y Pull Request. |
| Mantenimiento | Corregir errores y realizar mejoras futuras al sistema. | Mantenedor | Registro de cambios. |

## 3. Riesgos identificados

| Riesgo | Consecuencia | Medida de prevención |
|---|---|---|
| Incluir incidentes cerrados. | Mostrar información que no requiere atención. | Filtrar por estado Abierto. |
| Ordenar incorrectamente las gravedades. | Atender incidentes menos urgentes primero. | Definir niveles de prioridad. |
| Modificar la lista original. | Alterar el registro de incidentes. | Utilizar sorted() para crear una lista nueva. |
| No conservar el orden en empates. | Cambiar el orden de registro de incidentes. | Utilizar una ordenación estable. |

## 4. Comparación de modelos de desarrollo

### Modelo secuencial

Consiste en desarrollar el proyecto mediante etapas ordenadas,
donde cada etapa debe completarse antes de iniciar la siguiente.

Su ventaja es que permite organizar y documentar el trabajo.
Su desventaja es que los cambios pueden ser más difíciles de incorporar
cuando una etapa ya fue terminada.

### Modelo iterativo

Consiste en desarrollar el sistema mediante ciclos de trabajo,
permitiendo probar, revisar y mejorar las funcionalidades.

Su ventaja es que facilita detectar errores y realizar ajustes
durante el desarrollo.

## 5. Modelo seleccionado

Se seleccionó el modelo iterativo porque permite incorporar
nuevas funcionalidades al sistema existente, realizar pruebas
y corregir errores sin tener que desarrollar nuevamente
todo el proyecto.

## 6. Conclusión

El ciclo de vida del software permitió organizar el desarrollo
de la consulta de incidentes pendientes, desde el análisis
de necesidades hasta las pruebas y la entrega.

La aplicación de este proceso ayuda a mantener el proyecto
ordenado, documentado y preparado para futuras mejoras.
