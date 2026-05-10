# Guia de video

## Objetivo de la sustentacion

Demostrar que el proyecto **Carbon Footprint Python** cumple la Actividad 5 mediante:

- Programacion orientada a objetos.
- Interfaz comun para clases no relacionadas por herencia.
- Polimorfismo aplicado en el flujo principal.
- Persistencia de datos en archivo **JSON**.
- Pruebas unitarias automatizadas.
- Estrategia de ramas Git solicitada (`main` -> `develop` -> `dev_ltuiran07`).

## Duracion sugerida

6 a 9 minutos.

## Problema que resuelve el proyecto

Se requiere modelar objetos del mundo real que generan huella de carbono con formulas diferentes, sin acoplar la logica principal a tipos concretos.

El problema se resuelve definiendo un contrato comun (`CalculableHuellaCarbono`) e implementando tres clases del dominio:

- `Edificio`
- `Automovil`
- `Bicicleta`

Con este enfoque se calcula la huella de forma uniforme, se persisten resultados en JSON y se valida el comportamiento con pruebas unitarias.

## Diseno de la solucion

Arquitectura modular por responsabilidades:

- `modelo`: entidades y la interfaz del dominio.
- `servicio`: operaciones de negocio (reporte y total).
- `persistencia`: guardar y leer informacion en JSON.
- `app`: orquestacion del flujo de ejecucion.
- `prueba`: validacion automatizada con `pytest`.

Beneficios del diseno:

- Facil mantenimiento y extension.
- Bajo acoplamiento entre capas.
- Cumplimiento de SRP y DIP.

## Clases e interfaz implementadas

### Interfaz comun

Archivo: `modelo/calculable_huella_carbono.py`

Define el contrato:

- `calcular_huella_carbono() -> float`
- `a_dict() -> dict`

### Clases del dominio

1. `Edificio` (`modelo/edificio.py`)
   - Atributos: `nombre`, `consumo_energia_mensual`, `factor_emision`
   - Formula: `consumo_energia_mensual * factor_emision`

2. `Automovil` (`modelo/automovil.py`)
   - Atributos: `placa`, `kilometros_recorridos`, `consumo_por_kilometro`, `factor_emision`
   - Formula: `kilometros_recorridos * consumo_por_kilometro * factor_emision`

3. `Bicicleta` (`modelo/bicicleta.py`)
   - Atributos: `marca`, `kilometros_recorridos`, `factor_emision_indirecta`
   - Formula: `kilometros_recorridos * factor_emision_indirecta`

Todas incluyen validaciones para evitar valores negativos.

## Polimorfismo aplicado

Archivo: `app/main.py` y `servicio/servicio_huella_carbono.py`

Se crea una lista tipada por la abstraccion (`CalculableHuellaCarbono`) con instancias de diferentes clases.
Luego el servicio recorre la lista y ejecuta `calcular_huella_carbono()` sin preguntar el tipo concreto.

Esto demuestra:

- Sustitucion de Liskov.
- Apertura para agregar nuevos tipos (OCP).
- Dependencia de abstracciones (DIP).

## Persistencia en archivo JSON

Archivo: `persistencia/repositorio_huella_json.py`

Flujo de persistencia:

1. `guardar(objetos)` serializa cada objeto con `a_dict()`.
2. Se escribe la lista en `data/huella_carbono.json`.
3. `leer()` carga el JSON y reconstruye objetos por campo `tipo`.

Justificacion de JSON:

- Es legible para evidencia academica.
- Conserva estructura de datos por objeto.
- Facilita validacion y trazabilidad de resultados.

## Pruebas unitarias

Archivo: `prueba/test_huella_carbono.py`

Cobertura implementada:

- Calculo de huella por cada clase.
- Casos borde (por ejemplo valores en cero).
- Validaciones de datos invalidos (negativos).
- Reporte y total del servicio.
- Guardado y lectura en JSON.
- Manejo de tipo no soportado en deserializacion.

Resultado esperado:

- `12 passed`.

## Guion recomendado para grabacion

### 1) Introduccion (30-45 segundos)

- Presentar proyecto y objetivo.
- Explicar brevemente el problema de negocio.

### 2) Estrategia de ramas Git (45-60 segundos)

Mostrar en terminal:

```bash
git branch
git branch -a
git status
```

Explicar flujo exigido: `main` -> `develop` -> `dev_ltuiran07`.

### 3) Estructura del proyecto (45-60 segundos)

Recorrer carpetas:

- `app`
- `modelo`
- `servicio`
- `persistencia`
- `prueba`
- `data`
- `docs`

### 4) Codigo fuente clave (1.5-2 minutos)

Mostrar en este orden:

1. `modelo/calculable_huella_carbono.py`.
2. `modelo/edificio.py`, `modelo/automovil.py`, `modelo/bicicleta.py`.
3. `servicio/servicio_huella_carbono.py`.
4. `persistencia/repositorio_huella_json.py`.
5. `app/main.py`.

### 5) Pruebas unitarias (45-60 segundos)

```bash
pytest -q
```

Mencionar el resultado obtenido (`12 passed`).

### 6) Ejecucion del programa (45-60 segundos)

```bash
python -m app.main
```

Mostrar salida por objeto, total y lectura desde JSON.

### 7) Validacion de archivo JSON (20-30 segundos)

```bash
type data\huella_carbono.json
```

### 8) Cierre (20-30 segundos)

- Confirmar cumplimiento de POO, SOLID, polimorfismo, JSON y pruebas.
- Referenciar documentacion: `README.md` y `docs/analisis_diseno.md`.

## Checklist de evidencias 1..8

- [ ] Evidencia 1 - Git
- [ ] Evidencia 2 - Estructura del proyecto
- [ ] Evidencia 3 - Instalacion de dependencias
- [ ] Evidencia 4 - Pruebas unitarias
- [ ] Evidencia 5 - Ejecucion del programa
- [ ] Evidencia 6 - Archivo generado
- [ ] Evidencia 7 - Codigo fuente clave
- [ ] Evidencia 8 - Documentacion
