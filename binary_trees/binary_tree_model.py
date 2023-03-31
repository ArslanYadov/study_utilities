from __future__ import annotations


class Node:
    """Простая модель бинарного дерева."""

    def __init__(self, value=None, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def find_min(self) -> Node:
        """Поиск минимального узла."""
        if not self.left:
            return self
        return self.left.find_min()

    def find_max(self) -> Node:
        """Поиск максимального узла."""
        if not self.right:
            return self
        return self.right.find_max()

    def remove(self, key) -> Node:
        """Удаление узла из дерева."""
        if not self:
            return self

        if key < self.value:
            self.left = self.left.remove(key)

        elif key > self.value:
            self.right = self.right.remove(key)

        elif self.left and self.right:
            self.value = self.right.find_min().value
            self.right = self.right.remove(self.value)

        else:
            if self.left:
                self = self.left
            elif self.right:
                self = self.right
            else:
                self = None

        return self

    def insert(self, key) -> None:
        """Вставка нового узла в дерево."""
        if not self.value:
            self.value = key
            return

        if key < self.value:
            if self.left:
                self.left.insert(key)
                return
            self.left = Node(key)
            return

        if key >= self.value:
            if self.right:
                self.right.insert(key)
                return
            self.right = Node(key)


if __name__ == '__main__':
    from searching_key import searching_key

    root: Node = Node()
    keys: tuple = (8, 3, 10, 1, 6, 14, 4, 7, 13)

    for key in keys:
        root.insert(key)

    root = root.remove(3)
    assert not searching_key(root, 3)
