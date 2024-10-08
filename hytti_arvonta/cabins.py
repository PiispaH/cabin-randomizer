from random import shuffle

def cabins(n: int, names: list):
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
