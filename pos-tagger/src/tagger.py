## src/tagger.py
import pickle
from collections import defaultdict, Counter
from nltk.tag import UnigramTagger, BigramTagger, TrigramTagger, DefaultTagger
from .utils import read_tagged_sentences


def train_unigram_tagger(train_path, model_path):
    sentences = read_tagged_sentences(train_path)
    # treina UnigramTagger com fallback DefaultTagger('NN')
    default = DefaultTagger('NN')
    uni_tagger = UnigramTagger(sentences, backoff=default)
    with open(model_path, 'wb') as f:
        pickle.dump(uni_tagger, f)
    print(f"Unigram model salvo em {model_path}")


def train_bigram_tagger(train_path, model_path):
    sentences = read_tagged_sentences(train_path)
    # fallback para substantivo 'NN' se não houver bigrama
    default = DefaultTagger('NN')
    bigram = BigramTagger(sentences, backoff=default)
    with open(model_path, 'wb') as f:
        pickle.dump(bigram, f)
    print(f"Bigram model salvo em {model_path}")


def train_trigram_tagger(train_path, model_path):
    sentences = read_tagged_sentences(train_path)
    default = DefaultTagger('NN')
    trigram = TrigramTagger(sentences, backoff=default)
    with open(model_path, 'wb') as f:
        pickle.dump(trigram, f)
    print(f"Trigram model salvo em {model_path}")

def train_trigram_tagger_backoff(train_path, model_path):

    # Carrega as sentenças anotadas
    sentences = read_tagged_sentences(train_path)

    # Tagger padrão para substantivos
    default_tagger = DefaultTagger('NN')

    # Unigram backoff
    unigram_tagger = UnigramTagger(sentences, backoff=default_tagger)

    # Bigram backoff para Unigram
    bigram_tagger = BigramTagger(sentences, backoff=unigram_tagger)

    # Trigram com cadeia de backoff
    trigram_tagger = TrigramTagger(sentences, backoff=bigram_tagger)

    # Salva o modelo treinado
    with open(model_path, 'wb') as f:
        pickle.dump(trigram_tagger, f)

    print(f"Trigram backoff model salvo em {model_path}")

def train_unigram_tagger_backoff(train_path, model_path):

    # Carrega as sentenças anotadas
    sentences = read_tagged_sentences(train_path)

    # Tagger padrão para substantivos
    default_tagger = DefaultTagger('NN')
    
    # Trigram com cadeia de backoff
    trigram_tagger = TrigramTagger(sentences, backoff=default_tagger)
    # Bigram backoff para Unigram
    bigram_tagger = BigramTagger(sentences, backoff=trigram_tagger)
    # Unigram backoff
    unigram_tagger = UnigramTagger(sentences, backoff=bigram_tagger)

    # Salva o modelo treinado
    with open(model_path, 'wb') as f:
        pickle.dump(unigram_tagger, f)

    print(f"unigram backoff model salvo em {model_path}")


def tag_with_model(test_path, model_path, output_path):
    sentences = read_tagged_sentences(test_path)
    with open(model_path, 'rb') as f:
        tagger = pickle.load(f)

    output_lines = []
    for sent in sentences:
        words = [w for w, _ in sent]
        tagged = tagger.tag(words)
        output_lines.append(" ".join(f"{w}_{t}" for w, t in tagged))

    with open(output_path, 'w') as f:
        for line in output_lines:
            f.write(line + "\n")
    print(f"Predições salvas em {output_path}")
