def unique_characters(input_str: str) -> bool:
    """Returns true if a string has all unique characters using a dict.

    Args:
        input_str: Input string

    Returns:
        Returns True if a string has all unique characters.
    """
    seen_chars = {}
    for char in input_str:
        if char in seen_chars:
            return False
        seen_chars[char] = True
    return True


def unique_characters_ds(input_str: str) -> bool:
    """Returns true if a string has all unique characters without using a dict.

    Args:
        input_str: Input string

    Returns:
        Returns True if a string has all unique characters.
    """
    for char in input_str:
        if input_str.count(char) > 1:
            return False
    return True


if __name__ == '__main__':
    test_cases = ('foo', 'bar', 'longer', 'example', 'python')
    for word in test_cases:
        print(word, unique_characters_ds(word))
