class Node:
    """Basic node for a linked list.

    It stores its value in `val` and the next node in `next`.
    """

    def __init__(self, val):
        self.val = val
        self.next = None

    def append(self, val: object) -> None:
        """Append a new node to the end of the node list

        Args:
            val: Value of new node
        """
        end = Node(val)
        n = self
        while n.next is not None:
            n = n.next
        n.next = end
