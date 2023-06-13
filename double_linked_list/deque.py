from node import Node
from typing import Any


class Deque:
    """Deque model."""

    def __init__(self) -> None:
        self.__head: Node | None = None
        self.__tail: Node | None = None
        self.__length: int = 0

    def is_empty(self) -> bool:
        """Return true if deque is empty."""
        return not self.__head or not self.__tail or self.__length == 0

    def __len__(self) -> int:
        """Return quantity of nodes in deque."""
        return self.__length

    def __str__(self) -> str:
        """View all nodes in deque."""
        if self.is_empty():
            return '{}()'.format(type(self).__name__)

        nodes: list = []
        node: Node = self.__head
        while node:
            nodes.append(node.key)
            node = node.next

        return ', '.join(str(key) for key in nodes)

    def push_back(self, item: Any) -> None:
        """Push item in the end of deque."""
        if self.is_empty():
            self.__push(item)
            return

        node: Node = Node(item, self.__tail)
        self.__tail.next = node
        self.__tail = self.__tail.next
        self.__length += 1

    def push_front(self, item: Any) -> None:
        """Push item in front of deque."""
        if self.is_empty():
            self.__push(item)
            return

    def __push(self, item: Any) -> None:
        """Push item in empty deque."""
        if not self.__head or not self.__tail:
            self.__head = self.__tail = Node(item)
            self.__length += 1
            return
