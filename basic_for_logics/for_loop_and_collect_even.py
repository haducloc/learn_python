# Import my random_util.py in the root folder
import random_util

# Collect all even numbers in the given list, then returnt the list of all collected even numbers.
def collect_even_numbers(arr):

    # Initial sum is ZERO
    evens = []

     # for each number
    for num in arr:
        if num % 2 == 0:  # If the number is EVEN -> Add it into the evens list
            evens.append(num)

    # return evens, exit the funtion
    return evens

##### CALL function ##########

numbers = random_util.random_list(5, 1, 10)
evens = collect_even_numbers(numbers)

print(f"Numbers={numbers}")
print(f"List of even numbers={evens}")


########### Python Built-in function ##########