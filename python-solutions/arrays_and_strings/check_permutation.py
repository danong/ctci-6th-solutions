def is_permutation(a: str, b: str) -> bool:
    """Check if a is a permutation of b

    Args:
        a: a string
        b: another string

    Returns:
        True if a is a permutation of b, False otherwise
    """
    counter = {}
    for char in a:
        counter[char] = counter.get(char, 0) + 1
    for char in b:
        counter[char] = counter.get(char, 0) - 1
    return all(value == 0 for value in counter.values())
