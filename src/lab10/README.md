# python_labs

## Лабораторная работа 10

### Задание A (structures)

<img width="1172" height="2838" alt="structures" src="https://github.com/user-attachments/assets/ac76d368-9823-4e21-bc62-996339977c8c" />


```
from collections import deque
from typing import Any
class Stack:

    def __init__(self):
        self._data: list[Any] = []

    def push(self, item: Any) -> None:
        self._data.append(item)

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self) -> Any | None:
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)


class Queue:
    """Очередь (FIFO) на базе collections.deque"""

    def __init__(self):
        self._data: deque[Any] = deque()
    def enqueue(self, item: Any) -> None:
        self._data.append(item)
    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()
    def peek(self) -> Any | None:
        if self.is_empty():
            return None
        return self._data[0]
    def is_empty(self) -> bool:
        return len(self._data) == 0
    def __len__(self) -> int:
        return len(self._data)
if __name__ == "__main__":
    s = Stack()
    print("Stack vacío:", s.is_empty())
    s.push(10)
    s.push(20)
    s.push(30)
    print("Peek:", s.peek())
    print("Pop:", s.pop())
    print("Tamaño:", len(s))
    print("Vacío:", s.is_empty())
    print("----")
    q = Queue()
    q.enqueue("a")
    q.enqueue("b")
    q.enqueue("c")
    print("Peek:", q.peek())
    print("Dequeue:", q.dequeue())
    print("Tamaño:", len(q))
    print("Vacía:", q.is_empty())


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


