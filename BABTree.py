from Solution import Solution
from mip import Constr

class BABTree():
    def __init__(self, model, variables):
        self.model = model
        self.variables = variables
        self.Zd = float('inf')
        self.Zp = float('-inf')
        self.solutions = [Solution(self.model, self.variables)]

    def branch(self):
        if len(self.solutions) == 0:
            return False
        
        solution = self.solutions[0]

        if solution.solutionType == 'infeasible':
            self.popSolution()
            return True

        if solution.solutionValue < self.Zp:
            self.popSolution()
            return True

        if solution.solutionType == 'binary':
            self.Zp = solution.solutionValue
            self.popSolution()
            return True

        i = self.checkVars(solution.variablesValues)

        solution.model += solution.variables[i] == 0
        modelCopy = solution.model.copy()
        solution1 = Solution(modelCopy, list(modelCopy.vars))

        solution.model.remove((solution.model.constrs[-1]))

        solution.model += solution.variables[i] == 1
        modelCopy = solution.model.copy()
        solution2 = Solution(modelCopy, list(modelCopy.vars))

        self.solutions.append(solution1)
        self.solutions.append(solution2)

        self.setZd(solution1.solutionValue, solution2.solutionValue)

        self.popSolution()

        return True

    def checkVars(self, variableValues):
        closest = float('inf')
        variableIndex = 0

        for i in variableValues:
            if i != 0 and i != 1 and abs(i - 0.5) < closest:
                closest = abs(i - 0.5)
                variableIndex = variableValues.index(i)
        
        return variableIndex

    def popSolution(self):
        self.solutions.pop(0)

    def setZd(self, value1, value2):
        if value1 != None and value2 != None:
            self.Zd = max(value1, value2)
        elif type(value1) == None:
            self.Zd = value2
        elif type(value2) == None:
            self.Zd = value1

    def solve(self):
        while self.branch():
            pass
            
        print(self.Zp)
    