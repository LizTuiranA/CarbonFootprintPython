from __future__ import annotations

import json

import pytest

from modelo.automovil import Automovil
from modelo.bicicleta import Bicicleta
from modelo.edificio import Edificio
from persistencia.repositorio_huella_json import RepositorioHuellaJSON
from servicio.servicio_huella_carbono import ServicioHuellaCarbono


def test_calculo_huella_edificio():
    edificio = Edificio("Bloque B", 1000.0, 0.5)
    assert edificio.calcular_huella_carbono() == 500.0


def test_calculo_huella_automovil():
    auto = Automovil("XYZ987", 100.0, 0.1, 2.0)
    assert auto.calcular_huella_carbono() == 20.0


def test_calculo_huella_bicicleta():
    bici = Bicicleta("Ruta", 200.0, 0.01)
    assert bici.calcular_huella_carbono() == 2.0


def test_huella_cero_bicicleta_si_km_cero():
    bici = Bicicleta("Ciudad", 0.0, 0.02)
    assert bici.calcular_huella_carbono() == 0.0


def test_servicio_generar_reporte_devuelve_tipos_correctos():
    objetos = [Edificio("A", 100, 0.1), Automovil("A1", 10, 0.2, 1.0), Bicicleta("M", 3, 0.4)]
    servicio = ServicioHuellaCarbono()

    reporte = servicio.generar_reporte(objetos)
    tipos = [item["tipo"] for item in reporte]

    assert tipos == ["Edificio", "Automovil", "Bicicleta"]


def test_servicio_calcular_total():
    objetos = [Edificio("A", 100, 0.1), Automovil("A1", 10, 0.2, 1.0), Bicicleta("M", 3, 0.4)]
    servicio = ServicioHuellaCarbono()

    assert servicio.calcular_total(objetos) == pytest.approx(13.2)


def test_repositorio_guarda_json(tmp_path):
    ruta = tmp_path / "huella.json"
    repo = RepositorioHuellaJSON(str(ruta))
    objetos = [Edificio("A", 100, 0.1)]

    repo.guardar(objetos)

    assert ruta.exists()
    data = json.loads(ruta.read_text(encoding="utf-8"))
    assert data[0]["tipo"] == "Edificio"


def test_repositorio_lee_json_y_reconstruye_objetos(tmp_path):
    ruta = tmp_path / "huella.json"
    ruta.write_text(
        json.dumps(
            [
                {
                    "tipo": "Automovil",
                    "placa": "AAA111",
                    "kilometros_recorridos": 50,
                    "consumo_por_kilometro": 0.1,
                    "factor_emision": 2,
                }
            ]
        ),
        encoding="utf-8",
    )
    repo = RepositorioHuellaJSON(str(ruta))

    leidos = repo.leer()

    assert len(leidos) == 1
    assert isinstance(leidos[0], Automovil)
    assert leidos[0].calcular_huella_carbono() == 10.0


def test_tipo_no_soportado_lanza_error(tmp_path):
    ruta = tmp_path / "huella.json"
    ruta.write_text(json.dumps([{"tipo": "Arbol"}]), encoding="utf-8")
    repo = RepositorioHuellaJSON(str(ruta))

    with pytest.raises(ValueError):
        repo.leer()


def test_no_permite_valores_negativos_edificio():
    with pytest.raises(ValueError):
        Edificio("A", -1, 0.4)


def test_no_permite_valores_negativos_automovil():
    with pytest.raises(ValueError):
        Automovil("ABC", -10, 0.1, 2.0)


def test_no_permite_valores_negativos_bicicleta():
    with pytest.raises(ValueError):
        Bicicleta("B", 10, -0.1)
