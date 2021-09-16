import sys


def compute_cube(x: int, y: int) -> list:
    """
    Return list of the cube integers.
    """
    try:
        return [number**3 for number in range(x, y + 1)]
    except TypeError as err:
        print(err)
        print("x =", x)
        print("y =", y)
        sys.exit(1)


print(compute_cube(2, 3))
print(compute_cube(1, 4))
print(compute_cube([], 4))
