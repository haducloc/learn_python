# Check if a number exist? if yes, return true, else return false
def find_number(arr, number_to_find):

    # for each number in arr
    for num in arr:
        if (num == number_to_find):
            ## WHY return True here needed??
            return True

    # return false if not found
    ## WHY return False here needed??
    return False

# Check if a number exist? if yes, return true, else return false  -- Version 2
def find_number2(arr, number_to_find):

    # We don't know yet, so initial the result is False
    found = False

    # for each number in arr
    for num in arr:
        if (num == number_to_find):
            found = True
            break  ## WHY break here needed??

    return found

##### CALL function ##########

arr = [1,2,3,4,5,7,9,11]

print("Use Algorighm 1")
print(find_number(arr, 1)) # True
print(find_number(arr, 6)) # False

print("Use Algorighm 2")
print(find_number2(arr, 1)) # True
print(find_number2(arr, 6)) # False


########### Python Built-in function ##########