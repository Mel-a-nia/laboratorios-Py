import csv
from pathlib import Path


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Функция открывает текстовый файл и возвращает содержимое как одну строку.
    По умолчанию используется кодировка UTF-8.
    Если нужно, пользователь может указать другую кодировку, например: encoding="cp1251".

    Пример:
        text = read_text("data/input.txt")
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Файл не найден: {path}")
    try:
        with p.open("r", encoding=encoding) as f:
            contenido = f.read()
            if contenido == "":
                return ""
            else:
                return contenido
    except UnicodeDecodeError:
        raise UnicodeDecodeError("Ошибка декодирования! Попробуйте другую кодировку.")


def ensure_parent_dir(path: str | Path) -> None:
    """
    Создает родительские директории, если их нет.
    Это удобно перед записью CSV.
    """
    p = Path(path)
    folder = p.parent
    if not folder.exists():
        print(f"Создаю директорию: {folder}")
        folder.mkdir(parents=True, exist_ok=True)


def write_csv(
    rows: list[list | tuple], path: str | Path, header: tuple[str, ...] | None = None
) -> None:
    """
    Создает CSV-файл с разделителем ','.
    Если передан header, записывает его первой строкой.
    Проверяет, что все строки одинаковой длины (иначе ValueError).

    Пример:
        write_csv([("word","count"),("test",3)], "data/check.csv")
    """
    ensure_parent_dir(path)
    p = Path(path)
    if rows is None:
        rows = []
    if len(rows) > 1:
        primera = len(rows[0])
        for r in rows:
            if len(r) != primera:
                raise ValueError("Не все строки одинаковой длины!")
    try:
        with p.open("w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            if header is not None:
                writer.writerow(header)
            for fila in rows:
                writer.writerow(fila)
            print(f"Файл '{path}' успешно записан!")
    except Exception as e:
        print("Ошибка при записи CSV:", e)


if __name__ == "__main__":
    print("=== Тест функции read_text ===")
    try:
        txt = read_text("data/input.txt")
        print("Содержимое файла:")
        print(txt)
    except Exception as e:
        print("Ошибка при чтении файла:", e)
    print("\n=== Тест функции write_csv ===")
    try:
        write_csv([("word", "count"), ("test", 3)], "data/check.csv")
    except Exception as e:
        print("Ошибка при записи CSV:", e)
