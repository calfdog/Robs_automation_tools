"""
    Developed by: Rob Marchetti 11/17/2014
    This Python module takes a string an makes a tuple / list that is quotes
    this is similar to Perl's qw function
    Example:
    s = 'Python Json Ruby Perl'
    will return a tuple('Python,', 'Json,', 'Ruby,', 'Perl')
    or a list ['Python', 'Json', 'Ruby', 'Perl']
    Updated for Python 3
"""

s = "Python Json Ruby Perl"

def quote_string_to_tuple(s):
    """
        Makes a tuple then quotes it like in Perl
    """
    #return tuple(s.split())
    return tuple(s.split())

def quote_string_to_list(s):
    """
        Makes a List then Qoutes it like in Perl
    """
    #return tuple(s.split())
    return list(s.split())




# examples
print(quote_string_to_tuple(s))
print(quote_string_to_list(s))
