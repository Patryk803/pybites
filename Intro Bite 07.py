def filter_positive_even_numbers(numbers):
    """Receives a list of numbers, and returns a filtered list of only the
       numbers that are both positive and even (divisible by 2), try to use a
       list comprehension."""
    return [ num for num in numbers if num> 0 and num%2 == 0 ]

number = [0,2,3,1,5,78,9]

# for num in number:
#     if num > 0 and num%2 == 0:
#         print("Brawo, liczba jest parzysta i dodatnia")
#     else:
#         print("nieparzysta albo niedodatnia")

