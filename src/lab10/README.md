# python_labs

## Лабораторная работа 10

### Задание A (structures)

<img width="1172" height="2838" alt="structures" src="https://github.com/user-attachments/assets/ac76d368-9823-4e21-bc62-996339977c8c" />


```
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
def write_csv(rows: list[list | tuple], path: str | Path, header: tuple[str, ...] | None = None) -> None:
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
        write_csv([("word","count"),("test",3)], "data/check.csv")
    except Exception as e:
        print("Ошибка при записи CSV:", e)

```



<img width="1112" height="255" alt="structures_result" src="https://github.com/user-attachments/assets/9e4187ef-fc56-41a8-8379-c5bf87bfefa8" />




### Задание B (linked_list)



<img width="1280" height="3750" alt="Linked_list" src="https://github.com/user-attachments/assets/665eddb3-1c42-4b62-bddb-93af07002547" />




```
from typing import Any, Iterator
class Node:
    """Узел односвязного списка"""

    def __init__(self, value: Any, next: "Node | None" = None):
        self.value = value
        self.next = next
class SinglyLinkedList:
    """Односвязный список"""

    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None
        self._size: int = 0
    def append(self, value: Any) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            assert self.tail is not None
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1
    def prepend(self, value: Any) -> None:
        new_node = Node(value, next=self.head)
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self._size += 1
    def insert(self, idx: int, value: Any) -> None:
        if idx < 0 or idx > self._size:
            raise IndexError("index out of range")
        if idx == 0:
            self.prepend(value)
            return
        if idx == self._size:
            self.append(value)
            return
        current = self.head
        for _ in range(idx - 1):
            assert current is not None
            current = current.next
        new_node = Node(value, next=current.next)
        current.next = new_node
        self._size += 1
    def remove(self, value: Any) -> None:
        current = self.head
        prev = None
        while current is not None:
            if current.value == value:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                if current == self.tail:
                    self.tail = prev
                self._size -= 1
                return
            prev = current
            current = current.next
    def __iter__(self) -> Iterator[Any]:
        current = self.head
        while current is not None:
            yield current.value
            current = current.next
    def __len__(self) -> int:
        return self._size
    def __repr__(self) -> str:
        return f"SinglyLinkedList({list(self)})"
    def pretty(self) -> str:
        parts = []
        current = self.head
        while current is not None:
            parts.append(f"[{current.value}]")
            current = current.next
        parts.append("None")
        return " -> ".join(parts)
if __name__ == "__main__":
    lst = SinglyLinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    print(lst)
    lst.prepend(0)
    print(lst)
    lst.insert(2, 99)
    print(lst)
    print("Length:", len(lst))
    for x in lst:
        print(x)
```

<img width="851" height="241" alt="Linked_list_result" src="https://github.com/user-attachments/assets/d18d0fbf-c8c7-480f-bb4e-31b0ede1fc9f" />


