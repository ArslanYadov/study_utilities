from binary_tree_model import Node


def bts_or_not(root: Node) -> bool:
    """
    Функция проверяет, является ли двоичное дерево
    - бинарным деревом поиска (BST - binary search tree).
    BST - бинарное дерево, у которого значение левого поддерева
    строго меньше значения узла, а в правой - строго больше.
    ---
    Аргументы:
        корень двоичного дерева
    Возвращаемое значение:
        True or False
    ---
    Сложность: O(N), т.к. если дерево bst, то прийдется пройтись
    по всем вершинам.
    ---
    Пример:
        5
       / \
      3   8
     / \   \
    1   4   9
    """
    def check(node: Node, min_val: int | float, max_val: int | float) -> bool:
        if not node:
            return True
        if node.value <= min_val or node.value >= max_val:
            return False
        return (
            check(node.left, min_val, node.value)
            and check(node.right, node.value, max_val)
        )
    return check(root, float('-inf'), float('inf'))


if __name__ == '__main__':

    node5 = Node(9)
    node4 = Node(4)
    node3 = Node(1)
    node2 = Node(8, None, node5)
    node1 = Node(3, node3, node4)
    node0 = Node(5, node1, node2)

    assert bts_or_not(node0)
    node4.value = 6
    assert not bts_or_not(node0)
