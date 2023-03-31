from binary_tree_model import Node


def in_range(data: list, root: Node, left: int, right: int) -> None:
    """
    Функция рекурсивно проходит по бинарному дереву поиска
    и выводит все значения вершин, которые соответствуют интервалу [i;j].
    Значения выводятся в неубывающем порядке.
    """
    if not root:
        return
    if root.value < left:
        in_range(data, root.right, left, root.value)
    if root.value >= left:
        in_range(data, root.left, left, right)
    if left <= root.value <= right:
        data.append(root.value)
    if root.value <= right:
        in_range(data, root.right, left, right)


if __name__ == '__main__':

    root: Node = Node()
    left: int = 448
    right: int = 763
    data: list = []

    keys: tuple = (
        668, 298, 702, 191, 701,
        870, 266, 822, 912, 932
    )
    for key in keys:
        root.insert(key)

    in_range(data, root, left, right)

    assert data == [668, 701, 702]
