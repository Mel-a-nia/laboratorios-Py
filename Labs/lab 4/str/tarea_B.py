import sys
import csv
from pathlib import Path
from collections import Counter

in_file = "data/input.txt"
out_file = "data/report.csv"
encoding = "utf-8"
for i in range(len(sys.argv)):
    if sys.argv[i] == "--in" and i + 1 < len(sys.argv):
        in_file = sys.argv[i + 1]
    if sys.argv[i] == "--out" and i + 1 < len(sys.argv):
        out_file = sys.argv[i + 1]
    if sys.argv[i] == "--encoding" and i + 1 < len(sys.argv):
        encoding = sys.argv[i + 1]
try:
    with open(in_file, "r", encoding=encoding) as f:
        text = f.read()
except FileNotFoundError:
    print("Ошибка: файл не найден ->", in_file)
    sys.exit(1)
except UnicodeDecodeError:
    print("Ошибка кодировки. Попробуйте указать параметр --encoding cp1251")
    sys.exit(1)
text = text.casefold()
text = text.replace("ё", "е")
text = text.replace("\t", " ")
text = text.replace("\n", " ")
text = text.replace("\r", " ")
while "  " in text:
    text = text.replace("  ", " ")
import re

tokens = re.findall(r"\w+(?:-\w+)*", text)
freq = Counter(tokens)
sorted_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
p = Path(out_file)
p.parent.mkdir(parents=True, exist_ok=True)
with open(out_file, "w", encoding="utf-8", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["word", "count"])
    for w, c in sorted_words:
        writer.writerow([w, c])
print("Всего слов:", len(tokens))
print("Уникальных слов:", len(freq))
top_n = 5
print("Топ-5:")
for i, (w, c) in enumerate(sorted_words[:top_n]):
    print(f"{i+1}. {w} ({c})")
if len(tokens) == 0:
    print("Файл пуст , создается только заголовок CSV.")
