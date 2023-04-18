from __future__ import annotations
from typing import Any


class Heap:
    """Модель кучи, основанной на списке."""

    def __init__(self) -> None:
        self.values = []
        self.size = 0

    def sift_up(self, i: int) -> None:
        """Просеивание кучи вверх."""
        while i != 0 and self.values[i] < self.values[(i - 1) // 2]:
            self.values[i], self.values[(i - 1) // 2] = (
                self.values[(i - 1) // 2], self.values[i]
            )

    def push_back(self, item: Any) -> None:
        """Вставка элемента в конец, с дальнейшим просеиванием."""
        self.values.append(item)
        self.size += 1
        self.sift_up(self.size - 1)

    def sift_down(self, i: int) -> None:
        """Просеивание кучи вниз."""
        while 2*i + 1 < self.size:
            j = i
            if self.values[2*i + 1] < self.values[i]:
                j = 2*i + 1
            if (
                2*i + 2 < self.size
                and self.values[2*i + 2] < self.values[j]
            ):
                j = 2*i + 2
            if i == j:
                break
            self.values[i], self.values[j] = self.values[j], self.values[i]

    def pop_min(self) -> Any:
        """
        Получение наименьшего элемента,
        с последующем удалением его из кучи.
        """
        if not self.size:
            return None

        item = self.values[0]
        self.values[0] = self.values[-1]
        self.values.pop()
        self.size -= 1
        self.sift_down(0)
        return item

    def heapify(self, items: list) -> Heap:
        """Преобразование списка в кучу."""
        self.values = items[:]
        self.size = len(items)
        for i in reversed(range(self.size // 2)):
            self.sift_down(i)
        return self

    def heap_sort(self) -> list:
        """Сортировка списка с помощью кучи."""
        sorted_list: list = []
        while self.size:
            sorted_list.append(self.pop_min())
        return sorted_list


if __name__ == '__main__':

    heap: Heap = Heap()
    items: list = [12, 43, 2, 8, 54, 5]

    heap.heapify(items)
    assert heap.heap_sort() == sorted(items)
