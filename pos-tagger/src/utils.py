def read_tagged_sentences(filepath):
    """Lê o corpus no formato word_tag separado por espaços."""
    sentences = []
    with open(filepath, 'r') as f:
        for line in f:
            pairs = line.strip().split()
            sentence = [tuple(pair.rsplit('_', 1)) for pair in pairs if '_' in pair]
            sentences.append(sentence)
    return sentences
