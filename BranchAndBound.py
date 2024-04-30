from Solution import Solution
from SolutionType import SolutionType

class BranchAndBound():
    # Constructor
    def __init__(self, model):
        self.model = model.copy()                   # Cópia do modelo
        self.variables = list(self.model.vars)      # Lista de variáveis do modelo
        self.Zd = float('inf')                      # Inicia o limite dual
        self.Zp = float('-inf')                     # Inicia o limite primal
        self.solutions = [Solution(self.model)]     # Inicia a lista de soluções com a melhor solução possível do problema original
        self.optimalSolutionVarsValues = []         # Atributo para armazenar futuramente os valores das variáveis da solução ótima

    # Método de Branch: retorna True se houver soluções a serem analisadas e False caso contrário
    def branch(self):
        # Verifica se a lista de soluções está vazia, pois se estiver, não há mais soluções a serem analisadas
        if len(self.solutions) == 0:
            return False
        
        # Seleciona a priimeira solução da lista
        solution = self.solutions[0]

        # Poda por inviabilidade
        if solution.solutionType == SolutionType.INFEASIBLE:
            self.bound()
            return True
        
        # Poda por limite
        if solution.solutionValue < self.Zp:
            self.bound()
            return True

        # Poda por solução binária
        if solution.solutionType == SolutionType.BINARY:
            self.Zp = solution.solutionValue
            self.optimalSolutionVarsValues = solution.variablesValues
            self.bound()
            return True

        # Armazena o índice da variável que mais se aproxima de 0.5 e é diferente de 0 e de 1
        i = self.checkVars(solution.variablesValues)

        # Adiciona a restrição de que a variável selecionada deve ser igual a 0
        solution.model += solution.variables[i] == 0
        solution1 = Solution(solution.model.copy())

        solution.model.remove((solution.model.constrs[-1]))

        # Adiciona a restrição de que a variável selecionada deve ser igual a 1
        solution.model += solution.variables[i] == 1
        solution2 = Solution(solution.model.copy())

        # Adiciona as duas soluções na lista de soluções
        self.solutions.append(solution1)
        self.solutions.append(solution2)

        # Atualiza o limite dual
        self.setZd(solution1.solutionValue, solution2.solutionValue)

        # Remove a solução atual da lista de soluções
        self.popSolution()

        return True

    # Metodo que retona o índice da variável que mais se aproxima de 0.5 e é diferente de 0 e de 1
    def checkVars(self, variableValues):
        closest = float('inf')
        variableIndex = 0

        for i in variableValues:
            if i != 0 and i != 1 and abs(i - 0.5) < closest:
                closest = abs(i - 0.5)
                variableIndex = variableValues.index(i)
        
        return variableIndex

    # Método que remove a primeira solução da lista de soluções
    def popSolution(self):
        self.solutions.pop(0)

    # Método que realiza a poda (criado apenas para melhorar o entendimento do código)
    def bound(self):
        self.popSolution()

    # Método que atualiza o limite dual
    def setZd(self, value1, value2):
        if value1 != None and value2 != None:
            self.Zd = max(value1, value2)
        elif type(value1) == None:
            self.Zd = value2
        elif type(value2) == None:
            self.Zd = value1

    # Método que resolve o problema e imprime a solução ótima
    def solveAndPrint(self):
        # Realiza o branch até que não haja mais soluções a serem analisadas
        while self.branch():
            pass
        
        # Imprime a solução ótima e os valores das variáveis
        print("Valor da solução ótima: ", self.Zp)
        print("\nValores das variáveis: ")
        for i in range(len(self.variables)):
            print(self.variables[i].name, ": ", self.optimalSolutionVarsValues[i])
    