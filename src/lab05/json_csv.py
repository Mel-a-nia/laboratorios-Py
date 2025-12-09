import json
import csv
import os


def json_to_csv(src_path: str, dst_path: str):
    if not os.path.exists(src_path):
        raise FileNotFoundError(f"File not found: {src_path}")

    try:
        with open(src_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        raise ValueError("Invalid JSON input")

    if not isinstance(data, list):
        raise ValueError("JSON must contain a list of objects")

    if len(data) == 0:
        with open(dst_path, "w", newline="", encoding="utf-8") as f:
            pass
        return

    headers = list(data[0].keys())

    with open(dst_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def csv_to_json(src_path: str, dst_path: str):
    if not os.path.exists(src_path):
        raise FileNotFoundError(f"File not found: {src_path}")

    try:
        with open(src_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            data = list(reader)
    except Exception:
        raise ValueError("Invalid CSV input")
    for row in data:
        for key, value in row.items():
            if value.isdigit():
                row[key] = int(value)
    with open(dst_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
