def sum_numbers(numbers=None):
    total = 0
    if numbers == None:
        return sum(range(1,101))
    for num in numbers:
        total += num
    return total