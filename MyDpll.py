import sys

class ReadCNF:
    def __init__(self, inputfile):
        self.num_variables, self.clauses = self.read_cnf(inputfile)

    @staticmethod
    def read_cnf(file_path):
        clauses = []
        num_variables = 0

        with open(file_path, 'r') as file:
            lines = file.readlines()

            for line in lines:
                if line.startswith('c'):
                    continue
                elif line.startswith('p cnf'):
                    num_variables = int(line.split()[2])
                else:
                    clause = [int(literal) for literal in line.split()[:-1]]
                    clauses.append(clause)

        return num_variables, clauses

class DPLL:
    def __init__(self, pathFile):
        self.fileCNF = ReadCNF(pathFile)

    @staticmethod
    def dpll(clauses, assignment):
        if all(len(clause) == 0 for clause in clauses):
            return True

        if any(len(clause) == 0 for clause in clauses):
            return False

        unit_clauses = [clause[0] for clause in clauses if len(clause) == 1]

        for unit in unit_clauses:
            if -unit in assignment:
                continue
            assignment.add(unit)
            new_clauses = [clause for clause in clauses if unit not in clause]
            simplified_clauses = [list(filter(lambda l: l != -unit, clause)) for clause in new_clauses]
            if DPLL.dpll(simplified_clauses, assignment):
                return True
            assignment.remove(unit)

        pure_literals = []
        literals = [literal for clause in clauses for literal in clause]
        for literal in literals:
            if -literal not in literals:
                pure_literals.append(literal)

        for pure_literal in pure_literals:
            if -pure_literal in assignment:
                continue
            assignment.add(pure_literal)
            new_clauses = [clause for clause in clauses if pure_literal not in clause]
            simplified_clauses = [list(filter(lambda l: l != -pure_literal, clause)) for clause in new_clauses]
            if DPLL.dpll(simplified_clauses, assignment):
                return True
            assignment.remove(pure_literal)

        literal = clauses[0][0]
        assignment.add(literal)
        new_clauses = [clause for clause in clauses if literal not in clause]
        simplified_clauses = [list(filter(lambda l: l != -literal, clause)) for clause in new_clauses]
        if DPLL.dpll(simplified_clauses, assignment):
            return True
        assignment.remove(literal)

        return False

def main(argv):
    pathFile = argv[0]
    instanceDPLL = DPLL(pathFile)
    assignment = set()

    if instanceDPLL.dpll(instanceDPLL.fileCNF.clauses, assignment):
        print('Satisfiable')
        print('Assignment:', assignment)
    else:
        print('Unsatisfiable')

if __name__ == "__main__":
    main(sys.argv[1:])
