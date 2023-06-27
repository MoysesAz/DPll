#!/bin/bash

# Diretório de testes
test_dir="test_cases"

# Nome do arquivo .py a ser executado
python_file="MyDpll.py"

# Loop pelos arquivos .cnf no diretório de testes
for test_file in "$test_dir"/*.cnf; do
    echo "Running: $test_file"
    python "$python_file" "$test_file"
    echo "----------------------------------------"
done
