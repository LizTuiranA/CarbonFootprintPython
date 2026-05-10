# Actividad 5 - Huella de Carbono (Python)

Proyecto académico orientado a objetos para modelar elementos con huella de carbono o consumo estimado.

## Descripcion del proyecto

El sistema modela tres tipos de objetos (`Edificio`, `Automovil` y `Bicicleta`) que comparten un contrato comun para calcular su huella de carbono. La aplicacion:

1. Crea objetos del dominio.
2. Usa polimorfismo para calcular su huella.
3. Guarda los objetos en un archivo JSON.
4. Lee nuevamente el JSON y muestra los datos recuperados.

## Interfaz `CalculableHuellaCarbono`

Se implementa como clase abstracta (`ABC`) en `modelo/calculable_huella_carbono.py`.

- Metodo principal: `calcular_huella_carbono() -> float`
- Metodo de soporte para persistencia: `a_dict() -> dict`

Este diseno permite aplicar sustitucion de Liskov y depender de abstracciones.

## Objetos implementados

- `Edificio` (`modelo/edificio.py`)
  - Atributos: `nombre`, `consumo_energia_mensual`, `factor_emision`
  - Formula: `consumo_energia_mensual * factor_emision`

- `Automovil` (`modelo/automovil.py`)
  - Atributos: `placa`, `kilometros_recorridos`, `consumo_por_kilometro`, `factor_emision`
  - Formula: `kilometros_recorridos * consumo_por_kilometro * factor_emision`

- `Bicicleta` (`modelo/bicicleta.py`)
  - Atributos: `marca`, `kilometros_recorridos`, `factor_emision_indirecta`
  - Formula: `kilometros_recorridos * factor_emision_indirecta`

## Polimorfismo

En `app/main.py`, los objetos se almacenan en una lista de tipo `CalculableHuellaCarbono`. El servicio `ServicioHuellaCarbono` recorre la lista sin depender de clases concretas, cumpliendo OCP y DIP.

## Guardado y lectura de JSON

La capa de persistencia esta en `persistencia/repositorio_huella_json.py`.

- Guardado: `guardar(objetos)` serializa a `data/huella_carbono.json`.
- Lectura: `leer()` deserializa y reconstruye objetos por campo `tipo`.

## Estructura del proyecto

```text
app/
modelo/
persistencia/
prueba/
servicio/
data/
```

## Como ejecutar el programa

1. Instalar dependencias:

```bash
pip install -r requirements.txt
```

2. Ejecutar la app:

```bash
python -m app.main
```

## Como ejecutar las pruebas unitarias

```bash
pytest -q
```

Incluye minimo 10 pruebas unitarias en `prueba/test_huella_carbono.py`.

## Aplicacion de principios SOLID

- **SRP:** modelo, servicio, persistencia y app estan separados.
- **OCP:** se pueden agregar nuevos tipos implementando la interfaz.
- **LSP:** cualquier objeto implementador funciona en la lista polimorfica.
- **ISP:** interfaz pequena y enfocada al calculo de huella.
- **DIP:** logica principal depende de `CalculableHuellaCarbono`, no de concreciones.

## Evidencia de rama correcta

La rama final de trabajo es `dev_ltuiran07` y se conserva la estructura:

- `main`
- `develop`
- `dev_ltuiran07`

Verificacion:

```bash
git branch
```
