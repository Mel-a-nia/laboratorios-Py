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
        csv_to_xlsx("lab 5/str/people.csv", "people.xlsx")
    except Exception as e:
        print("Ocurrió un error:", e)
