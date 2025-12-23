from collections import deque
from typing import Any
class Stack:
    """Стек (LIFO) на базе list"""

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
