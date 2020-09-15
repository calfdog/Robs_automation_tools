"""
Description:
This is a simple example of using pandas in web-scraping
two separate tables on a wikipedia page using the following links
to get the names of the deities from the tables:
https://en.wikipedia.org/wiki/List_of_Germanic_deities#Gods
https://en.wikipedia.org/wiki/List_of_Germanic_deities#Goddesses

By Rob Marchetti
"""

import pandas as pd


def get_names_of_gods(df):
    """Get the names from the "Name" column in the first deity table.
        param: df - dataframe for god table.

    This will get the names as an array - ['Alcis (Latinized Germanic)', 'Baldr (Old Norse)', ...']
    Uses split on space to break the name into list  and then [0]
    to get first list item - ['Baldr',  (Old Norse)']
    else it would print 'Baldr (Old Norse)' instead.

    If you were verifying each name in rows under the "Name" column you may want to get the whole string
    example: 'Baldr (Old Norse)'
    """
    # First table - df[o]
    names = df[0]["Name"].values
    for name in names:
        print(f"God:{name.split(' ')[0]}")


def get_names_of_goddesses(df):
    """Get the names from the "Name" column in the second deity table.
        param: df - dataframe for goddesses table.
        (See above method as well)
    """
    # Second table - df[1]
    names = df[1]["Name"].values
    for name in names:
        print(f"Goddess:{name.split(' ')[0]}")


"""
Note:
If you were using Selenium, you would get the source this way:
# Get the source
browser.get("https://en.wikipedia.org/wiki/List_of_Germanic_deities#Gods")
html = browser.page_source
# read the html in as a dataframe
data_frame1 = pd.read_html(html)
"""

# read in the html source as a dataframe to get access to the table's rows and columns
# first table
data_frame1 = pd.read_html('https://en.wikipedia.org/wiki/List_of_Germanic_deities#Gods')
# second table
data_frame2 = pd.read_html('https://en.wikipedia.org/wiki/List_of_Germanic_deities#Goddesses')

# Call the appropriate methods: each method takes dataframe as an argument
get_names_of_gods(data_frame1)
get_names_of_goddesses(data_frame2)


