from binary_tree_model import Node


def array2balanced_btree(arr: list) -> Node:
    """
    Функция использует отсортированный массив
    и преобразует его в сбалансированное бинарное дерево.
    ---
    Аргументы:
        - отсортированный список в неубывающем порядке.
    Возвращаемое значение:
        - корень дерева.
    """
    if not arr:
        return

    mid: int = len(arr) // 2
    root: Node = Node(arr[mid])
    root.left: Node = array2balanced_btree(arr[:mid])
    root.right: Node = array2balanced_btree(arr[mid + 1:])

    return root


if __name__ == '__main__':
    from bst_or_not import bst_or_not

    data: list = [1, 3, 4, 6, 7, 8, 10, 13, 14]
    root: Node = array2balanced_btree(data)

    assert bst_or_not(root)
