# Import 'sys' module provided by Python
import sys

# Import my random_util.py in the root folder
import random_util

# Find min of all numbers in an array, then return the min
def find_min(arr):

    # Always start with the largest number to find min
    min = sys.float_info.max

    # for each number, compare it with the current min
    # and see if the num > the current min -> record new min

    for num in arr:
        if (num < min): # found a new min candidate -> Record it
            min = num

    # return min, exit function
    return min

# Find max of all numbers in an array, then return the max
def find_max(arr):

    # Always start with the smallest number to find max
    max = sys.float_info.min

    # for each number, compare it with the current max
    # and see if the num < the current max -> record new max

    for num in arr:
        if (num > max): # found a new max candidate -> Record it
            max = num

    # return max, exit function
    return max

##### CALL function ##########

amounts = random_util.random_list(5, 1, 10)

min_amounts = find_min(amounts)
max_amounts = find_max(amounts)

print(f"Amounts={amounts}")
print(f"Min amount={min_amounts}")
print(f"Max amount={max_amounts}")


########### Python Built-in function ##########