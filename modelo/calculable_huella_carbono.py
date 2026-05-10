from __future__ import annotations

from abc import ABC, abstractmethod


class CalculableHuellaCarbono(ABC):
    """Define el contrato para objetos con huella de carbono calculable."""

    @abstractmethod
    def calcular_huella_carbono(self) -> float:
        """Retorna la huella de carbono estimada."""

    @abstractmethod
    def a_dict(self) -> dict:
        """Serializa el objeto para persistencia en JSON."""
