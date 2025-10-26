'''

==================================================
=========== Python Password Geerator =============
==================================================

    a simple python code to generate passwords
    the password will contain at least a digit
    a special character and an uppercase letter
    the minimum length of the password is 3

    by Hocine (hocinebib)

==================================================
==================================================

'''

import argparse
import string
import random

STR_FCTS = {'1': string.ascii_lowercase, '2': string.digits, '3': string.punctuation, '4': string.ascii_uppercase}

def generate_password(length):
    '''
    the function to generate the secure password of specified length.
    
    Args:
        length (int): Length of the desired password. Must be >= 3.
    
    Returns:
        str: A randomly generated secure password.
    '''

    if length < 3:
        raise ValueError("Password length must be at least 3 to include all required character types.")

    password = random.choice(string.ascii_uppercase) + random.choice(string.digits) + random.choice(string.punctuation)

    for i in range(length - 3):
        fct = STR_FCTS[str(random.choices([1, 2, 3, 4], weights = [10, 2, 2, 2], k = 1)[0])]
        password += random.choice(fct)

    l = list(password)
    random.shuffle(l)

    return ''.join(l)


if __name__ == '__main__':

    PARSER = argparse.ArgumentParser()

    PARSER.add_argument("char_nbr", help="The number of characters that the password must contain (minimum 3).", type=int)

    ARGS = PARSER.parse_args()

    NB = ARGS.char_nbr

    try:
    	print(generate_password(NB))
    except ValueError as e:
    	print("Erreur : ", e)
