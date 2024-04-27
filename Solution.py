from mip import OptimizationStatus
from SolutionType import SolutionType

class Solution():
    def __init__(self, model):
        self.model = model
        self.solution = self.model.optimize()
        if self.solution == OptimizationStatus.INFEASIBLE:
            self.solutionType = SolutionType.INFEASIBLE
            self.solutionValue = None
            self.variablesValues = None
            self.variables = None
        else:
            self.solutionValue = model.objective_value
            self.variablesValues = [i.x for i in list(self.model.vars)]
            self.variables = list(self.model.vars)
            self.defineSolutionType()
    
    def defineSolutionType(self):
        for i in self.variablesValues:
            if i == 0 or i == 1:
                continue
            else:
                self.solutionType = SolutionType.NOT_BINARY
                return
        self.solutionType = SolutionType.BINARY
    
    def modelCopy(self):
        pass