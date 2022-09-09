# Import my random_util.py in the root folder
import random_util

# To calculate sum of all EVEN numbers in an array, then return the sum
def calculate_even_sum(arr):

    # Initial sum is ZERO
    sum = 0

     # for each number
    for num in arr:
        if num % 2 == 0:  # If the number is EVEN -> Add it to sum
            sum += num

    # return sum, exit the funtion
    return sum

##### CALL function ##########

numbers = random_util.random_list(5, 1, 10)
even_sum = calculate_even_sum(numbers)

print(f"Numbers={numbers}")
print(f"Sum of even numbers={even_sum}")


########### Python Built-in function ##########