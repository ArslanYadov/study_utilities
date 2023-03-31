from binary_tree_model import Node


def inorder(root: Node) -> None:
    """Обход дерева в центрированном порядке."""
    if not root:
        return
    inorder(root.left)
    print(root.value)
    inorder(root.right)


def preorder(root: Node) -> None:
    """Обход дерева в прямом порядке."""
    if not root:
        return
    print(root.value)
    preorder(root.left)
    preorder(root.right)


def postorder(root: Node) -> None:
    """Обход дерева в обратном порядке."""
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.value)


if __name__ == '__main__':

    root: Node = Node()
    values: tuple = (5, 8, 3, 4, 1)
    for val in values:
        root.insert(val)

    traversal_types: tuple = (
        (preorder, 'preorder'),
        (postorder, 'postorder'),
        (inorder, 'inorder'),
    )

    for trav, name in traversal_types:
        print(name, '-' * len(name), sep='\n')
        trav(root)
        print()
