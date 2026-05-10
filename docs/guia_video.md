# Guia de video

## Objetivo de la sustentacion

Demostrar que el proyecto Python cumple la Actividad 5 en POO, polimorfismo, persistencia, pruebas y estrategia de ramas Git.

## Duracion sugerida

5 a 8 minutos.

## Guion recomendado

## 1) Introduccion (30-45 segundos)

- Nombre del proyecto y objetivo.
- Resumen de objetos modelados: `Edificio`, `Automovil`, `Bicicleta`.

## 2) Estrategia de ramas Git (45-60 segundos)

Mostrar en terminal:

```bash
git branch
git branch -a
git status
```

Explicar flujo requerido: `main` -> `develop` -> `dev_ltuiran07`.

## 3) Estructura del proyecto (45-60 segundos)

Recorrer carpetas:

- `app`
- `modelo`
- `servicio`
- `persistencia`
- `prueba`
- `data`
- `docs`

## 4) Codigo fuente clave (1.5-2 minutos)

Mostrar rapidamente:

1. `modelo/calculable_huella_carbono.py` (contrato comun).
2. `modelo/edificio.py`, `modelo/automovil.py`, `modelo/bicicleta.py` (formulas).
3. `servicio/servicio_huella_carbono.py` (polimorfismo).
4. `persistencia/repositorio_huella_json.py` (guardar/leer JSON).
5. `app/main.py` (flujo principal).

## 5) Ejecucion de pruebas (45-60 segundos)

```bash
pytest -q
```

Confirmar resultado: `12 passed`.

## 6) Ejecucion del programa (45-60 segundos)

```bash
python -m app.main
```

Mostrar salida por objeto, total y lectura del JSON.

## 7) Evidencia de archivo generado (20-30 segundos)

```bash
type data\huella_carbono.json
```

## 8) Cierre (20-30 segundos)

- Confirmar cumplimiento de POO, SOLID, JSON, pruebas y ramas.
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
