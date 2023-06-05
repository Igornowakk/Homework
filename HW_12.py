from typing import Union

def difference(*args: Union[int, float]) -> Union[int, float]:
    """
    Difference between the largest (maximum) and smallest (minimum) element.
    :param args: input digits to calculate difference
    :return: difference of the largest and smallest digit
    """
    if len(args) == 0:
        return 0

    min_val = min(args)
    max_val = max(args)

    for element in args:
        if element < min_val:
            min_val = element
        if element > max_val:
            max_val = element

    return max_val - min_val

print(difference(1, 2, 6, 4, -6))