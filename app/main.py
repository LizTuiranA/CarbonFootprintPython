from __future__ import annotations

from modelo.automovil import Automovil
from modelo.bicicleta import Bicicleta
from modelo.calculable_huella_carbono import CalculableHuellaCarbono
from modelo.edificio import Edificio
from persistencia.repositorio_huella_json import RepositorioHuellaJSON
from servicio.servicio_huella_carbono import ServicioHuellaCarbono


def crear_objetos_demo() -> list[CalculableHuellaCarbono]:
    return [
        Edificio(nombre="Bloque A", consumo_energia_mensual=1200.0, factor_emision=0.45),
        Automovil(
            placa="ABC123",
            kilometros_recorridos=800.0,
            consumo_por_kilometro=0.08,
            factor_emision=2.31,
        ),
        Bicicleta(marca="EcoBike", kilometros_recorridos=300.0, factor_emision_indirecta=0.01),
    ]


def main() -> None:
    objetos = crear_objetos_demo()
    servicio = ServicioHuellaCarbono()
    repositorio = RepositorioHuellaJSON("data/huella_carbono.json")

    print("--- Huella de carbono por objeto ---")
    for item in servicio.generar_reporte(objetos):
        print(f"{item['tipo']}: {item['huella_carbono']:.2f}")

    print(f"Total: {servicio.calcular_total(objetos):.2f}")

    repositorio.guardar(objetos)
    objetos_leidos = repositorio.leer()

    print("\n--- Datos leidos desde JSON ---")
    for objeto in objetos_leidos:
        print(objeto.a_dict())


if __name__ == "__main__":
    main()
