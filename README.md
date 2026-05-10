# Carbon Footprint Python

Proyecto academico en Python para modelar objetos con huella de carbono mediante clases no relacionadas por herencia (`Edificio`, `Automovil` y `Bicicleta`) que implementan una interfaz comun (`CalculableHuellaCarbono`).

## Caso de estudio

Se modelan tres tipos de objetos del mundo real que generan impacto ambiental de formas distintas:

- `Edificio`: huella por consumo de energia mensual y factor de emision.
- `Automovil`: huella por kilometros recorridos, consumo por kilometro y factor de emision.
- `Bicicleta`: huella indirecta por kilometros recorridos y factor de emision indirecta.

La integracion se hace mediante una interfaz compartida para habilitar polimorfismo y cumplir el enunciado de clases no relacionadas entre si por herencia.

## Conceptos aplicados

- **Interfaz:** `CalculableHuellaCarbono` define el contrato comun (`calcular_huella_carbono`, `a_dict`).
- **Polimorfismo:** una lista de `CalculableHuellaCarbono` contiene objetos de distintos tipos.
- **Modularidad:** separacion por paquetes `modelo`, `servicio`, `persistencia`, `app`, `prueba`.
- **Reutilizacion:** `RepositorioHuellaJSON` sirve para cualquier objeto que implemente la interfaz.
- **Manejo de archivos:** escritura y lectura en `data/huella_carbono.json`.
- **Pruebas unitarias:** pruebas con `pytest` por clase, servicio y persistencia.
- **SOLID:**
  - `SRP`: cada modulo tiene una responsabilidad clara.
  - `OCP`: se pueden agregar nuevas fuentes sin romper la logica central.
  - `LSP`: todas las clases implementadoras son sustituibles por la interfaz.
  - `ISP`: interfaz pequena con solo lo necesario.
  - `DIP`: flujo principal depende de la abstraccion.

## Estructura del proyecto

```text
CarbonFootprintPython/
|- README.md
|- requirements.txt
|- .gitignore
|- pytest.ini
|- data/
|  |- huella_carbono.json
|- app/
|  |- __init__.py
|  |- main.py
|- modelo/
|  |- __init__.py
|  |- calculable_huella_carbono.py
|  |- edificio.py
|  |- automovil.py
|  |- bicicleta.py
|- servicio/
|  |- __init__.py
|  |- servicio_huella_carbono.py
|- persistencia/
|  |- __init__.py
|  |- repositorio_huella_json.py
|- prueba/
   |- test_huella_carbono.py
```

## Ejecucion

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar pruebas:

```bash
pytest -q
```

Ejecutar aplicacion:

```bash
python -m app.main
```

Verificar archivo generado:

```bash
type data\huella_carbono.json
```

## Estrategia de ramas Git

Ramas requeridas y flujo:

- `main`: rama principal del repositorio.
- `develop`: rama de integracion.
- `dev_ltuiran07`: rama final de trabajo y entrega de codigo.

Comandos de verificacion sugeridos:

```bash
git branch
git branch -a
git status
```

## Evidencias

> Nota: se deja preparada la seccion para adjuntar capturas cuando esten disponibles.
> Ruta sugerida para imagenes: `docs/evidencias/`.

### Evidencia 1 - Git

- Mostrar ramas locales y remotas con `git branch -a`.
- Confirmar rama activa `dev_ltuiran07` con `git status`.
- Imagen pendiente: `docs/evidencias/01-git.png`

### Evidencia 2 - Estructura del proyecto

- Mostrar arbol del proyecto segun la seccion de estructura.
- Imagen pendiente: `docs/evidencias/02-estructura-proyecto.png`

### Evidencia 3 - Instalacion de dependencias

- Ejecutar `pip install -r requirements.txt` sin errores.
- Imagen pendiente: `docs/evidencias/03-instalacion-dependencias.png`

### Evidencia 4 - Pruebas unitarias

- Ejecutar `pytest -q`.
- Resultado esperado: `12 passed`.
- Imagen pendiente: `docs/evidencias/04-pruebas-unitarias.png`

### Evidencia 5 - Ejecucion del programa

- Ejecutar `python -m app.main`.
- Mostrar huella por objeto, total y datos leidos desde JSON.
- Imagen pendiente: `docs/evidencias/05-ejecucion-programa.png`

### Evidencia 6 - Archivo generado

- Verificar creacion de `data/huella_carbono.json`.
- Imagen pendiente: `docs/evidencias/06-archivo-generado.png`

### Evidencia 7 - Codigo fuente clave

- Interfaz: `modelo/calculable_huella_carbono.py`.
- Clases de dominio: `modelo/edificio.py`, `modelo/automovil.py`, `modelo/bicicleta.py`.
- Persistencia: `persistencia/repositorio_huella_json.py`.
- Main y polimorfismo: `app/main.py`.
- Imagen pendiente: `docs/evidencias/07-codigo-fuente-clave.png`

### Evidencia 8 - Documentacion

- README completo en `README.md`.
- Imagen pendiente: `docs/evidencias/08-documentacion.png`
