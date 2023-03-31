class Node:
    """Простая модель вершины бинарного дерева."""

    def __init__(self, value=None, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def insert(self, value) -> None:
        """Вставка нового узла в дерево."""
        if not self.value:
            self.value = value
            return

        if value < self.value:
            if self.left:
                self.left.insert(value)
                return
            self.left = Node(value)
            return

        if value >= self.value:
            if self.right:
                self.right.insert(value)
                return
            self.right = Node(value)
