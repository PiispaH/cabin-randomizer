#!/usr/bin/env python3

from random import shuffle
from typing import List

def cabins(n: int, names: list) -> List[List]:
    """
    Randomizes the given names into n groups of four each.

    Args:
        n (int): Amount of cabins.
    Returns:
        rooms (list): A list of the randomized four person cabins.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be an integer with value greater than 0.")
    if len(names) != 4 * n:
        raise ValueError("The amount of names must equal the number of cabins times 4.")
    if len(names) != len(set(names)):
        raise ValueError("All names must be unique.")
    
    shuffle(names)
    rooms = []
    for _ in range(n):
        rooms.append(names[:4])
        names = names[4:]
    return rooms
