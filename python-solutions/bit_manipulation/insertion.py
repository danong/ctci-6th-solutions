def insert_bits(n: int, m: int, i: int, j: int) -> int:
    mask = ~((1 << j + 1) - (1 << i))
    shifted_m = m << i
    return (n & mask) | shifted_m
