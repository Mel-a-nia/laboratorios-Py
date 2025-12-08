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
    parser = argparse.ArgumentParser(description="Преобразователи данных-lab6")
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
