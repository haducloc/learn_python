##### Define all my re-use functions #####
##### All re-use .py files should be in the root folder #####

from datetime import datetime
import re

def __parse_date(str):
    return datetime.strptime(str, f"%m/%d/%Y")

def __parse_bool(str):
    if str == "true" or str == "yes" or str == "y":
        return True
    if str == "false" or str == "no" or str == "n":
        return False
    raise "Could not convert the given str into True/False. Possible values: true|false|yes|no|y|n" 

def __input(var_name, type_converter=None, required=True, validator = None):
    failed = False
    while True:
        # input
        if failed:
            print(f"ERROR: Invalid {var_name}.")
        str = input(f">>> Enter {var_name}: ")
        str = str.strip()

        # optional?
        if not required:
            if str == "":
                return None

        # convert
        try:
            parsedVal = str if type_converter is None else type_converter(str)
        except:
            failed = True
            continue

        # validate
        if validator is None:
            return parsedVal
        valid = validator(parsedVal)

        if not valid:
            failed = True
        else:
            return parsedVal

def input_int(var_name, required=True, validator=None):
    return __input(var_name, int, required, validator)

def input_float(var_name, required=True, validator=None):
    return __input(var_name, float, required, validator)

def input_string(var_name, required=True, validator=None):
   return __input(var_name, None, required, validator)

def input_bool(var_name):
    return __input(var_name, __parse_bool, True, None)    

def input_date(var_name, required=True, validator=None):
   return __input(var_name, __parse_date, required, validator)   

def __input_list(var_name, type_converter=None, required=True, validator = None):
    failed = False
    while True:
        # input
        if failed:
            print(f"ERROR: Invalid {var_name}.")
            failed = False
        
        str = input(f">>> Enter {var_name}: ")
        str = str.strip()
        items = re.split("(?<!\\\\),", str)

        # optional?
        if not required:
            if len(items) == 0:
                return items

        # convert
        list = []
        for item in items:
            item = item.replace("\,", ",")
            try:
                item = item.strip()
                if item == "":
                    list.append(None)
                else:
                    parsedVal = item if type_converter is None else type_converter(item)
                    list.append(parsedVal)
            except:
                failed = True
                break

        if failed:
            continue

        # validate
        if validator is None:
            return list
        
        for parsedVal in list:
            valid = validator(parsedVal)

            if not valid:
                failed = True
                break

        if failed:
            continue

        return list

def input_ints(var_name, required=True, validator = None):
    return __input_list(var_name, int, required, validator)

def input_floats(var_name, required=True, validator = None):
    return __input_list(var_name, float, required, validator)

def input_strings(var_name, required=True, validator = None):
    return __input_list(var_name, None, required, validator)

def input_bools(var_name, required=True, validator = None):
    return __input_list(var_name, __parse_bool, required, validator)

def input_dates(var_name, required=True, validator = None):
    return __input_list(var_name, __parse_date, required, validator)    
