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
