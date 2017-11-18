def mean(a, b, c):
    """computes the mean of real numbers a, b, and c."""
    return (a + b + c) / 3


def median(a, b, c):
    """computes the median of real numbers a, b, and c."""
    if a >= b >= c or c >= b >= a:
        return b
    elif a >= c >= b or b >= c >= a:
        return c
    else:
        return a


def rms(a, b, c):
    """computes the root-mean-square of real numbers a, b, and c.
    invokes the function 'mean' once"""
    return mean(a ** 2, b ** 2, c ** 2) ** (1 / 2)


def middle_average(a, b, c):
    """computes the mean, median, and rms of a, b, c and returns the median
    of those three averages.
    invokes the functions 'mean' and 'rms' once each and 'median' twice."""
    return median(mean(a, b, c), median(a, b, c), rms(a, b, c))
