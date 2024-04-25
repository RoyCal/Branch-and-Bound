from Solution import Solution

class BABTree():
    def __init__(self, model, variables):
        self.model = model
        self.variables = variables
        self.Zd = float('inf')
        self.Zp = float('-inf')
        self.solutions = [Solution(model, self.variables)]
        self.best_solution = None

    def branch():
        pass

    def checkVars(self, variableValues):
        closest = abs(variableValues[0] - 0.5)
        variableValue = variableValues[0]
        variableIndex = 0

        for i in variableValues:
            if abs(i - 0.5) < closest:
                closest = abs(i - 0.5)
                variableValue = i
                variableIndex = variableValues.index(i)
        
        return variableValue, variableIndex

    def popSolution(self):
        self.solutions.pop(0)