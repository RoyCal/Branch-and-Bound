class Solution():
    def __init__(self, model, variables):
        self.model = model
        self.solution = self.model.optimize()
        self.solutionValue = model.objective_value
        self.variablesValues = [i.x for i in variables]
        self.defineSolutionType()
    
    def defineSolutionType(self):
        for i in self.variablesValues:
            if float.is_integer(i):
                continue
            else:
                self.solutionType = 'continuous'
                return
        self.solutionType = 'integer'