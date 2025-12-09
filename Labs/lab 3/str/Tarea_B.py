import sys
from lab import normalize, tokenize, count_freq, top_n


def main():
    text_input = sys.stdin.read()
    norm_text = normalize(text_input)
    tokens = tokenize(norm_text)
    freq = count_freq(tokens)
    print("Всего слов:", len(tokens))
    print("Уникальных слов:", len(freq))
    print("Топ-5:")
    top5 = top_n(freq, n=5)
    for word, count in top5:
        print(f"{word}:{count}")
    main()
