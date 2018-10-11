def swapper(a: int, b: int) -> tuple:
    """Swap a and b in place without using any temporary variables

    Integers in python are immutable so this doesn't really make sense. We can't
    modify a, b outside of this function's scope and each operation creates a
    new int. It would be much more pythonic to write:
    b, a = a, b

    Args:
        a: an integer
        b: another integer

    Returns:
        (a, b) but they're swapped
    """
    a ^= b
    b ^= a
    a ^= b
    return a, b
