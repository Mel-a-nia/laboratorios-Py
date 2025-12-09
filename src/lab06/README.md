# python_labs

## Лабораторная работа 6

### Задание cli_text
<img width="1542" height="3446" alt="cli_convert" src="https://github.com/user-attachments/assets/fd12fecd-4097-4146-b007-25e1e91fc7f4" />
```
import argparse
from pathlib import Path


def json_to_csv(json_path, csv_path):
    import json, csv

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список объектов")
    if len(data) == 0:
        raise ValueError("Файл JSON пуст.")
    keys = data[0].keys()
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)


def csv_to_json(csv_path, json_path):
    import csv, json

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = list(reader)
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def csv_to_xlsx(csv_path, xlsx_path):
    import csv
    from openpyxl import Workbook

    wb = Workbook()
    ws = wb.active
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            ws.append(row)
    wb.save(xlsx_path)


def main():
    parser = argparse.ArgumentParser(description="Преобразователи данных-lab06")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv", help="Конвертировать JSON в CSV")
    p1.add_argument("--in", dest="input", required=True)
    p1.add_argument("--out", dest="output", required=True)

    p2 = sub.add_parser("csv2json", help="Конвертировать CSV в JSON")
    p2.add_argument("--in", dest="input", required=True)
    p2.add_argument("--out", dest="output", required=True)

    p3 = sub.add_parser("csv2xlsx", help="Конвертировать CSV в XLSX")
    p3.add_argument("--in", dest="input", required=True)
    p3.add_argument("--out", dest="output", required=True)

    args = parser.parse_args()

    inp = Path(args.input)
    outp = Path(args.output)

    if not inp.exists():
        raise FileNotFoundError(f"Файл не существует: {inp}")

    if args.cmd == "json2csv":
        json_to_csv(inp, outp)
        print("Преобразование JSON - CSV завершено")

    elif args.cmd == "csv2json":
        csv_to_json(inp, outp)
        print("Преобразование CSV - JSON завершено.")

    elif args.cmd == "csv2xlsx":
        csv_to_xlsx(inp, outp)
        print("Конвертация CSV - XLSX завершена.")


if __name__ == "__main__":
    main()

```
#### Result
<img width="605" height="336" alt="cli_convert --help" src="https://github.com/user-attachments/assets/3881eda4-82db-4e0d-8788-ba6e9457a253" />
<img width="548" height="234" alt="cli_convert json2cvs --help" src="https://github.com/user-attachments/assets/3ef4a5b7-9f92-4a9a-97f5-1580a279e825" />
<img width="651" height="243" alt="cli_convert csv2xlsx --help" src="https://github.com/user-attachments/assets/8d183034-bac3-459e-8aaa-552ea4342162" />
<img width="569" height="220" alt="cli_convert csv2json --help" src="https://github.com/user-attachments/assets/81e1e168-facc-4301-bdde-c756096176ac" />
<img width="1254" height="663" alt="cli_convert json2csv --in" src="https://github.com/user-attachments/assets/b73e294d-aff6-4aaf-893a-78eafb36aeb3" />
<img width="635" height="176" alt="cli_convert csv2xlsx --in" src="https://github.com/user-attachments/assets/0b8ffa64-a872-4fc7-b111-db6cbab7ca5d" />
<img width="1236" height="662" alt="cli_convert csv2json --in" src="https://github.com/user-attachments/assets/cb439c70-6cd4-4d1c-8d6f-20399bbc756e" />

### Задание cli_text
<img width="1526" height="2724" alt="cli_text" src="https://github.com/user-attachments/assets/5cbc2fb8-97d6-4da1-898b-b4b0a0c81d30" />
 ```
import argparse
from pathlib import Path


def load_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def count_words(text):
    words = {}
    for w in text.lower().split():
        w = "".join(c for c in w if c.isalnum())
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


```

#### Result 
<img width="531" height="370" alt="cli_text py --help" src="https://github.com/user-attachments/assets/a6623800-c53c-498d-8b1f-b9ed879b5918" />
<img width="1271" height="645" alt="cli_text --help" src="https://github.com/user-attachments/assets/e3be8215-982d-40d5-b68b-da71f25fb0bb" />
<img width="578" height="231" alt="cli_text cat --help" src="https://github.com/user-attachments/assets/698c4c5a-044c-4dbd-8e99-eb7620653820" />
<img width="573" height="225" alt="cli_text stast --help" src="https://github.com/user-attachments/assets/c4e50a8f-02e7-4e09-9354-ec3f89e3fe7b" />
<img width="817" height="761" alt="cli_text cat --input" src="https://github.com/user-attachments/assets/5821714c-4a6c-4176-bf60-8339f4a4c768" />
<img width="499" height="153" alt="cli_text cat--input data check --top 5" src="https://github.com/user-attachments/assets/be0f7283-a28c-4bc3-9386-a501e09e0a9c" />
<img width="537" height="177" alt="cli_text cat--input data check" src="https://github.com/user-attachments/assets/6f75fcf7-ac44-4fde-9c89-5d85e2513f51" />
<img width="652" height="186" alt="cli_text cat--input data check-n" src="https://github.com/user-attachments/assets/6880ee20-5ce3-4804-8e0b-fb21b233a3b0" />
<img width="557" height="297" alt="cli_text cat--input data samples people -n" src="https://github.com/user-attachments/assets/d725db2b-9784-4ee2-bd2c-eba0639784c0" />
<img width="1296" height="450" alt="cli_text stats --input data check --top5" src="https://github.com/user-attachments/assets/c7434121-af88-4e6f-98a3-396603f7a9f4" />
<img width="560" height="232" alt="cli_text stats --input sata samples people --top5" src="https://github.com/user-attachments/assets/ea160913-0103-4535-97c8-cdc6682c66bb" />













