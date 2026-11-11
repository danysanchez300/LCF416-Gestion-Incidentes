# Gestión de Incidentes de Ciberseguridad

## Objetivo

Proyecto académico desarrollado en Python para aplicar los conceptos de Programación Orientada a Objetos en un sistema de gestión de incidentes de ciberseguridad.

## Unidad III - Integrador

El proyecto implementa los siguientes conceptos:

### 1. Asociación: Usuario - Incidente

La clase `Incidente` mantiene una referencia opcional a un objeto `Usuario` como responsable.

Un usuario puede ser responsable de varios incidentes.

### 2. Agregación: GestorIncidentes - Incidente

La clase `GestorIncidentes` administra una colección de objetos `Incidente`.

Los incidentes pueden seguir existiendo aunque sean retirados de la colección del gestor, ya que tienen una existencia independiente.

### 3. Dependencia: GestorIncidentes - Notificador

El gestor utiliza temporalmente un objeto `Notificador` para enviar avisos cuando se cierra un incidente.

### 4. Herencia y polimorfismo

La clase `Incidente` es la clase base.

Sus clases especializadas son:

- `IncidenteAcceso`
- `IncidenteMalware`

Cada subclase sobrescribe el método `generar_reporte()` para incorporar información específica de su tipo de incidente.

## Estructura del proyecto

```text
LCF416-Gestion-Incidentes/
│
├── docs/
│   ├── 02_uml_clase7(2).pdf
│   ├── 02_uml_clase8.pdf
│   └── 02_uml_repaso.pdf
│
├── src/
│   ├── main.py
│   │
│   ├── modelos/
│   │   ├── usuario.py
│   │   ├── incidente.py
│   │   ├── gestor_incidentes.py
│   │   ├── incidente_acceso.py
│   │   ├── incidente_malware.py
│   │   ├── pruebas_agregacion.py
│   │   ├── pruebas_clasificacion.py
│   │   ├── pruebas_polimorfismo.py
│   │   └── pruebas_validaciones.py
│   │
│   └── servicios/
│       └── notificador.py
│
└── README.md
```

## Ejecución del programa

Desde la carpeta principal del proyecto, ejecutar:

```bash
python -m src.main
```

## Pruebas del proyecto

Las pruebas se ejecutan desde la carpeta principal del proyecto mediante los siguientes comandos:

### 1. Prueba de agregación

```bash
python -m src.modelos.pruebas_agregacion
```

Comprueba el registro y retiro de incidentes, la conservación de referencias externas y el rechazo de identificadores duplicados.

### 2. Prueba de clasificación

```bash
python -m src.modelos.pruebas_clasificacion
```

Comprueba la clasificación de incidentes según su gravedad.

### 3. Prueba de herencia y polimorfismo

```bash
python -m src.modelos.pruebas_polimorfismo
```

Comprueba la generación de reportes mediante la clase base y sus clases especializadas.

### 4. Prueba de validaciones

```bash
python -m src.modelos.pruebas_validaciones
```

Comprueba la validación de gravedad, el manejo de errores controlados y el rechazo de identificadores duplicados.

## Comprobaciones realizadas

- Asociación entre `Usuario` e `Incidente`.
- Agregación entre `GestorIncidentes` e `Incidente`.
- Conservación de referencias externas al retirar incidentes.
- Rechazo de identificadores duplicados.
- Clasificación de incidentes por gravedad.
- Herencia y polimorfismo en la generación de reportes.
- Cierre de incidentes y envío de notificaciones.
- Manejo de errores controlados.

## Datos de simulación

El proyecto utiliza usuarios e incidentes ficticios.

Para ejemplos de redes se puede utilizar `192.0.2.0/24`, bloque reservado para documentación.

No se utilizan datos de incidentes reales.

## Tecnologías utilizadas

- Python
- Programación Orientada a Objetos
- Git
- GitHub


## Unidad IV - Clase 11: Abstracción y ciclo de vida del software

### 1. Análisis y requisitos

Se identificó la necesidad de consultar los incidentes abiertos
y ordenarlos de acuerdo con su nivel de gravedad.

El operador utiliza esta funcionalidad para identificar
los incidentes que requieren atención prioritaria.

Los requisitos funcionales y no funcionales se encuentran
documentados en:

- `docs/requisitos_clase11.md`

### 2. Ciclo de vida del software

Se documentaron las etapas de análisis, requisitos, diseño,
implementación, pruebas, entrega y mantenimiento.

También se identificaron riesgos y se seleccionó el modelo
iterativo para continuar mejorando el proyecto.

Documento:

- `docs/ciclo_vida_clase11.md`

### 3. Consulta de incidentes pendientes

Se agregó el método `pendientes_priorizados()` a la clase
`GestorIncidentes`.

Esta funcionalidad:

- Consulta únicamente incidentes abiertos.
- Ordena por gravedad: Crítica, Alta, Media y Baja.
- Conserva el orden de registro cuando existen empates.
- Devuelve una lista nueva sin modificar la colección original.

### 4. Pruebas de Clase 11

Las pruebas se ejecutan desde la carpeta principal del proyecto.

**Prueba de priorización:**

```bash
python -m src.modelos.pruebas_priorizacion
```

**Pruebas de validación:**

```bash
python -m src.modelos.pruebas_clase11
```

Se comprobaron seis casos: orden de prioridad, exclusión de
incidentes cerrados, lista vacía, empate estable, conservación
de la lista original y rechazo de gravedad inválida.

### 5. Control de versiones

Los cambios de la Clase 11 se trabajan en la rama:

`feature/requisitos-ciclo-vida`

La documentación y las modificaciones del sistema se registran
mediante Git y se preparan para su revisión mediante un
Pull Request en GitHub.
