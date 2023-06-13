class Node:
    """
    Simple model for node with key,
    pointer on previous and next node.
    """

    def __init__(self, key=0, prev=None, next=None) -> None:
        self.key = key
        self.prev = prev
        self.next = next
