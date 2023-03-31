from binary_tree_model import Node


def searching_key(root: Node, key: int) -> bool:
    """Поиск ключа в бинарном дереве поиска."""
    if not root:
        return False
    if key == root.value:
        return True
    return (
        searching_key(root.left, key) if key < root.value
        else searching_key(root.right, key)
    )


if __name__ == '__main__':

    root: Node = Node()
    data: tuple = (5, 3, 1, 4, 8, 6)
    for val in data:
        root.insert(val)

    assert searching_key(root, 4)
    assert not searching_key(root, 2)
