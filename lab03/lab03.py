# Question 1-4

def where_above(lst, limit):
    """
    where_above behaves like table.where(column, are.above(limit)).
    The analogy is completed if you think of a column of a table as a list and return the filtered column instead of the entire table.

    >>> where_above([1, 2, 3], 2)
    [3]
    >>> where_above(range(13), 10)
    [11, 12]
    >>> where_above(range(123), 120)
    [121, 122]

    """
    "*** YOUR CODE HERE ***"
    result = filter(lambda x: x > limit, lst)
    return list(result)
    


def minmax(s):
    """Return the minimum and maximum elements of a non-empty list. Hint: start 
    with defining two variables at the beginning. Do not use the built in 
    max or min functions

    >>> minmax([1, 2, -3])
    [-3, 2]
    >>> x = minmax([2])
    >>> x
    [2, 2]
    >>> minmax([4, 5, 4, 5, 1, 9, 0, 7])
    [0, 9]
    >>> minmax([100, -10, 1, 0, 10, -100])
    [-100, 100]
    """
    "*** YOUR CODE HERE ***"

    mini = s[0]

    i = 0
    while i < len(s):
        if s[i] < mini:
            mini = s[i]
        i += 1

    u = 0
    maxi = s[0]
    while u < len(s):
        if s[u] > maxi:
            maxi = s[u]
        u += 1


    return [mini, maxi]
    


def common_member(lst1, lst2):
    """
    Returns true if there are any common members between
    lst1 and lst2.
    >>> common_member([5, 3, 2, 1], [1, 9, 3, 4, 5])
    True
    >>> common_member([17, 18, 24], [23, 21, 22, 27, 29, 5])
    False
    >>> common_member([5, 7], [7, 3])
    True
    """
    "*** YOUR CODE HERE ***"

    i = 0
    while i < len(lst1):
        u = 0
        while u < len(lst2):
            if lst1[i] == lst2[u]:
                return True
            u += 1
        i += 1
        

    return False 


def closest_power_2(x):
    """ Returns the closest power of 2 that is less than x
    >>> closest_power_2(6)
    4
    >>> closest_power_2(32)
    16
    >>> closest_power_2(87)
    64
    >>> closest_power_2(4095)
    2048
    >>> closest_power_2(524290)
    524288
    """
    "*** YOUR CODE HERE ***"
    power = 0
    result = 0
    while result < x:
        result = 2**power
        power += 1

    return 2**(power - 2)

    


# Optional, Extra Credit.
def lab03_extra_credit():
  """
  Fill in the values for these two variables.
  You will get the special code from the study tool when you complete all quesitons from lab.
  This code will be unique to your okpy email and this lab.
  Go here to practice: https://codestyle.herokuapp.com/cs88-lab03
  """
  okpy_email = "shrutipai@berkeley.edu"
  practice_result_code = "df7222e14aff8a8bdeadfac2eb81c810"
  return (okpy_email, practice_result_code)
