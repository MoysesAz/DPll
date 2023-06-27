import sys, getopt
from functools import lru_cache

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
