class Node:
    """Модель узла."""

    def __init__(self, value=None, next=None) -> None:
        self.value = value
        self.next = next


class LinkedList:
    """Модель односвязного списка."""

    def __init__(self) -> None:
        self.__head = None
        self.__length = 0

    def __len__(self) -> int:
        """Возвращает длину односвязного списка."""
        return self.__length

    def is_empty(self) -> bool:
        """Проверка пустого списка."""
        return len(self) == 0 and not self.__head

    def __push(self, item) -> None:
        """Вставка элемента в пустой список."""
        self.__head = Node(item)
        self.__length += 1
        return

    def convert(self, iterable, reverse=False) -> None:
        """Конвертация итерируемого объекта в односвязный список."""
        if not reverse:
            for item in iterable:
                self.push_back(item)
            return

        for item in iterable:
            self.push_front(item)
        return

    def push_back(self, item) -> None:
        """Вставка элемента в конец односвязного списка."""
        if self.is_empty():
            self.__push(item)
            return

        node: Node = self.__head
        while node.next:
            node = node.next
        node.next = Node(item)
        self.__length += 1
        return

    def push_front(self, item) -> None:
        """Вставка элемента в начало односвязного списка."""
        if self.is_empty():
            self.__push(item)
            return

        node: Node = Node(item, self.__head)
        self.__head = node
        self.__length += 1
        return

    def __str__(self) -> str:
        if self.is_empty():
            return '[]'

        nodes: list = []
        node: Node = self.__head
        while node:
            nodes.append(node.value)
            node = node.next
        return ', '.join(str(val) for val in nodes)
