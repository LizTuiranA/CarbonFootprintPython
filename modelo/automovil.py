from __future__ import annotations

from dataclasses import dataclass

from modelo.calculable_huella_carbono import CalculableHuellaCarbono


@dataclass
class Automovil(CalculableHuellaCarbono):
    placa: str
    kilometros_recorridos: float
    consumo_por_kilometro: float
    factor_emision: float

    def __post_init__(self) -> None:
        if self.kilometros_recorridos < 0:
            raise ValueError("Los kilometros recorridos no pueden ser negativos")
        if self.consumo_por_kilometro < 0:
            raise ValueError("El consumo por kilometro no puede ser negativo")
        if self.factor_emision < 0:
            raise ValueError("El factor de emision no puede ser negativo")

    def calcular_huella_carbono(self) -> float:
        return self.kilometros_recorridos * self.consumo_por_kilometro * self.factor_emision

    def a_dict(self) -> dict:
        return {
            "tipo": "Automovil",
            "placa": self.placa,
            "kilometros_recorridos": self.kilometros_recorridos,
            "consumo_por_kilometro": self.consumo_por_kilometro,
            "factor_emision": self.factor_emision,
        }
