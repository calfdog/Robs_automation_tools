"""
Simple random name generator
by Rob Marchetti 3/7/2022
"""

import random


def get_name():
    file = 'last_names.txt'
    names_file = open(file, "r")
    lnames = names_file.read()
    last_names = [lname for lname in lnames.split('\n')]

    file = 'first_names.txt'
    names_file = open(file, "r")
    fnames = names_file.read()
    first_names = [fname for fname in fnames.split('\n')]

    # random first and last names
    random_fname = random.choice(first_names)
    random_lname = random.choice(last_names)

    # Declare a variable as a random choice
    return f"{random_fname} {random_lname}"


