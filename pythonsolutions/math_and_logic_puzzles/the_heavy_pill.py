"""Solution:

Given bottles 1, 2, ..., n. Place i pills on the scale from bottle #i. for i in
1, 2, ..., n. Use the surplus weight (see function below) to determine which
bottle has the heavy pills.
"""


def bottle_id(total_weight: float, bottles: int = 20, normal_pill: float = 1.0,
              heavy_pill: float = 1.1) -> int:
    """Return the bottle ID that has the heavy pills given the total weight

    Args:
        total_weight: weight of 1 pill from bottle 1, 2 pills from bottle 2, ...
        bottles: number of bottles
        normal_pill: weight of a normal pill
        heavy_pill: weight of a heavy pill

    Returns:
        Bottle ID
    """
    expected_weight = normal_pill * ((bottles * (bottles + 1)) / 2)
    surplus_weight = total_weight - expected_weight
    return round(surplus_weight / (heavy_pill - normal_pill))
