from node import Node


class Deque:
    """Deque model."""

    def __init__(self) -> None:
        self.__head: Node | None = None
        self.__tail: Node | None = None
        self.__length: int = 0

    def __len__(self) -> int:
        """Return quantity of nodes in deque."""
        return self.__length

    def __str__(self) -> str:
        """View all nodes in deque."""
        if not self.__head or not self.__tail or self.__length == 0:
            return '{}()'.format(type(self).__name__)

        nodes: list = []
        node: Node = self.__head
        while node:
            nodes.append(node)
            node = node.next

        return ', '.join(str(node) for node in nodes)
