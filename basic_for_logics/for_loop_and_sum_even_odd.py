# Import my random_util.py in the root folder
import random_util

# Return sum of even numbers and sum of odd numbers in the given array
def find_sum_even_odd(arr):

    # Initial sum is ZERO
    even_sum = 0
    odd_sum = 0

     # for each number
    for num in arr:
        if num % 2 == 0:  # If the number is EVEN -> Add it into even_sum
            even_sum += num
        else:             # If the number is ODD -> Add it into odd_sum
            odd_sum += num

    # return 2 sum:  even_sum and odd_sum:  Tuple type
    return (even_sum, odd_sum)

##### CALL function ##########

numbers = random_util.random_list(5, 1, 10)
even_odd_sum = find_sum_even_odd(numbers)

print(f"Numbers={numbers}")
print(f"Sum of even numbers={even_odd_sum[0]}") # even_sum at index 0 of the Tuple result
print(f"Sum of odd numbers={even_odd_sum[1]}")  # even_sum at index 1 of the Tuple result


# Call function find_sum_even_odd again (different way)

# Declare 2 variable named even_sum, odd_sum
# even_sum = first number in the result --- index 0
# odd_sum = second number in the result --- index 1

(even_sum, odd_sum)  = find_sum_even_odd(numbers)

print(f"Sum of even numbers={even_sum}")
print(f"Sum of odd numbers={odd_sum}")


########### Python Built-in function ##########
