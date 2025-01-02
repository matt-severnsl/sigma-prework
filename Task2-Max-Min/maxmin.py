# given an array of integers, return the smallest and largest in an array without min or max
print("Welcome to the min-max finder! Please enter your list of numbers separated by commas.")
numbers = input().split(',')


def min_max(numbers):
    min_and_max = []
    min = numbers[0]
    max = numbers[0]

    for num in numbers:
        if num < min:
            min = num
    for num in numbers:
        if num > max:
            max = num
    return [min, max]


print(min_max(numbers))
