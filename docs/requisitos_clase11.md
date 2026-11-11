
# Requisitos del Sistema - Clase 11

## 1. Necesidad del sistema

El sistema de gestión de incidentes de ciberseguridad necesita
consultar los incidentes que se encuentran abiertos y ordenarlos
de acuerdo con su nivel de gravedad, para facilitar la atención
de los casos más importantes.

## 2. Actor principal

**Operador:** necesita consultar los incidentes pendientes
para identificar cuáles requieren atención prioritaria.

## 3. Alcance

La funcionalidad permite consultar los incidentes abiertos,
ordenarlos desde gravedad Crítica hasta Baja y conservar
el orden de registro cuando existen incidentes con la misma gravedad.

La consulta no modifica la colección original de incidentes.

## 4. Requisitos funcionales

| ID | Requisito |
|---|---|
| RF-01 | El sistema debe permitir registrar incidentes con folio, gravedad y estado. |
| RF-02 | El sistema debe permitir consultar los incidentes registrados. |
| RF-03 | El sistema debe mostrar únicamente los incidentes con estado Abierto en la consulta de pendientes. |
| RF-04 | El sistema debe ordenar los incidentes por gravedad: Crítica, Alta, Media y Baja, conservando el orden original en caso de empate. |

## 5. Requisitos no funcionales

| ID | Requisito |
|---|---|
| RNF-01 | La consulta debe conservar sin modificaciones la colección original de incidentes. |
| RNF-02 | La consulta debe devolver una lista nueva con los incidentes pendientes priorizados. |

## 6. Criterios de aceptación

- Los incidentes Críticos deben aparecer antes que los de gravedad Alta.
- Los incidentes Alta deben aparecer antes que los de gravedad Media.
- Los incidentes Media deben aparecer antes que los de gravedad Baja.
- Los incidentes Cerrados deben quedar excluidos.
- Los incidentes con la misma gravedad deben conservar su orden de registro.
- Una colección vacía debe producir una lista vacía.
- La consulta no debe modificar la colección original.
- El sistema debe rechazar gravedades no permitidas.
