#Check if the first and last numbers of a list are the same

def check_first_last(numbers):
    if len(numbers) == 0:
        return False
    return numbers[0] == numbers[-1]

# numbers = [1, 2, 3, 1]
# output = True

# numbers = [1, 2, 3, 4]
# output = False