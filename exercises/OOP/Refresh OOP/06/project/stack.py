from typing import List


class Stack:
    def __init__(self):
        self.data: list[str] = []

    def push(self, item: str) -> None:
        if isinstance(item, str):
            self.data.append(item)

    def pop(self) -> str:
        return self.data.pop() if len(self.data) > 0 else 'There is no data'

    def top(self) -> str:
        return self.data[-1] if len(self.data) > 0 else 'There is no data'

    def is_empty(self) -> bool:
        return len(self.data) == 0

    def __str__(self) -> str:
        return ', '.join((reversed(self.data)))