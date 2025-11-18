import json
import csv
from pathlib import Path
def json_to_csv(json_path: str, csv_path: str) -> None:
    try:
        if not Path(json_path).exists():
            raise FileNotFoundError(f"El archivo {json_path} no existe!")
        if not json_path.endswith(".json"):
            raise ValueError("El archivo no es JSON!")
        with open(json_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                raise ValueError("El archivo JSON esta vacio o es invalido :(")
        if not isinstance(data, list) or len(data) == 0:
            raise ValueError("El JSON no contiene una lista de diccionarios o está vacio")
        for item in data:
            fieldnames = []
            if isinstance(item, dict):
                for key in item.keys():
                    if key not in fieldnames:
                        fieldnames.append(key)
            else:
                raise ValueError("El JSON no tiene un formato correcto (no es lista de diccionarios)")
        with open(csv_path, "w", encoding="utf-8", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for item in data:
                row = {}
                for key in fieldnames:
                    if key in item:
                        row[key] = item[key]
                    else:
                        row[key] = ""
                writer.writerow(row)
    except FileNotFoundError as e:
        raise e
    except ValueError as e:
        raise e
    except Exception as e:
        raise ValueError(f"Ocurrio un error raro: {e}")
def csv_to_json(csv_path: str, json_path: str) -> None:
    try:
        if not Path(csv_path).exists():
            raise FileNotFoundError(f"El archivo {csv_path} no existe!")
        if not csv_path.endswith(".csv"):
            raise ValueError("El archivo no es CSV!")
        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames is None:
                raise ValueError("El CSV no tiene encabezado!")
            data = []
            for row in reader:
                new_row = {}
                for k, v in row.items():
                    if v is None:
                        new_row[k] = ""
                    else:
                        new_row[k] = v
                data.append(new_row)
        if len(data) == 0:
            raise ValueError("El CSV esta vacio!")
        with open(json_path, "w", encoding="utf-8") as fjson:
            json.dump(data, fjson, ensure_ascii=False, indent=2)
    except FileNotFoundError as e:
        raise e
    except ValueError as e:
        raise e
    except Exception as e:
        raise ValueError(f"Ocurrio un error inesperado: {e}")
if __name__ == "__main__":
    print("Convirtiendo JSON a CSV...")
    try:
        json_to_csv("data/samples/people.json", "data/out/people_from_json.csv")
    except Exception as e:
        print("Error en json_to_csv:", e)

    print("Convirtiendo CSV a JSON...")
    try:
        csv_to_json("data/samples/people.csv", "data/out/people_from_csv.json")
    except Exception as e:
        print("Error en csv_to_json:", e)
