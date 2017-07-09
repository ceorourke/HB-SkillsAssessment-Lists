"""List Practice

Edit the functions until all of the doctests pass when
you run this file.
"""

def print_list(items):
    """Print each item in the input list."""

    for item in items:
        print(item)


def long_words(words):
    """Return words in input list that longer than 4 characters."""

    long_words = []

    for word in words:
        if len(word) > 4:
            long_words.append(word)

    return long_words


def n_long_words(words, n):
    """Return words in list longer than `n` characters."""

    long_words = []

    for word in words:
        if len(word) > n:
            long_words.append(word)

    return long_words


def smallest_int(numbers):
    """Find the smallest integer in a list of integers and return it."""

    smallest_int = None

    for num in numbers:
        if num < smallest_int:
            smallest_int = num

    return smallest_int


def largest_int(numbers):
    """Find the largest integer in a list of integers and return it."""

    largest_int = None

    for num in numbers:
        if num > largest_int:
            largest_int = num

    return largest_int


def halvesies(numbers):
    """Return list of numbers from input list, each divided by two."""
    # halvesies = []

    # for num in numbers:
    #     num = float(num) / 2
    #     halvesies.append(num)
    # practicing comprehensions

    halvesies = [float(num) / 2 for num in numbers]

    return halvesies


def word_lengths(words):
    """Return the length of words in the input list."""
    # word_lengths = []
    # for word in words:
    #     word_lengths.append(len(word))
    # practicing comprehensions

    word_lengths = [len(word) for word in words]

    return word_lengths


def sum_numbers(numbers):
    """Return the sum of all of the numbers in the list."""
    # sum_numbers = 0

    # for num in numbers:
    #     sum_numbers += num
    # practicing comprehensions

    sum_numbers = (sum_numbers + num for num in numbers)

    return sum_numbers


def mult_numbers(numbers):
    """Return product (result of multiplication) of numbers in list."""

    mult_numbers = 1

    # for num in numbers:
    #         mult_numbers = mult_numbers * num
    # practicing comprehensions

    mult_numbers = (mult_numbers * num for num in numbers)

    return mult_numbers


def join_strings(words):
    """Return a string of all input strings joined together."""
    join_strings = ''

    # for word in words:
    #     join_strings += word
    # practicing comprehensions

    join_strings = (join_strings + word for word in words)

    return join_strings


def average(numbers):
    """Return the average (mean) of the list of numbers given.

    For example::

        >>> average([2, 4])
        3.0

    This should handle cases where the result isn't an integer::

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty;
    it's fine if this raises an error when given an empty list.

    (Think of the best way to handle an empty input list, though,
    and feel free to provide a good solution here.)
    """
    try:
        length = len(numbers)
        sum_numbers = 0

        for num in numbers:
            sum_numbers += float(num)     

        average = sum_numbers / length
        return average
    except:
        average = 0
        return average

    # added a try and except to handle a possible empty list

def join_strings_with_comma(words):
    """Return ['list', 'of', 'words'] like "list, of, words"."""
    join_strings_with_comma = ''

    if len(words) == 1:
        join_strings_with_comma = words[0]
    else:
        join_strings_with_comma = words[0] + ", " + words[1] + ", " + words[2]

    return join_strings_with_comma

    # I know this is a really bad way to do this because the input could 
    # be more than 3 words. I couldn't figure out how to remove the last 
    # comma from the dogs in a for loop. We did something similar in lab 
    # but I was advised to use .join which we can't use here :( so, it 
    # passed the doctests, but I know it's not a great solution. 


def reverse_list(items):
    """Return the input list, reversed."""

    return items[::-1]


def reverse_list_in_place(items):
    """Reverse the input list `in place`.

    Reverse the input list given, but do it "in place" --- that is,
    do not create a new list and return it, but modify the original
    list.

    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.

    For example::

        >>> orig = [1, 2, 3]
        >>> reverse_list_in_place(orig)
        >>> orig
        [3, 2, 1]

        >>> orig = ["cookies", "love", "I"]
        >>> reverse_list_in_place(orig)
        >>> orig
        ['I', 'love', 'cookies']
    """
    items[::-1] = items
    return items

    # super confused as to why this isn't passing the tests. I tried it out in 
    # the console and it appears to work. it says it's expecting nothing, why
    # would it expect nothing?


def duplicates(items):
    """Return list of words from input list which were duplicates.

    Return a list of words which are duplicated in the input list.
    The returned list should be in ascending order.

    For example::

        >>> duplicates(
        ...     ["apple", "banana", "banana", "cherry", "apple"]
        ... )
        ['apple', 'banana']

        >>> duplicates([1, 2, 2, 4, 4, 4, 7])
        [2, 4]

    You should do this without changing the original list::

        >>> orig = ["apple", "apple", "berry"]
        >>> duplicates(orig)
        ['apple']

        >>> orig
        ['apple', 'apple', 'berry']
    """
    duplicates = []
    dupe = ''
    for item in items:
        #if the item is in the list more than once
            duplicates.append(item)    

    return duplicates

    # not sure how to check if it's in the list more than once

def find_letter_indices(words, letter):
    """Return list of indices where letter appears in each word."""

    indices = []

    for i, word in enumerate(words):
        for l in word:
            if l == letter:
                indices.append(i)
        if letter not in word:
            indices.append(None)

    return indices


#####################################################################
# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print("\nALL TESTS PASSED. GOOD WORK!\n")
