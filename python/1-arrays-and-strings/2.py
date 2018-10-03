# 1.2 Solution by Daniel Ong
# Contact: danielong1@gmail.com

def is_permutation(a, b):
    """Returns true if strings a and b are permutations of each other and false otherwise."""
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    print('foo', 'bar', is_permutation('foo', 'bar'))
    print('dog', 'god ', is_permutation('dog', 'god '))
    print('dog', 'god', is_permutation('dog', 'god'))
