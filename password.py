import random 
import string 

# generates pw, the nums and chars parameters are optional but True by default 
def generate_password(min_length, nums=True, special_chars=True):
    # vars for all possible nums, special chars, and letters 
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    # will contain everything in one string so we can randomly select from 
    chars = letters 
    # if statements will append string of digits/specials if asked for 
    if nums:
        chars += digits
    if special_chars:
        chars += special   

    output = '' # will store the generated pw 
    meets_criteria = False # set to true once pw meets criteria 
    has_num = False 
    has_special = False 
    while not meets_criteria or len(output) < min_length:
        new_char = random.choice(chars)   
        output += new_char

        if new_char in digits:
            has_num = True 
        elif new_char in special:
            has_special = True 

        meets_criteria = True 
        if nums:
            meets_criteria = has_num
        if special_chars:
            meets_criteria = meets_criteria and has_special
    return output




min_length = int(input('Hello, please provide a minimum length for your password: '))
nums = input('would you like to include any numbers (y/n)? ')
special = input('would you like to include any special characters (y/n)? ')
if nums != 'y': 
    nums = False 
if special != 'y':
    special = False
pwd = generate_password(min_length, nums, special)



print(pwd)