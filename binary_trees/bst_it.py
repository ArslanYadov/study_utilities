from __future__ import annotations
from collections import deque


class TreeNode:
    """Модель узла дерева."""

    def __init__(self, value=None, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    """
    Простая модель бинарного дерева.
    Вместо рекурсий используется итеративный метод.
    """

    def __init__(self) -> None:
        self.root: TreeNode | None = None

    def insert(self, key) -> None:
        """Вставка нового узла в дерево."""
        if not self.root:
            self.root: TreeNode | None = TreeNode(key)
            return

        current_node: TreeNode = self.root
        prev_node: TreeNode | None = None
        while current_node:
            prev_node = current_node
            if key < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right

        if not prev_node:
            prev_node = TreeNode(key)
        elif key < prev_node.value:
            prev_node.left = TreeNode(key)
        else:
            prev_node.right = TreeNode(key)
        return

    def height(self) -> int:
        """Вычисление высоты дерева."""
        if not self.root:
            return 0

        node: TreeNode = self.root
        height_count: int = 0
        queue = deque([node])

        while queue:
            height_count += 1
            for _ in range(len(queue)):
                current_node = queue.popleft()
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

        return height_count


if __name__ == '__main__':

    root: BinarySearchTree = BinarySearchTree()
    keys: tuple = (8, 3, 10, 1, 6, 14, 4, 7, 13)

    for key in keys:
        root.insert(key)

    assert root.height() == 4
