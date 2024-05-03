from enum import Enum

# Tipo da solução
class SolutionType(Enum):
    # Solução inviável
    INFEASIBLE = 0

    # Solução inteira
    INTEGER = 1

    # Solução contínua
    CONTINUOUS = 2