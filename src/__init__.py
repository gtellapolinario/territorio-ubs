"""
Módulo principal do território UBS.
Contém classes e funções para gerenciamento de território de UBS.
"""

from .biblioteca_ubs import GerenciadorTerritorio, DadosProcessados, CensoDemografico
from .consulta import ConsultasTerritorio

__version__ = "1.0.0"
__author__ = "Guilherme Tell"

# Exporta classes principais
__all__ = [
    "GerenciadorTerritorio",
    "DadosProcessados",
    "CensoDemografico",
    "ConsultasTerritorio"
]
