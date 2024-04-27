from mip import OptimizationStatus

class Solution():
    def __init__(self, model, variables):
        self.model = model
        self.solution = self.model.optimize()
        if self.solution == OptimizationStatus.INFEASIBLE:
            self.solutionType = 'infeasible'
            self.solutionValue = None
            self.variablesValues = None
            self.variables = None
        else:
            self.solutionValue = model.objective_value
            self.variablesValues = [i.x for i in variables]
            self.variables = variables
            self.defineSolutionType()
    
    def defineSolutionType(self):
        for i in self.variablesValues:
            if i == 0 or i == 1:
                continue
            else:
                self.solutionType = 'continuous'
                return
        self.solutionType = 'binary'
    
    def modelCopy(self):
        pass