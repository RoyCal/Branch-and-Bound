from Solution import Solution
from mip import CONTINUOUS

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

        if solution.solutionType == 'integer':
            self.Zp = solution.solutionValue
            self.popSolution()
            return False
        
        if solution.solutionType == 'infeasible':
            self.popSolution()
            return True
        
        if solution.solutionValue < self.Zp:
            self.popSolution()
            return True

        i = self.checkVars(solution.variablesValues)

        solution.model += solution.variables[i] == 0
        solution1 = Solution(solution.model, solution.variables)

                   
        solution2 = Solution(solution.model, solution.variables)

        self.solutions.append(solution1)
        self.solutions.append(solution2)

        self.Zd = max(solution1.solutionValue, solution2.solutionValue)

        self.popSolution()

        return True

    def checkVars(self, variableValues):
        closest = abs(variableValues[0] - 0.5)
        variableIndex = 0

        for i in variableValues:
            if abs(i - 0.5) < closest:
                closest = abs(i - 0.5)
                variableIndex = variableValues.index(i)
        
        return variableIndex

    def popSolution(self):
        self.solutions.pop(0)

    def solve(self):
        while self.branch():
            pass
            
        print(self.Zp)
    