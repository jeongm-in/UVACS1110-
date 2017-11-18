# Version : Jeong Min Lim (sogogibeef)
# averages contains four functions mean, median, rms, and middle_average.
# mean(a,b,c) takes three arguments and returns the arithmetic mean
# median(a,b,c) takes three arguments and returns the median
# rms(a,b,c) takes three arguments and returns root-mean-square
# middle_average(a,b,c) takes three arguments and computes mean, median and rms of a, b, c
# and returns median of three averages.


def mean(a, b, c):
    return (a + b + c) / 3


def median(a, b, c):
    values = [a, b, c]
    sorted_values = sorted(values)  # Hehe, used sorted(). Will fix later not using sorted() WIP
    middle_index = int(len(sorted_values) / 2)
    return (sorted_values[middle_index])


def rms(a, b, c):
    rms_value = mean(a ** 2, b ** 2, c ** 2) ** 0.5
    return rms_value


def middle_average(a, b, c):
    mean_result = mean(a, b, c)
    median_result = median(a, b, c)
    rms_result = rms(a, b, c)
    middle_average_result = median(mean_result, median_result, rms_result)
    return middle_average_result


print(mean(1, 5, 1))
print(median(1, 5, 1))
print(rms(1, 5, 1))
print(middle_average(1, 5, 1))

# Should work on "general" version
