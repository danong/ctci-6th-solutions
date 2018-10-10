from functools import lru_cache


def recursive(num_steps: int) -> int:
    """Compute possible number of ways of climbing n steps if we can take 1, 2,
    or 3 steps at a time.

    Args:
        num_steps: number of total steps

    Returns:
        The number of possible ways to climb the stairs
    """
    if num_steps <= 2:
        return num_steps
    if num_steps == 3:
        return 4
    return recursive(num_steps - 1) + recursive(num_steps - 2) + recursive(
        num_steps - 3)


def bottom_up(num_steps: int) -> int:
    """Compute number of steps using a bottom up approach

    This iterative appraoch is the best approach. Since it avoids the max
    recursion depth and uses O(1) space. Actually, the space complexity is more
    complicated. We only use 3 ints but the space needed by those 3 ints grows
    as n grows. I guess it actually uses O(log(n)) space?

    Args:
        num_steps: number of total steps

    Returns:
        The number of possible ways to climb the stairs
    """
    if num_steps <= 2:
        return num_steps
    if num_steps == 3:
        return 4
    a = 1
    b = 2
    c = 4
    for _ in range(4, num_steps):
        a, b, c = b, c, a + b + c
    return a + b + c


def top_down(num_steps: int, cache: dict = {1: 1, 2: 2, 3: 4}) -> int:
    """Same as `recursive()` but using a dict as a cache

    cache will have num_steps elements

    Args:
        num_steps: number of total steps
        cache:

    Returns:
        The number of possible ways to climb the stairs
    """
    if num_steps in cache:
        return cache[num_steps]
    res = top_down(num_steps - 3) + top_down(num_steps - 2) + top_down(
        num_steps - 1)
    cache[num_steps] = res
    return res


@lru_cache(maxsize=3)
def pythonic(num_steps: int) -> int:
    """Same as `recursive()` but using built in cache.

    We can safely use a cache of size 3 to save some space.

    Args:
        num_steps:

    Returns:
        The number of possible ways to climb the stairs
    """
    if num_steps <= 2:
        return num_steps
    if num_steps == 3:
        return 4
    return pythonic(num_steps - 3) + pythonic(num_steps - 2) + pythonic(
        num_steps - 1)
