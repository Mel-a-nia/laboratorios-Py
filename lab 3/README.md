# python_labs

## Лабораторная работа 3

### Задание A



```
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
        if word in freq:
            freq[word] = freq[word] + 1
        else:
            freq[word] = 1

    return freq
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    items = list(freq.items())
    sorted_items = sorted(items, key=lambda x: (-x[1], x[0]))
    top_n_items = sorted_items[:n]
    return top_n_items
text = "ПрИвЕт\nМИр\t"
print("normalize:", normalize(text))
text2 = normalize("emoji 😀 не слово")
print("tokenize:", tokenize(text2))
tokens = ["a", "b", "a", "c", "b", "a"]
freq = count_freq(tokens)
print("count_freq:", freq)
print("top_n:", top_n(freq, n=2))
```



### Задание B



```
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
        if word in freq:
            freq[word] = freq[word] + 1
        else:
            freq[word] = 1
    return freq

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    items = list(freq.items())
    sorted_items = sorted(items, key=lambda x: (-x[1], x[0]))
    top_n_items = sorted_items[:n]
    return top_n_items

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
```

