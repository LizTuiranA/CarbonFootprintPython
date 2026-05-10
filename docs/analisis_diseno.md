# Analisis de diseno

## 1. Objetivo

Modelar objetos con huella de carbono usando programacion orientada a objetos, polimorfismo, persistencia JSON y pruebas unitarias, manteniendo separacion de responsabilidades.

## 2. Arquitectura

Se adopta una arquitectura por capas ligera:

1. `app`: orquestacion de flujo de la aplicacion.
2. `servicio`: logica de negocio transversal (reportes y totalizacion).
3. `modelo`: entidades del dominio y contrato comun.
4. `persistencia`: lectura y escritura de datos en JSON.
5. `prueba`: validacion automatizada del comportamiento.

Flujo general:

`app/main.py` -> `servicio/servicio_huella_carbono.py` -> `modelo/*`

`app/main.py` -> `persistencia/repositorio_huella_json.py` -> `data/huella_carbono.json`

## 3. Decisiones de modelado

### Interfaz comun

`CalculableHuellaCarbono` (ABC) define:

- `calcular_huella_carbono()` para estandarizar el calculo.
- `a_dict()` para serializacion sin acoplar app/persistencia a clases concretas.

### Entidades del dominio

- `Edificio`: `consumo_energia_mensual * factor_emision`
- `Automovil`: `kilometros_recorridos * consumo_por_kilometro * factor_emision`
- `Bicicleta`: `kilometros_recorridos * factor_emision_indirecta`

Cada entidad valida que valores de consumo/factores no sean negativos.

## 4. Persistencia

`RepositorioHuellaJSON` centraliza operaciones de archivo:

- `guardar(objetos)`: serializa lista de objetos.
- `leer()`: reconstruye objetos segun campo discriminador `tipo`.

Esto permite mantener la capa de aplicacion libre de detalles de JSON.

## 5. SOLID aplicado

- **SRP:** cada modulo cumple una tarea especifica.
- **OCP:** para agregar una nueva fuente de huella se implementa la interfaz sin romper servicio/app.
- **LSP:** cualquier implementacion de la interfaz funciona en la coleccion polimorfica.
- **ISP:** interfaz pequena, enfocada en calculo y serializacion.
- **DIP:** el flujo principal depende de la abstraccion `CalculableHuellaCarbono`.

## 6. Estrategia de pruebas

`pytest` cubre:

- formulas de calculo por tipo de objeto.
- validaciones de datos de entrada.
- reporte y total en servicio.
- guardado y lectura en JSON.
- manejo de tipo no soportado en deserializacion.

Resultado esperado del paquete actual: `12 passed`.
