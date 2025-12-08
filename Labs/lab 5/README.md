# python_labs

## Лабораторная работа 5

### Задание A

<img width="1880" height="3446" alt="Tarea_A" src="https://github.com/user-attachments/assets/342e99f1-473e-4621-a251-7196d1b08b29" />


```
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
```
        
<img width="1046" height="131" alt="Tarea_A result" src="https://github.com/user-attachments/assets/068bfbf1-fe08-479d-8d5c-33be4041f138" />

### Задание B

<img width="1664" height="2762" alt="Tarea_B" src="https://github.com/user-attachments/assets/57edc4da-ca2e-423e-8196-ad0e85ae8fa3" />
 ```
import csv
from openpyxl import Workbook
from pathlib import Path

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Convierte CSV a XLSX usando openpyxl.
    - La primera fila del CSV es el encabezado.
    - La hoja se llama "Sheet1".
    - Ajusta ancho de columnas (minimo 8).
    """

    p = Path(csv_path)
    if not p.exists():
        raise FileNotFoundError("El archivo CSV no existe :(")

    if not csv_path.endswith(".csv"):
        raise ValueError("El archivo no tiene extension .csv, revisa eso")

    try:
        with open(csv_path, "r", encoding="utf-8") as f:
            lector = csv.reader(f)
            filas = list(lector)
    except Exception as e:
        raise ValueError("Error leyendo el CSV, tal vez está vacío o dañado: " + str(e))

    if not filas:
        raise ValueError("El CSV está vacío (no hay nada)")

    encabezado = filas[0]
    if not encabezado or all(c.strip() == "" for c in encabezado):
        raise ValueError("El CSV no tiene encabezado valido")

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    for fila in filas:
        ws.append(fila)

    try:
        for col in ws.columns:
            max_largo = 0
            letra = col[0].column_letter
            for celda in col:
                valor = str(celda.value) if celda.value is not None else ""
                if len(valor) > max_largo:
                    max_largo = len(valor)
            if max_largo < 8:
                max_largo = 8
            ws.column_dimensions[letra].width = max_largo + 1
    except Exception as e:
        print("No se pudo ajustar ancho de columnas, pero el excel igual sirve:", e)

    try:
        wb.save(xlsx_path)
        print("Archivo XLSX guardado en:", xlsx_path)
    except Exception as e:
        raise ValueError("No se pudo guardar el archivo XLSX: " + str(e))

if __name__ == "__main__":
    try:
        csv_to_xlsx("data/samples/people.csv", "data/out/people.xlsx")
    except Exception as e:
        print("Ocurrió un error:", e)

```


<img width="533" height="470" alt="Tarea_B result" src="https://github.com/user-attachments/assets/3fa8b510-01ee-4eeb-bef0-52a8addbd6ae" />





