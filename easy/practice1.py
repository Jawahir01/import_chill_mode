#Write a function that counts the number of vowels in a given string.

def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count



# input_string = "Hello World" 
# output = 3
# input_string = "Python Programming" 
# output = 4