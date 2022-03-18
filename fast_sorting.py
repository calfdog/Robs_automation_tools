""" This is an example of a simple fast sort alogrithm - By Rob Marchetti
    I put in comments for those just learning. I would suggest to use the debug
    walk through the code to get idea how it works
"""


def fast_sort(sequence):
    """Takes a sequence of numbers and sorts them.
    """

    length = len(sequence)

    # if we only have 1 item then just return list, since thre is no need to sort any further
    if length <= 1:
        return sequence
    else:
        # Pop off the last item on the list and this becomes the pivot
        pivot = sequence.pop()

    # Put items bigger than the pivot here
    items_larger = []
    # Put items smaller than the pivot here
    items_smaller = []

    # Lets loop thru the sequence and test it the item is bigger or smaller than the pivot
    for item in sequence:
        """ if true that the item in the list bigger the the pivot append it to items.larger
            if true that the item in the list smaller the the pivot append it to items.smaller
        """
        if item > pivot:
            items_larger.append(item)
        else:
            items_smaller.append(item)

    return fast_sort(items_smaller) + [pivot] + fast_sort(items_larger)


# Print out the sorted list
print(fast_sort([88,400,76,6,9,1,3,5,4,13,34,11,123.03]))