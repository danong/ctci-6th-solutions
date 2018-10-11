def merge(a: list, b: list) -> list:
    """Merges B into A in sorted order

    a is modified in place and also returned

    Args:
        a: sorted list with enough buffer at the end to hold b
        b: sorted list

    Returns:
        A single sorted list
    """
    end_b = len(b) - 1
    for idx, val in enumerate(a):
        if val is None:
            break
    end_a = idx - 1

    last = end_b + end_a + 1

    while end_b >= 0 and end_a >= 0:
        if a[end_a] > b[end_b]:
            a[last] = a[end_a]
            a[end_a] = None
            end_a -= 1
        else:
            a[last] = b[end_b]
            b[end_b] = None
            end_b -= 1
        last -= 1
    return a
