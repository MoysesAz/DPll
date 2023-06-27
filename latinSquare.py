import itertools

class ReadMatrix:
    def __init__(self, fileName):
        self.fileName = fileName

    def read_matrix(self):
        with open(self.fileName, 'r') as f:
            matrix = [[int(num) for num in line.split(',')] for line in f.read().split(';') if line]
        return matrix


class WriteMatrix:
    def __init__(self, fileName, matrix):
        self.fileName = fileName
        self.n = len(matrix)
        self.matrix = matrix
        self.clauses = []

    # Restrição 1: Cada célula contém exatamente um símbolo
    def atLeast1Number(self, n): 
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 0:
                    self.clauses.append([n * n * i + n * j + k + 1 for k in range(n)])
                else:
                    self.clauses.append([n * n * i + n * j + matrix[i][j]])

    # Restrição 2: Cada símbolo ocorre no máximo uma vez em cada linha
    def oncePerLine(self, n):
        for i in range(n):
            for k in range(n):
                for j1, j2 in itertools.combinations(range(n), 2):
                    self.clauses.append([-(n * n * i + n * j1 + k + 1), -(n * n * i + n * j2 + k + 1)])

    # Restrição 3: Cada símbolo ocorre no máximo uma vez em cada coluna
    def onceInEachColumn(self, n):
        for j in range(n):
            for k in range(n):
                for i1, i2 in itertools.combinations(range(n), 2):
                    self.clauses.append([-(n * n * i1 + n * j + k + 1), -(n * n * i2 + n * j + k + 1)])
    
    # Restrição 4: Cada símbolo ocorre no máximo uma vez na diagonal principal
    def onceOnTheMainDiagonal(self, n):
        for k in range(n):
            for i1, i2 in itertools.combinations(range(n), 2):
                self.clauses.append([-(n * n * i1 + n * i1 + k + 1), -(n * n * i2 + n * i2 + k + 1)])

    # Restrição 5: Cada símbolo ocorre no máximo uma vez na diagonal secundária
    def onceOnTheMainSecondary(self, n):
        for k in range(n):
            for i1, i2 in itertools.combinations(range(n), 2):
                self.clauses.append([-(n * n * i1 + n * (n - 1 - i1) + k + 1), -(n * n * i2 + n * (n - 1 - i2) + k + 1)])
        
    def createClauses(self):
        self.atLeast1Number(self.n)
        self.oncePerLine(self.n)
        self.onceInEachColumn(self.n)
        self.onceOnTheMainDiagonal(self.n)
        self.onceOnTheMainSecondary(self.n)

    def save(self, n):
        with open(self.fileName, 'w') as f:
            f.write(f'p cnf {n*n*n} {len(self.clauses)}\n')
            f.write('\n'.join([' '.join(map(str, clause)) + ' 0' for clause in self.clauses]))



instanceReadMatrix = ReadMatrix('matrix.txt')
matrix = instanceReadMatrix.read_matrix()
instanceWriteMatrix = WriteMatrix('matrixCNF.cnf', matrix)
instanceWriteMatrix.createClauses()
instanceWriteMatrix.save(instanceWriteMatrix.n)
