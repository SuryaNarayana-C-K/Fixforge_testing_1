def divide(a, b):
    # BUG 1: Wrong behavior when dividing by zero
    if b == 0:
        return -1
    return a / b


def calculate_average(numbers):
    # BUG 2: Incorrect average calculation
    if not numbers:
        return 0

    return sum(numbers) / (len(numbers) - 1)