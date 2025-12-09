# python_labs

## Лабораторная работа 7

### Задание A (text.py)


<img width="1418" height="1698" alt="text" src="https://github.com/user-attachments/assets/0b4d3a1a-5c7a-431c-9442-eb9ca63ccf41" />


```
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

```

### Pytest

<img width="814" height="170" alt="pytest" src="https://github.com/user-attachments/assets/17dcace8-550e-4aeb-b526-8a7cf6d04c7a" />


### Задание test_text

<img width="1280" height="1394" alt="test_text" src="https://github.com/user-attachments/assets/e4570f02-f631-4292-b74c-df266f76b42f" />



 ```
import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(
    ("src", "exp"),
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("Hello  WORLD", "hello world"),
        ("  doble   espacios ", "doble espacios"),
        ("", ""),
    ],
)
def test_normalize(src, exp):
    assert normalize(src) == exp


def test_tokenize_and_count_freq():
    txt = "a a b c a"
    tokens = tokenize(txt)
    assert tokens == ["a", "a", "b", "c", "a"]
    freq = count_freq(tokens)
    assert freq == {"a": 3, "b": 1, "c": 1}


def test_top_n_tie_breaker():
    freq = {"apple": 2, "banana": 2, "cherry": 1}
    assert top_n(freq, 2) == [("apple", 2), ("banana", 2)]

```

### Pytest test_text 

<img width="828" height="159" alt="pytest text" src="https://github.com/user-attachments/assets/3b1f2994-9cbb-4913-8bef-2fb5a1e59b2f" />

### Задание test_json_csv

<img width="1448" height="1660" alt="test_json_csv" src="https://github.com/user-attachments/assets/4cfa14e9-2b20-4d1e-babc-b0dcb840c20a" />


```
import json
import csv
import pytest
from pathlib import Path
from src.lab05.json_csv import json_to_csv, csv_to_json


def test_json_to_csv_and_back(tmp_path: Path):
    src = tmp_path / "in.json"
    dst = tmp_path / "out.csv"
    data = [{"name": "Alice", "age": 22}, {"name": "Bob", "age": 25}]
    src.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())
    dst2 = tmp_path / "out2.json"
    csv_to_json(str(dst), str(dst2))
    out_data = json.loads(dst2.read_text(encoding="utf-8"))
    assert len(out_data) == 2


def test_json_invalid_raises(tmp_path: Path):
    bad = tmp_path / "bad.json"
    bad.write_text("not json", encoding="utf-8")
    with pytest.raises(ValueError):
        json_to_csv(str(bad), str(tmp_path / "o.csv"))


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        json_to_csv("no_existe.json", "out.csv")

```

### Pytest --cov

<img width="1190" height="670" alt="pytest --cov=src --cov-report=term-missing" src="https://github.com/user-attachments/assets/82d2ae3e-1c20-468b-acf7-6e9f37f7ee95" />

### Black .

<img width="595" height="234" alt="black " src="https://github.com/user-attachments/assets/58b93680-a10c-48c3-a463-fd9f42e76218" />

### Black --check .

<img width="758" height="154" alt="black --check" src="https://github.com/user-attachments/assets/2552b450-9213-4cf2-8f05-e61dd447a97f" />


### Test manual

<img width="1142" height="558" alt="test_manual" src="https://github.com/user-attachments/assets/c2f93813-8e5c-4df9-876b-e65b0b2b8699" />

<img width="618" height="672" alt="prueba json" src="https://github.com/user-attachments/assets/cb3bf1b7-f879-4e87-aa03-e119ed7556fa" />

