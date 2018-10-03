# 1.1 Solution by Daniel Ong
# Contact: danielong1@gmail.com

def unique_characters(s):
    """Returns true if a string has all unique characters."""
    return len(s) == len(set(s))


def unique_characters_ds(s):
    """Returns true if a string has all unique characters without using additional data structures."""
    for char in s:
        if s.count(char) > 1:
            return False
    return True


if __name__ == '__main__':
    test_cases = ('foo', 'bar', 'longer', 'example', 'python')
    for word in test_cases:
        print(word, unique_characters_ds(word))
