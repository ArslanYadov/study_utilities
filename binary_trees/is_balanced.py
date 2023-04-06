from binary_tree_model import Node


def is_balanced(root: Node) -> bool:
    """
    Проверка сбалансированно ли бинарное дерево.
    Сбалансированным считает дерево,
    у которого глубина правого и левого поддерева,
    для каждой вершины, не более единицы.
    ---
    Сложность: O(N), т.к. приходится пройтись по всем
    узлам дерева.
    """
    flag: bool = True

    def depth(root: Node) -> int:
        """Подсчитывает глубину бинарного дерева."""
        nonlocal flag
        if not root:
            return 0

        left: int = depth(root.left)
        right: int = depth(root.right)

        if abs(left - right) > 1:
            flag = False

        return max(left, right) + 1

    depth(root)
    return flag


if __name__ == '__main__':
    from sarr_to_btree import array2balanced_btree

    keys: tuple = (1, 2, 2, 3, 3, 4, 4)
    root: Node = Node()

    for key in keys:
        root.insert(key)

    assert not is_balanced(root)

    new_root: Node = array2balanced_btree(keys)

    assert is_balanced(new_root)
