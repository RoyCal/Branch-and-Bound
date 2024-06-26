from mip import OptimizationStatus
from SolutionType import SolutionType

class Solution():
    # Constructor
    def __init__(self, model):
        self.model = model                                                  # Modelo
        self.solution = self.model.optimize()                               # Solução
        if self.solution == OptimizationStatus.INFEASIBLE:                  # Verifica se a solução é inviável
            self.solutionType = SolutionType.INFEASIBLE
            self.solutionValue = None
            self.variablesValues = None
            self.variables = None
        else:                                                               # Caso a solução seja viável:
            self.solutionValue = model.objective_value                      # Armaneza o valor da solução
            self.variablesValues = [i.x for i in list(self.model.vars)]     # Armazena os valores das variáveis
            self.variables = list(self.model.vars)                          # Armazena as variáveis
            self.defineSolutionType()                                       # Define o tipo da solução (binária ou não)
    
    # Método que define o tipo da solução
    def defineSolutionType(self):
        for i in self.variablesValues:
            if float(i).is_integer():
                continue
            else:
                self.solutionType = SolutionType.CONTINUOUS
                return
        self.solutionType = SolutionType.INTEGER