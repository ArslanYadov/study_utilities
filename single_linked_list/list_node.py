class Node:
    """Класс узла."""
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class ListNode:
    """Класс односвязного списка."""
    head: Node | None = None
    length: int = 0

    def __getitem__(self, key: int) -> int:
        """Метод для получения значения по индексу."""
        if not isinstance(key, int):
            raise TypeError('Индекс должен быть целым числом.')

        i: int = 0
        node: Node | None = self.head

        while i < key:
            node = node.next
            i += 1

        return node.val

    def __len__(self) -> int:
        """Метод отображения количества узлов."""
        return self.length

    def __str__(self) -> str:
        """Метод отображения односвязного списка."""
        node: Node | None = self.head

        line: str = '['
        while node.next:
            line += str(node.val) + ', '
            node = node.next
        line += str(node.val) + ']'
        return line

    def append(self, val: int) -> None:
        """Метод добавления нового узла в конец списка."""
        if self.head is None:
            self.head = Node(val)
            self.length += 1 
            return

        node: Node = self.head
        while node.next:
            node = node.next
        node.next = Node(val)
        self.length += 1 
        return

    def insert(self, key: int, val: int) -> None:
        """Метод вставки узла в односвязный список."""
        if key == 0:
            temp_head = self.head
            self.head = Node(val, next=temp_head)
            self.length += 1 
            return

        i: int = 0
        node: Node | None = self.head
        prev_node: Node | None = self.head

        while i < key:
            prev_node = node
            node = node.next
            i += 1
        prev_node.next = Node(val, next=node)
        self.length += 1 
        return
