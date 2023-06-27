def create_cnf_file(matrix, filename):
    n = len(matrix)
    num_symbols = n * n

    clauses = []

    # Restrição 1: Cada célula contém exatamente um símbolo
    for i in range(n):
        for j in range(n):
            clause = []
            for k in range(1, n + 1):
                clause.append(i * n * n + j * n + k)
            clauses.append(clause)

            for k in range(1, n + 1):
                for l in range(k + 1, n + 1):
                    clauses.append([-1 * (i * n * n + j * n + k), -1 * (i * n * n + j * n + l)])

    # Restrição 2: Cada símbolo ocorre no máximo uma vez em cada linha
    for i in range(n):
        for k in range(1, n + 1):
            for j in range(n):
                for l in range(j + 1, n):
                    clauses.append([-1 * (i * n * n + j * n + k), -1 * (i * n * n + l * n + k)])

    # Restrição 3: Cada símbolo ocorre no máximo uma vez em cada coluna
    for j in range(n):
        for k in range(1, n + 1):
            for i in range(n):
                for l in range(i + 1, n):
                    clauses.append([-1 * (i * n * n + j * n + k), -1 * (l * n * n + j * n + k)])

    # Restrição 4: Cada símbolo ocorre no máximo uma vez na diagonal principal
    for k in range(1, n + 1):
        for i in range(n):
            for j in range(n):
                if i != j:
                    clauses.append([-1 * (i * n * n + i * n + k), -1 * (j * n * n + j * n + k)])

    # Restrição 5: Cada símbolo ocorre no máximo uma vez na diagonal secundária
    for k in range(1, n + 1):
        for i in range(n):
            for j in range(n):
                if i + j != n - 1:
                    clauses.append([-1 * (i * n * n + (n - 1 - i) * n + k), -1 * (j * n * n + (n - 1 - j) * n + k)])

    # Restrição 6: Valores pré-definidos
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                clauses.append([i * n * n + j * n + matrix[i][j]])

    num_clauses = len(clauses)

    # Escrever as cláusulas no arquivo CNF
    with open(filename, 'w') as file:
        file.write(f'p cnf {num_symbols} {num_clauses}\n')
        for clause in clauses:
            clause.append(0)  # Adicionar terminador 0
            file.write(' '.join(str(literal) for literal in clause) + '\n')

# Exemplo de uso
matrix = [
    [0, 0, 0, 2],
    [4, 0, 1, 3],
    [2, 0, 3, 0],
    [3, 0, 0, 0]
]

create_cnf_file(matrix, 'quadrado_latino.cnf')