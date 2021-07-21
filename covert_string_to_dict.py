"""
    Developed by: Rob Marchetti July 2021
    Lazy man's script that lets you take a string that you want as a dict and converts it to a dictionary
    Example:
        INPUT: s = "Lang1 Python Lang2 Ruby Lang3 Java Lang4 Perl"
        OUTPUT: {'Lang1': 'Python', 'Lang2': 'Ruby', 'Lang3': 'Java', 'Lang4': 'Perl'}

    Updated for Python 3
"""


def covert_string_to_dict(s):
    """Take a string, split it, quote it, convert to list convert to dict"""
    lst = list(s.split())
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct


# string to convert
s = "Lang1 Python Lang2 Ruby Lang3 Java Lang4 Perl"
dct = covert_string_to_dict(s)

print(dct) # {'Lang1': 'Python', 'Lang2': 'Ruby', 'Lang3': 'Java', 'Lang4': 'Perl'}
print(dct["Lang1"]) # Python

