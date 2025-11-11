import sys
import re
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    result = text
    if casefold:
        result = result.casefold()
    if yo2e:
        result = result.replace("ё", "е").replace("Ё", "Е")
    result = result.replace("\t", " ")
    result = result.replace("\r", " ")
    result = result.replace("\n", " ")
    while "  " in result:
        result = result.replace("  ", " ")
    result = result.strip()
    return result
def tokenize(text: str) -> list[str]:
    pattern = r"\w+(?:-\w+)*"
    tokens = re.findall(pattern, text)
    return tokens
def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for word in tokens:
        freq[word] = freq.get(word, 0) + 1
    return freq
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    items = list(freq.items())
    sorted_items = sorted(items, key=lambda x: (-x[1], x[0]))
    top_n_items = sorted_items[:n]
    return top_n_items
def main():
    if len(sys.argv) > 1:
        text_input = " ".join(sys.argv[1:])
    else:
        print("Escribe o pega el texto (Ctrl+Z y Enter):")
        text_input = sys.stdin.read()
    if not text_input.strip():
        print("No se ingresó texto.")
        return
    norm_text = normalize(text_input)
    tokens = tokenize(norm_text)
    freq = count_freq(tokens)

    print("Всего слов:", len(tokens))
    print("Уникальных слов:", len(freq))
    print("Топ-5:")
    for word, count in top_n(freq, n=5):
        print(f"{word}:{count}")
if __name__ == "__main__":
    main()

