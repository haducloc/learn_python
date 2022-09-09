# Import my random_util.py in the root folder
import random_util

# To calculate sum of all numbers in an array, then return the sum
def calculate_sum(arr):

    # Initial sum is ZERO
    sum = 0

     # for each number, add the number to the sum
    for num in arr:
        sum += num

    # return sum, exit the funtion
    return sum

##### CALL function ##########

amounts = random_util.random_list(5, 1, 10)
sum_amounts = calculate_sum(amounts)

print(f"Amounts={amounts}")
print(f"Total amounts={sum_amounts}")


########### Python Built-in function ##########