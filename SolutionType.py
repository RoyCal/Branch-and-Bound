from enum import Enum

# Tipo da solução
class SolutionType(Enum):
    # Solução inviável
    INFEASIBLE = 0

    # Solução binária
    BINARY = 1

    # Solução não binária
    INTEGER = 2