from __future__ import annotations

from modelo.calculable_huella_carbono import CalculableHuellaCarbono


class ServicioHuellaCarbono:
    """Provee operaciones de negocio para objetos calculables."""

    def generar_reporte(self, objetos: list[CalculableHuellaCarbono]) -> list[dict]:
        reporte = []
        for objeto in objetos:
            reporte.append(
                {
                    "tipo": type(objeto).__name__,
                    "huella_carbono": objeto.calcular_huella_carbono(),
                }
            )
        return reporte

    def calcular_total(self, objetos: list[CalculableHuellaCarbono]) -> float:
        return sum(objeto.calcular_huella_carbono() for objeto in objetos)
