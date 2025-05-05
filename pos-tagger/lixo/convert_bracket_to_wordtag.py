import re
import os
#este arquivo está defasado, o código novo já fez isto automaticamente

def convert_bracket_file():
    input_path = r"C:\Users\thiag\Downloads\exercicios_programming\pos-tagger\outputs\predictions_dev.txt"
    output_path = r"C:\Users\thiag\Downloads\exercicios_programming\pos-tagger\outputs\predictions_converted.txt"

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(input_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    output_lines = []
    for idx, line in enumerate(lines):
        # Remove o primeiro parêntese e o "S" (para começar com a tag correta)
        line = line.strip()
        if line.startswith("(S "):
            line = line[3:]  # Remove "(S " no começo da linha

        # Captura (TAG palavra) corretamente
        tags = re.findall(r"\((\S+)\s+([^)]+)\)", line)
        if not tags:
            print(f"Aviso: linha {idx+1} não possui pares (TAG palavra): {line}")
            output_lines.append(line)
            continue

        # Converte para "palavra_TAG"
        new_line = " ".join([f"{word}_{tag}" for tag, word in tags])
        output_lines.append(new_line)

    print(f"Processadas {len(output_lines)} linhas para saída")

    with open(output_path, "w", encoding="utf-8") as f:
        for line in output_lines:
            f.write(line + "\n")

# Executa a função diretamente
convert_bracket_file()
