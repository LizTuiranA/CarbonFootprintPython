from __future__ import annotations

from dataclasses import dataclass

from modelo.calculable_huella_carbono import CalculableHuellaCarbono


@dataclass
class Edificio(CalculableHuellaCarbono):
    nombre: str
    consumo_energia_mensual: float
    factor_emision: float

    def __post_init__(self) -> None:
        if self.consumo_energia_mensual < 0:
            raise ValueError("El consumo de energia mensual no puede ser negativo")
        if self.factor_emision < 0:
            raise ValueError("El factor de emision no puede ser negativo")

    def calcular_huella_carbono(self) -> float:
        return self.consumo_energia_mensual * self.factor_emision

    def a_dict(self) -> dict:
        return {
            "tipo": "Edificio",
            "nombre": self.nombre,
            "consumo_energia_mensual": self.consumo_energia_mensual,
            "factor_emision": self.factor_emision,
        }
