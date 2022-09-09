# No Name       2013 - ?
# Gen Z	        1997 – 2012
# Millennials	1981 – 1996
# Gen X	        1965 – 1980
# Boomers II*	1955 – 1964
# Boomers I*	1946 – 1954
# No Name	    ?  - 1945

# Write a function to return generation name of the given year of birth

def print_generation_name(year_of_birth):

    if year_of_birth <= 1945:
        print("No Name")
        return  # WHY I have to put 'return' here?

    if year_of_birth <= 1954:
        print("Boomers I")
        return  # WHY I have to put 'return' here?

    if year_of_birth <= 1964:
        print("Boomers II")
        return  # WHY I have to put 'return' here?

    if year_of_birth <= 1980:
        print("Gen X")
        return  # WHY I have to put 'return' here?

    if year_of_birth <= 1996:
        print("Millennials")
        return  # WHY I have to put 'return' here?

    if year_of_birth <= 2012:
        print("Gen Z")
        # WHY I don't need to put 'return' here?

##### CALL function ##########

loc_yob = 1980
print_generation_name(loc_yob)

##### CALL function ##########

luke_yob = 2017
print_generation_name(luke_yob)
