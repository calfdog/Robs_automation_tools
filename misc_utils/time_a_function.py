"""
    Description: Can be used for timing test and such. timing_function takes a decorated function as an
    arg and returns the time it took for the function to complete.
    Developer: Rob Marchetti
"""

import time


def timing_function(some_function):
    """
    Outputs the time a function takes
    to execute.
    """

    def wrapper():
        t1 = time.time()
        some_function()
        t2 = time.time()
        return "Time it took to run the function: " + str((t2-t1)) + "\n"
    return wrapper


@timing_function
def my_function():
    num_list = []
    for x in (range(1, 99999)):
        num_list.append(x)
    print("\nSum of all the numbers: " +str((sum(num_list))))


# prints the time it took to sum all the numbers
print(my_function())
