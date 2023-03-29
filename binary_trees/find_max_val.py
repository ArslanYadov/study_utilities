class Node:
    """Класс узла для бинарного дерева."""

    def __init__(self, value=0, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


def find_max_val(root: Node) -> int:
    """
    Функция обходит бинарное дерево и находит вершину,
    которая имеет самый большой вес.
    Аргументы:
        root - корень дерева
    Возвращаемое значение:
        самое большое значение из всех вершин дерева.
    """
    if not root:
        return 0
    max_val: int = root.value
    lval: int = find_max_val(root.left)
    rval: int = find_max_val(root.right)
    return max(max_val, lval, rval)


if __name__ == '__main__':
    node11 = Node(1)
    node10 = Node(0)
    node9 = Node(3)
    node8 = Node(15)
    node7 = Node(14)
    node6 = Node(6, node10, node11)
    node5 = Node(2)
    node4 = Node(10, None, node9)
    node3 = Node(8, node7, node8)
    node2 = Node(5, node5, node6)
    node1 = Node(3, node3, node4)
    root = Node(1, node1, node2)

    assert find_max_val(root) == 15
