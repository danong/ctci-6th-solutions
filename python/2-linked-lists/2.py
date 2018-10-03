from typing import Optional

from .linked_list import Node


def kth_to_last(k: int, head: Node) -> Optional(Node):
    """Returns the kth to last element of a singly linked list

    Args:
        k: Number of spaces from the end of the list
        head: Start of linked list

    Returns:
        The k-th node from the end of the list if valid

    """
    ahead = behind = head

    for _ in range(k):  # move ahead k spots forward
        if ahead is None:
            return None
        else:
            ahead = ahead.next

    while ahead is not None:  # move ahead and behind forward together
        ahead = ahead.next
        behind = behind.next
    return behind
