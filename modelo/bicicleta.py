from __future__ import annotations

from dataclasses import dataclass

from modelo.calculable_huella_carbono import CalculableHuellaCarbono


@dataclass
class Bicicleta(CalculableHuellaCarbono):
    marca: str
    kilometros_recorridos: float
    factor_emision_indirecta: float

    def __post_init__(self) -> None:
        if self.kilometros_recorridos < 0:
            raise ValueError("Los kilometros recorridos no pueden ser negativos")
        if self.factor_emision_indirecta < 0:
            raise ValueError("El factor de emision indirecta no puede ser negativo")

    def calcular_huella_carbono(self) -> float:
        return self.kilometros_recorridos * self.factor_emision_indirecta

    def a_dict(self) -> dict:
        return {
            "tipo": "Bicicleta",
            "marca": self.marca,
            "kilometros_recorridos": self.kilometros_recorridos,
            "factor_emision_indirecta": self.factor_emision_indirecta,
        }
