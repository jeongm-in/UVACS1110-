# Version: Jeong Min Lim (sogogibeef)
# quadratic.py contains big_root function that takes three input
# and returns the more positive root of the quadratic equation.

# a*x**2 + b*x + c

def big_root(a, b, c):
    bigger_root = (-b + (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)
    return bigger_root


def small_root(a, b, c):
    smaller_root = (-b - (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)
    return smaller_root
