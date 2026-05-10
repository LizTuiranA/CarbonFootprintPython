from __future__ import annotations

import json
from pathlib import Path

from modelo.automovil import Automovil
from modelo.bicicleta import Bicicleta
from modelo.calculable_huella_carbono import CalculableHuellaCarbono
from modelo.edificio import Edificio


class RepositorioHuellaJSON:
    """Persistencia de objetos de huella de carbono en JSON."""

    def __init__(self, ruta_archivo: str) -> None:
        self.ruta_archivo = Path(ruta_archivo)

    def guardar(self, objetos: list[CalculableHuellaCarbono]) -> None:
        self.ruta_archivo.parent.mkdir(parents=True, exist_ok=True)
        datos = [objeto.a_dict() for objeto in objetos]
        with self.ruta_archivo.open("w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=2, ensure_ascii=False)

    def leer(self) -> list[CalculableHuellaCarbono]:
        with self.ruta_archivo.open("r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        return [self._crear_objeto(item) for item in datos]

    def _crear_objeto(self, item: dict) -> CalculableHuellaCarbono:
        tipo = item.get("tipo")
        if tipo == "Edificio":
            return Edificio(
                nombre=item["nombre"],
                consumo_energia_mensual=item["consumo_energia_mensual"],
                factor_emision=item["factor_emision"],
            )
        if tipo == "Automovil":
            return Automovil(
                placa=item["placa"],
                kilometros_recorridos=item["kilometros_recorridos"],
                consumo_por_kilometro=item["consumo_por_kilometro"],
                factor_emision=item["factor_emision"],
            )
        if tipo == "Bicicleta":
            return Bicicleta(
                marca=item["marca"],
                kilometros_recorridos=item["kilometros_recorridos"],
                factor_emision_indirecta=item["factor_emision_indirecta"],
            )
        raise ValueError(f"Tipo de objeto no soportado: {tipo}")
