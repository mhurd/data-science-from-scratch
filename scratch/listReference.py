from __future__ import division

# LISTS

# Probably the most fundamental data structure in Python is the list. A list is simply an ordered collection.
# (It is similar to what in other languages might be called an array, but with some added functionality.)

integer_list = [1, 2, 3]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [ integer_list, heterogeneous_list, [] ]
list_length = len(integer_list)     # equals 3
list_sum = sum(integer_list)     # equals 6

# You can get or set the nth element of a list with square brackets:x = range(10)   # is the list [0, 1, ..., 9]

x = [1, 2, 3]

zero = x[0]     # equals 0, lists are 0-indexed
one = x[1]      # equals 1
nine = x[-1]    # equals 9, 'Pythonic' for last element
eight = x[-2]   # equals 8, 'Pythonic' for next-to-last element
x[0] = -1       # now x is [-1, 1, 2, 3, ..., 9]

# You can also use square brackets to "slice" lists:

first_three = x[:3]                 # [-1, 1, 2]
three_to_end = x[3:]                # [3, 4, ..., 9]
one_to_four = x[1:5]                # [1, 2, 3, 4]
last_three = x[-3:]                 # [7, 8, 9]
without_first_and_last = x[1:-1]    # [1, 2, ..., 8]
copy_of_x = x[:]                    # [-1, 1, 2, ..., 9]

# Python has an in operator to check for list membership:

r1 = 1 in [1, 2, 3]    # True
r2 = 0 in [1, 2, 3]    # False

# This check involves examining the elements of the list one at a time, which means that you probably
# shouldn't use it unless you know your list is pretty small (or unless you don't care how long the check takes).
# It is easy to concatenate lists together:

x = [1, 2, 3]
x.extend([4, 5, 6])     # x is now [1,2,3,4,5,6]

# If you don't want to modify x you can use list addition:

x = [1, 2, 3]
y = x + [4, 5, 6]       # y is [1, 2, 3, 4, 5, 6]; x is unchanged

# More frequently we will append to lists one item at a time:

x = [1, 2, 3]
x.append(0)      # x is now [1, 2, 3, 0]
y = x[-1]        # equals 0
z = len(x)       # equals 4

# It is often convenient to unpack lists if you know how many elements they contain:

x, y = [1, 2]    # now x is 1, y is 2

# although you will get a ValueError if you don't have the same numbers of elements on both sides.
# It's common to use an underscore for a value you're going to throw away:

_, y = [1, 2]    # now y == 2, didn't care about the first element
