##### Define all my re-use functions #####
##### All re-use .py files should be in the root folder #####

# Import Python random module
import random

# define a function to generate a random list with len, min, max.
# the max = 20 if not passed
# the min = 1 if not passed

def random_list(len, min = 1, max = 20):
    return random.sample(range(min, max), len)
    
