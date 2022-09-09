# Import 'sys' module provided by Python
import sys

# Import my random_util.py in the root folder
import random_util

# Find min of all numbers in an array, then return the min's index
# If the min duplicated, return the last index

def find_min_index(arr):

    # Always start with the largest number to find min
    min = sys.float_info.max
    min_index = -1  # we don't know index yet so initial should be invalid index

    # for each number, compare it with the current min
    # and see if the num > the current min -> record new min

    for idx, num in enumerate(arr):
        #if (num < min): min = num
        if (num < min):  # Found a new min candidate -> Record the new min and its index
            min = num
            min_index = idx
            
            # Question:  What if I want to return the first index of the min (if duplicated)?

    # return min and min_index, exit function
    return (min, min_index)

##### CALL function ##########

amounts = random_util.random_list(5, 1, 10)

(min, min_index) = find_min_index(amounts)

print(f"Amounts={amounts}")
print(f"Min amount={min}")
print(f"Min index={min_index}")


########### Python Built-in function ##########