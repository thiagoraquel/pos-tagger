## main.py
import argparse
from src.tagger import (
    train_unigram_tagger,
    train_bigram_tagger,
    train_trigram_tagger,
    train_trigram_tagger_backoff,
    train_unigram_tagger_backoff,
    tag_with_model
)
from src.evaluate import evaluate_accuracy, generate_confusion_matrix

def main():
    parser = argparse.ArgumentParser(
        description="""
        Programa para treinar, usar e avaliar um tagger baseado em unigramas, bigramas ou trigramas.

        Modos de operação:
        train    - Treina o modelo a partir de um corpus anotado
                    Requer: --input, --model, --model-type

        tag      - Usa um modelo treinado para etiquetar frases
                    Requer: --input, --model, --output

        evaluate - Compara as tags geradas com as verdadeiras
                    Requer: --output e --gold

        Exemplos de uso:
        python main.py --mode train --model-type bigram --input data/train --model outputs/bigram_model.pkl
        python main.py --mode tag   --input data/dev   --model outputs/bigram_model.pkl --output outputs/predictions_dev.txt
        python main.py --mode evaluate --output outputs/predictions_dev.txt --gold data/dev
        """
    )
    parser.add_argument('--mode', choices=['train', 'tag', 'evaluate'], required=True)
    parser.add_argument('--model-type', choices=['unigram', 'bigram', 'trigram', 'trigram_backoff', 'unigram_backoff'], default='unigram', help='Tipo de modelo para treinar (somente em --mode train)')
    parser.add_argument('--input', help='Caminho para o arquivo de entrada')
    parser.add_argument('--model', help='Caminho para salvar/carregar o modelo')
    parser.add_argument('--output', help='Arquivo de saída (predições)')
    parser.add_argument('--gold', help='Arquivo com as tags verdadeiras (para avaliação)')
    args = parser.parse_args()

    if args.mode == 'train':
        if args.model_type == 'unigram':
            train_unigram_tagger(args.input, args.model)
        elif args.model_type == 'bigram':
            train_bigram_tagger(args.input, args.model)
        elif args.model_type == 'trigram':
            train_trigram_tagger(args.input, args.model)
        elif args.model_type == 'trigram_backoff':
            train_trigram_tagger_backoff(args.input, args.model)
        elif args.model_type == 'unigram_backoff':
            train_unigram_tagger_backoff(args.input, args.model)
        else:
            print("nothing")
    elif args.mode == 'tag':
        tag_with_model(args.input, args.model, args.output)

    elif args.mode == 'evaluate':
        evaluate_accuracy(args.output, args.gold)
        generate_confusion_matrix(args.output, args.gold)

if __name__ == '__main__':
    main()
