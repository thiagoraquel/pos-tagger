import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd
import os
import numpy as np
from .utils import read_tagged_sentences

def evaluate_accuracy(predicted_path, gold_path):
    # Lê as sentenças com palavras e tags no formato "palavra_tag"
    pred_sentences = read_tagged_sentences(predicted_path)
    gold_sentences = read_tagged_sentences(gold_path)

    correct = 0
    total = 0

    # Compara as sentenças previstas com as reais (gold)
    for pred, gold in zip(pred_sentences, gold_sentences):
        for (p_word, p_tag), (g_word, g_tag) in zip(pred, gold):
            if p_word != g_word:
                continue  # Ignora desalinhamento
            if g_tag in ['.', ',', ':', "``", "''"]:  # Ignora pontuação
                continue
            if p_tag == g_tag:
                correct += 1
            total += 1

    accuracy = correct / total if total > 0 else 0
    print(f"Acurácia: {accuracy:.4f} ({correct}/{total})")


def generate_confusion_matrix(predicted_path, gold_path, max_tags=20):
    pred_sentences = read_tagged_sentences(predicted_path)
    gold_sentences = read_tagged_sentences(gold_path)

    counts = Counter()

    for pred, gold in zip(pred_sentences, gold_sentences):
        for (p_word, p_tag), (g_word, g_tag) in zip(pred, gold):
            if p_word != g_word or g_tag in ['.', ',', ':', "``", "''"]:
                continue
            counts[(g_tag, p_tag)] += 1

    # Define manualmente a ordem e o conjunto de tags a serem exibidas
    tag_set = ['NN', 'IN', 'DT', 'NNP', 'JJ', 'NNS', 'CD', 'PDT', 'CC', 'VBD', 'VBZ', 'VB', 'VBN', 'VBP', 'RP', 'RBR', 'RB', 'PRP', 'TO', 'MD']


    matrix = pd.DataFrame(
        data=np.zeros((len(tag_set), len(tag_set)), dtype=int),
        index=tag_set,
        columns=tag_set
    )

    for (g_tag, p_tag), count in counts.items():
        if g_tag in tag_set and p_tag in tag_set:
            matrix.loc[g_tag, p_tag] += count

    if matrix.to_numpy().size == 0:
        print("⚠️ Matriz de confusão vazia. Nenhum dado válido para comparar.")
        return

    # Cria o diretório se não existir
    os.makedirs("confusion_matrix", exist_ok=True)

    # Define o nome do arquivo com base no nome do arquivo de saída
    base_name = os.path.splitext(os.path.basename(predicted_path))[0]
    output_path = os.path.join("confusion_matrix", f"{base_name}_confusion_matrix.png")

    plt.figure(figsize=(12, 10))
    sns.heatmap(matrix.astype(int), annot=True, fmt="d", cmap="Blues")
    plt.title("Confusion Matrix (gold vs predicted)")
    plt.xlabel("Predicted Tag")
    plt.ylabel("Gold Tag")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()