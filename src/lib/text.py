def normalize(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("El argumento debe ser un string")
    cleaned = text.lower().replace("\n", " ").replace("\t", " ").strip()
    while "  " in cleaned:
        cleaned = cleaned.replace("  ", " ")

    return cleaned


def tokenize(text: str) -> list[str]:
    if not isinstance(text, str):
        raise TypeError("Аргумент должен быть string")

    norm = normalize(text)
    if not norm:
        return []
    return norm.split(" ")


def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq


def top_n(freq: dict[str, int], n: int) -> list[tuple[str, int]]:
    if not isinstance(freq, dict):
        raise TypeError("freq должен быть словарем")

    if n <= 0:
        return []
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    return sorted_items[:n]
