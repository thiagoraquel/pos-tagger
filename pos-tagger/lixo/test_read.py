from src.utils import read_tagged_sentences

gold = read_tagged_sentences("data/dev")
pred = read_tagged_sentences("outputs/predictions_converted.txt")

print("Gold ex:", gold[0][:20])
print("Pred ex:", pred[0][:20])
