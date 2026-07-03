"""Implementa RN-002 (docs/business-rules.md): un curso se aprueba con nota >= 75%."""


def calcular_aprobacion(nota: float) -> bool:
    return nota >= 75
