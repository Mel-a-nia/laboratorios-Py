import argparse
from pathlib import Path
def load_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
def count_words(text):
    words = {}
    for w in text.lower().split():
        w = ''.join(c for c in w if c.isalnum())
        if not w:
          continue
        words[w] = words.get(w, 0) + 1
    return words
def top_words(words_dict, n=5):
    return sorted(words_dict.items(), key=lambda x: x[1], reverse=True)[:n]
def main():
    parser = argparse.ArgumentParser(description="Текстовые инструменты-lab06")
    sub = parser.add_subparsers(dest="cmd")
    p_cat = sub.add_parser("cat", help="Отобразить файл построчно")
    p_cat.add_argument("--input", required=True)
    p_cat.add_argument("-n", action="store_true", help="Числовые линии")

    p_stats = sub.add_parser("stats", help="Top слова в тексте")
    p_stats.add_argument("--input", required=True)
    p_stats.add_argument("--top", type=int, default=5)

    args = parser.parse_args()
    if args.cmd == "cat":
        path = Path(args.input)
        if not path.exists():
            raise FileNotFoundError(f"Файл не существует: {path}")
        
        with open(path, "r", encoding="utf-8") as f:
            for i, line in enumerate(f, 1):
                if args.n:
                    print(f"{i}: {line.rstrip()}")
                else:
                    print(line.rstrip())

    elif args.cmd == "stats":
        path = Path(args.input)
        if not path.exists():
            raise FileNotFoundError(f"Файл не существует: {path}")
        
        text = load_text(path)
        frec = count_words(text)
        top_list = top_words(frec, args.top)


        print(f"Top {args.top}наиболее часто встречающиеся слова:\n")
        for w, c in top_list:
            print(f"{w}: {c}")


if __name__ == "__main__":
    main()