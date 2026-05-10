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
|- docs/
|  |- analisis_diseno.md
|  |- guia_video.md
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

## Documentacion

- Documento principal: `README.md`
- Analisis de diseno: `docs/analisis_diseno.md`
- Guia de sustentacion: `docs/guia_video.md`

## Evidencias

> Nota: se deja preparada la seccion para adjuntar capturas cuando esten disponibles.
> Ruta actual de imagenes: `evidencias/`.

### Evidencia 1 - Git

- Mostrar ramas locales y remotas con `git branch -a`.
- Confirmar rama activa `dev_ltuiran07` con `git status`.

![Evidencia 1 - Git](evidencias/01%20GIT.jpg)

### Evidencia 2 - Estructura del proyecto

- Mostrar arbol del proyecto segun la seccion de estructura.

![Evidencia 2 - Estructura del proyecto](evidencias/02%20Estructura%20del%20proyecto.jpg)

### Evidencia 3 - Instalacion de dependencias

- Ejecutar `pip install -r requirements.txt` sin errores.

![Evidencia 3 - Instalacion de dependencias](evidencias/03%20Instalacion%20de%20dependencias.jpg)

### Evidencia 4 - Pruebas unitarias

- Ejecutar `pytest -q`.
- Resultado esperado: `12 passed`.

![Evidencia 4 - Pruebas unitarias](evidencias/04%20Pruebas%20Unitarias.jpg)

### Evidencia 5 - Ejecucion del programa

- Ejecutar `python -m app.main`.
- Mostrar huella por objeto, total y datos leidos desde JSON.

![Evidencia 5 - Ejecucion del programa](evidencias/05%20Ejecucion%20del%20programa.jpg)

### Evidencia 6 - Archivo generado

- Verificar creacion de `data/huella_carbono.json`.

![Evidencia 6-0 - Archivo generado](evidencias/06-0%20archivo%20generado.jpg)

![Evidencia 6-1 - Archivo generado](evidencias/06-1%20archivo%20generado.jpg)

### Evidencia 7 - Codigo fuente clave

- Interfaz: `modelo/calculable_huella_carbono.py`.
- Clases de dominio: `modelo/edificio.py`, `modelo/automovil.py`, `modelo/bicicleta.py`.
- Persistencia: `persistencia/repositorio_huella_json.py`.
- Main y polimorfismo: `app/main.py`.

![Evidencia 7-0 - Codigo fuente clave](evidencias/07-0%20Codigo%20Fuente%20Clave.jpg)

![Evidencia 7-1 - Codigo fuente clave](evidencias/07-1%20Codigo%20Fuente%20Clave.jpg)

![Evidencia 7-2 - Codigo fuente clave](evidencias/07-2%20Codigo%20Fuente%20Clave.jpg)

![Evidencia 7-3 - Codigo fuente clave](evidencias/07-3%20Codigo%20Fuente%20Clave.jpg)

![Evidencia 7-4 - Codigo fuente clave](evidencias/07-4%20Codigo%20Fuente%20Clave.jpg)

![Evidencia 7-5 - Codigo fuente clave](evidencias/07-5%20Codigo%20Fuente%20Clave.jpg)

### Evidencia 8 - Documentacion

- README completo en `README.md`.
- Analisis de diseno en `docs/analisis_diseno.md`.
- Guia de video en `docs/guia_video.md`.

![Evidencia 8-0 - Documentacion](evidencias/08-0%20documentacion.jpg)

![Evidencia 8-1 - Documentacion](evidencias/08-1%20documentacion.jpg)

![Evidencia 8-2 - Documentacion](evidencias/08-2%20documentacion.jpg)
