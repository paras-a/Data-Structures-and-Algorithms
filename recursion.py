from logging.config import valid_ident
from sys import flags


def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    @param n: A non-negative integer.
    @type n: int
    @return: The factorial of n.
    @rtype: int
    @raise ValueError: If n is negative.

    @example:
        >>> factorial(5)
        120
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0:
        return 1
    if n == 1:
        return n
    return n * factorial(n - 1)


def fibonacci(n):
    """
    Compute the nth Fibonacci number using recursion.

    @param n: The position in the Fibonacci sequence.
    @type n: int
    @return: The nth Fibonacci number.
    @rtype: int
    @raise ValueError: If n is negative.

    @example:
        >>> fibonacci(6)
        8
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def sum_digits(n):
    """
    Calculate the sum of the digits of a number using recursion.

    @param n: A non-negative integer.
    @type n: int
    @return: The sum of the digits.
    @rtype: int

    @example:
        >>> sum_digits(1234)
        10
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0:
        return n
    return n % 10 + sum_digits(n // 10)


def count_ways(n):
    """
    Count the number of distinct ways to climb n stairs, taking 1 or 2 steps at a time.

    @param n: The number of steps.
    @type n: int
    @return: Number of ways to reach the top.
    @rtype: int

    @example:
        >>> count_ways(4)
        5
        >>> count_ways(2)
        2
        >>> count_ways(3)
        3
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0 or n == 1:
        return 1
    return count_ways(n - 1) + count_ways(n - 2)


def reverse_string(s):
    """
    Reverse a string using recursion.

    @param s: The string to reverse.
    @type s: str
    @return: The reversed string.
    @rtype: str

    @example:
        >>> reverse_string("hello")
        'olleh'
    """
    mid = len(s) // 2
    if mid == 0:
        return s
    return reverse_string(s[mid + 1:]) + s[mid] + reverse_string(s[:mid])


def is_palindrome(s):
    """
    Check if a string is a palindrome using recursion.

    @param s: The string to check.
    @type s: str
    @return: True if the string is a palindrome, False otherwise.
    @rtype: bool

    @example:
        >>> is_palindrome("radar")
        True
        >>> is_palindrome("hello")
        False
    """
    if len(s) < 2:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])


def sum_array(arr):
    """
    Calculate the sum of all elements in a list using recursion.

    @param arr: A list of integers.
    @type arr: list[int]
    @return: The sum of the elements.
    @rtype: int

    @example:
        >>> sum_array([1, 2, 3, 4])
        10
    """
    if len(arr) == 0:
        return 0
    return arr[0] + sum_array(arr[1:])


def count_elements(lst):
    """
    Count the number of elements in a list using recursion.

    @param lst: A list of any elements
    @return: The number of elements in the list
    @rtype: int

    Examples:
        >>> count_elements([1, 2, 3])
        3
        >>> count_elements([])
        0
    """
    if len(lst) == 0:
        return 0
    return 1 + count_elements(lst[1:])


def power(base, exp):
    """
    Calculate base raised to the power of exp using recursion.

    @param base: The base number
    @param exp: The exponent (non-negative integer)
    @return: base raised to the power of exp
    @rtype: int or float

    Examples:
        >>> power(2, 3)
        8
        >>> power(5, 0)
        1
    """
    if exp < 0:
        raise ValueError("exponent must be a non-negative integer")
    if exp == 0:
        return 1
    return base * power(base, exp - 1)


def max_element(lst):
    """
    Find the maximum element in a list using recursion.

    @param lst: A non-empty list of comparable elements
    @return: The maximum element
    @rtype: int or float

    Examples:
        >>> max_element([1, 5, 3, 9, 2])
        9
        >>> max_element([0])
        0
    """
    if len(lst) == 1:
        return lst[0]
    element = lst[0]
    next_element = max_element(lst[1:])
    if next_element > element:
        element = next_element
    return element


def sum_to_n(n):
    """
    Calculate the sum of integers from 1 to n using recursion.

    @param n: A positive integer
    @return: The sum of integers from 1 to n
    @rtype: int

    Examples:
        >>> sum_to_n(5)
        15
        >>> sum_to_n(1)
        1
    """
    if n == 0:
        raise ValueError("n must begin from 1.")
    if n == 1:
        return 1
    return n + sum_to_n(n - 1)


def print_numbers(n):
    """
    Print numbers from n down to 1 using recursion.

    @param n: A positive integer
    @return: None

    Examples:
        >>> print_numbers(3)
        3
        2
        1
    """
    if n > 0:
        print(n)
        print_numbers(n - 1)


def count_up(n):
    """
    Print numbers from 1 up to n using recursion.

    @param n: A positive integer
    @return: None

    Examples:
        >>> count_up(3)
        1
        2
        3
    """
    if n > 0:
        count_up(n - 1)
        print(n)


def count_char(s, char):
    """
    Count occurrences of a character in a string using recursion.

    @param s: The input string
    @param char: The character to count
    @return: Number of occurrences of char in s
    @rtype: int

    Examples:
        >>> count_char("banana", "a")
        3
        >>> count_char("hello", "z")
        0
    """
    count = 0
    if len(s) == 0:
        return 0
    if s[0] == char:
        count += 1
    return count + count_char(s[1:], char)


def multiply(a, b):
    """
    Multiply two non-negative integers using recursive addition.

    @param a: First non-negative integer
    @param b: Second non-negative integer
    @return: Product of a and b
    @rtype: int

    Examples:
        >>> multiply(3, 4)
        12
        >>> multiply(5, 0)
        0
    """
    if a < 0 or b < 0:
        raise ValueError("integers must be non-negative")
    if b == 1:
        return b
    if a == 0 or b == 0:
        return 0
    multiply(a, b - 1)
    return a * b


def print_reverse(s):
    """
    Print characters of a string in reverse order using recursion.

    @param s: The input string
    @return: None

    Examples:
        >>> print_reverse("abc")
        c
        b
        a
    """
    if len(s) > 0:
        print(s[len(s) - 1])
        print_reverse(s[:len(s) - 1])


def even_sum(n):
    """
    Calculate the sum of even numbers from 1 to n using recursion.

    @param n: A positive integer
    @return: Sum of even numbers from 1 to n
    @rtype: int

    Examples:
        >>> even_sum(6)
        12
        >>> even_sum(3)
        2
    """
    if n <= 0:
        raise ValueError("n must be a non-negative integer")
    if n == 1:
        return 0
    total = 0
    if n % 2 == 0:
        total += n
    return total + even_sum(n - 1)


def remove_char(s, char):
    """
    Remove all occurrences of a character from a string using recursion.

    @param s: The input string
    @param char: The character to remove
    @return: String with all instances of char removed
    @rtype: str

    Examples:
        >>> remove_char("banana", "a")
        'bnn'
        >>> remove_char("hello", "l")
        'heo'
    """
    if len(s) == 0:
        return s
    string = ""
    if s[0] != char:
        string += s[0]
    return string + remove_char(s[1:], char)


def sum_squares(n):
    """
    Calculate the sum of squares of integers from 1 to n using recursion.

    @param n: A positive integer
    @return: Sum of squares from 1 to n
    @rtype: int

    Examples:
        >>> sum_squares(3)
        14
        >>> sum_squares(1)
        1
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 1:
        return 1
    sum_of_squares = n * n
    return sum_of_squares + sum_squares(n - 1)


def is_power_of_two(n):
    """
    Check if a number is a power of 2 using recursion.

    @param n: A positive integer
    @return: True if n is a power of 2, False otherwise
    @rtype: bool

    Examples:
        >>> is_power_of_two(8)
        True
        >>> is_power_of_two(6)
        False
    """
    if n < 0:
        raise ValueError("n must be a positive integer")
    if n == 0:
        return False
    if n == 1:
        return True
    return is_power_of_two(n // 2)


def append_to_list(lst, n):
    """
    Create a list of numbers from 1 to n using recursion.

    @param lst: The list to append to (initially empty)
    @param n: A positive integer
    @return: List containing numbers from 1 to n
    @rtype: list

    Examples:
        >>> append_to_list([], 3)
        [1, 2, 3]
        >>> append_to_list([], 1)
        [1]
    """
    if n <= 0:
        raise ValueError("n must start from 1")
    if n == 1:
        lst.insert(0, 1)
        return lst
    append_to_list(lst, n - 1)
    lst.append(n)
    return lst


def product_list(lst):
    """
    Calculate the product of all elements in a list using recursion.

    @param lst: A list of numbers
    @return: The product of all elements
    @rtype: int or float

    Examples:
        >>> product_list([2, 3, 4])
        24
        >>> product_list([])
        1
    """
    if len(lst) == 0:
        return 1
    product = lst[0]
    if product == 0:
        raise ValueError("0 cannot be in the list.")
    return product * product_list(lst[1:])


def count_vowels(s):
    """
    Count the number of vowels (a, e, i, o, u) in a string using recursion.

    @param s: The input string
    @return: The number of vowels
    @rtype: int

    Examples:
        >>> count_vowels("hello")
        2
        >>> count_vowels("")
        0
    """
    if len(s) == 0:
        return 0
    vowels = ["a", "e", "i", "o", "u"]
    num_vowels = 0
    if s[0].lower() in vowels:
        num_vowels += 1
    return num_vowels + count_vowels(s[1:])


def sum_odd(n):
    """
    Calculate the sum of odd numbers from 1 to n using recursion.

    @param n: A positive integer
    @return: The sum of odd numbers from 1 to n
    @rtype: int

    Examples:
        >>> sum_odd(5)
        9
        >>> sum_odd(4)
        4
    """
    if n <= 0:
        raise ValueError("n must be a positive number")
    if n == 1:
        return n
    odd_sum = 0
    if n % 2 != 0:
        odd_sum += n
    return odd_sum + sum_odd(n-1)


def replace_char(s, old, new):
    """
    Replace all occurrences of a character with a new character in a string using recursion.

    @param s: The input string
    @param old: The character to replace
    @param new: The new character
    @return: The string with all old characters replaced by new
    @rtype: str

    Examples:
        >>> replace_char("hello", "l", "x")
        'hexxo'
        >>> replace_char("", "a", "b")
        ''
    """
    if len(old) == 0 or len(new) == 0:
        raise ValueError("Nothing to replace")
    if len(s) == 0:
        return s
    new_s = ""
    if s[0] == old:
        new_s += new
    else:
        new_s += s[0]
    return new_s + replace_char(s[1:], old, new)

def find_min(lst):
    """
    Find the minimum element in a non-empty list using recursion.

    @param lst: A non-empty list of comparable elements
    @return: The minimum element
    @rtype: int or float

    Examples:
        >>> find_min([4, 2, 7, 1, 9])
        1
        >>> find_min([5])
        5
    """
    if len(lst) == 0:
        raise ValueError("Empty list passed")
    if len(lst) == 1:
        return lst[0]
    curr_min = lst[0]
    next_min = find_min(lst[1:])
    if next_min < curr_min:
        curr_min = next_min
    return curr_min


def capitalize_string(s):
    """
    Capitalize the first letter of a string using recursion.

    @param s: The input string
    @return: The string with its first letter capitalized
    @rtype: str

    Examples:
        >>> capitalize_string("hello")
        'Hello'
        >>> capitalize_string("")
        ''
        >>> capitalize_string("this is a sample text")
        'This Is A Sample Text'
    """
    if len(s) == 0:
        return s
    if not(97 <= ord(s[0]) <= 122):
        return s
    if s.count(" ") == 0:
        return s.capitalize()
    return s[:s.index(" ")].capitalize() + " " + capitalize_string(s[s.index(" ") + 1:])



def sum_multiples_three(n):
    """
    Calculate the sum of all multiples of 3 from 1 to n using recursion.

    @param n: A positive integer
    @return: The sum of multiples of 3 from 1 to n
    @rtype: int

    Examples:
        >>> sum_multiples_three(9)
        18
        >>> sum_multiples_three(5)
        3
    """
    if n <= 0:
        raise ValueError("n must be non-negative integer")
    if n == 1:
        return n
    total = 0
    if n % 3 == 0:
        total += n
    return total + sum_multiples_three(n)


def recursive_len(s):
    """
    Calculate the length of a string using recursion.

    @param s: The input string
    @return: The length of the string
    @rtype: int

    Examples:
        >>> recursive_len("python")
        6
        >>> recursive_len("")
        0
    """
    if s == "":
        return 0
    str_len = 1
    return str_len + recursive_len(s[1:])


def count_occurrences(lst, target):
    """
    Count the number of occurrences of a target value in a list using recursion.

    @param lst: A list of elements
    @param target: The value to count
    @return: The number of times target appears in lst
    @rtype: int

    Examples:
        >>> count_occurrences([1, 2, 1, 3, 1], 1)
        3
        >>> count_occurrences([], 5)
        0
    """
    if len(lst) == 0:
        return 0
    count = 0
    if lst[0] == target:
        count += 1
    return count + count_occurrences(lst[1:], target)


def is_sorted(lst):
    """
    Check if a list is sorted in ascending order using recursion.

    @param lst: A list of comparable elements
    @return: True if the list is sorted in ascending order, False otherwise
    @rtype: bool

    Examples:
        >>> is_sorted([1, 2, 3, 4])
        True
        >>> is_sorted([1, 3, 2, 4])
        False
    """
    if len(lst) <= 1:
        return True
    current_element = lst[0]
    next_element = lst[1]
    return (current_element < next_element) and is_sorted(lst[1:])


def sum_even_indices(lst):
    """
    Calculate the sum of elements at even indices in a list using recursion.

    @param lst: A list of numbers
    @return: The sum of elements at even indices (0, 2, 4, ...)
    @rtype: int or float

    Examples:
        >>> sum_even_indices([1, 2, 3, 4, 5])
        9
        >>> sum_even_indices([])
        0
    """
    if len(lst) == 0:
        return 0
    count = lst[0]
    return count + sum_even_indices(lst[2:])

def count_consonants(s):
    """
    Count the number of consonants in a string using recursion.

    @param s: The input string
    @return: The number of consonants (non-vowel letters)
    @rtype: int

    Examples:
        >>> count_consonants("hello")
        3
        >>> count_consonants("")
        0
    """
    if len(s) == 0:
        return 0
    vowels = ["a", "e", "i", "o", "u", "y"]
    count = 0
    if s[0].lower() not in vowels:
        count += 1
    return count + count_consonants(s[1:])


def product_odd(n):
    """
    Calculate the product of odd numbers from 1 to n using recursion.

    @param n: A positive integer
    @return: The product of odd numbers from 1 to n
    @rtype: int

    Examples:
        >>> product_odd(5)
        15
        >>> product_odd(4)
        3
    """
    if n <= 0:
        raise ValueError("n must be a non-negative integer")
    if n == 1:
        return n
    product = 1
    if n % 2 != 0:
        product *= n
    return product * product_odd(n-1)


def reverse_list(lst):
    """
    Reverse a list using recursion.

    @param lst: A list of any elements
    @return: The reversed list
    @rtype: list

    Examples:
        >>> reverse_list([1, 2, 3])
        [3, 2, 1]
        >>> reverse_list([])
        []
    """
    if len(lst) == 0:
        return lst
    new_list = []
    new_list.insert(0, lst[0])
    return reverse_list(lst[1:]) + new_list


def count_greater(lst, threshold):
    """
    Count the number of elements in a list greater than a threshold using recursion.

    @param lst: A list of numbers
    @param threshold: The threshold value
    @return: The number of elements greater than threshold
    @rtype: int

    Examples:
        >>> count_greater([1, 5, 3, 7, 2], 3)
        2
        >>> count_greater([], 0)
        0
    """
    if len(lst) == 0 or threshold == 0:
        return 0
    count = 0
    if lst[0] > threshold:
        count += 1
    return count + count_greater(lst[1:], threshold)


def to_uppercase(s):
    """
    Convert a string to uppercase using recursion.

    @param s: The input string
    @return: The string in uppercase
    @rtype: str

    Examples:
        >>> to_uppercase("hello")
        'HELLO'
        >>> to_uppercase("")
        ''
    """
    if len(s) == 0:
        return s
    return s[0].upper() + to_uppercase(s[1:])


def sum_divisible_by_five(n):
    """
    Calculate the sum of numbers divisible by 5 from 1 to n using recursion.

    @param n: A positive integer
    @return: The sum of numbers divisible by 5 from 1 to n
    @rtype: int

    Examples:
        >>> sum_divisible_by_five(15)
        30
        >>> sum_divisible_by_five(4)
        0
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return 0
    sum_num = 0
    if n % 5 == 0:
        sum_num += n
    return sum_num + sum_divisible_by_five(n-1)


def recursive_index(lst, target):
    """
    Find the index of the first occurrence of a target value in a list using recursion.

    @param lst: A list of elements
    @param target: The value to find
    @return: The index of target if found, -1 otherwise
    @rtype: int

    Examples:
        >>> recursive_index([1, 2, 3, 2], 2)
        1
        >>> recursive_index([1, 3, 4], 5)
        -1
    """
    if len(lst) == 1:
        if target == lst[0]:
            return 0
    if target not in lst or len(lst) == 0:
        return -1
    count = 0
    if lst[0] != target:
        count += 1
    if lst[0] == target:
        return count
    return count + recursive_index(lst[1:], target)

def remove_duplicates(s):
    """
    Remove consecutive duplicate characters from a string using recursion.

    @param s: The input string
    @return: The string with consecutive duplicates removed
    @rtype: str

    Examples:
        >>> remove_duplicates("hello")
        'helo'
        >>> remove_duplicates("")
        ''
    """
    if len(s) == 0:
        return s
    if len(s) == 1:
        return s
    current_char = s[0]
    next_char = s[1]
    new_s = ""
    if current_char != next_char:
        new_s += current_char
    return new_s + remove_duplicates(s[1:])

def is_power_of_three(n):
    """
    Check if a number is a power of 3 using recursion.

    @param n: A positive integer
    @return: True if n is a power of 3, False otherwise
    @rtype: bool

    Examples:
        >>> is_power_of_three(9)
        True
        >>> is_power_of_three(10)
        False
    """
    if n < 0:
        raise ValueError("n must be a positive integer")
    if n == 0:
        return False
    if n == 1:
        return True
    return is_power_of_three(n // 3)


def sum_odd_indices(lst):
    """
    Calculate the sum of elements at odd indices in a list using recursion.

    @param lst: A list of numbers
    @return: The sum of elements at odd indices (1, 3, 5, ...)
    @rtype: int or float

    Examples:
        >>> sum_odd_indices([1, 2, 3, 4, 5])
        6
        >>> sum_odd_indices([])
        0
    """
    if len(lst) <= 1:
        return 0
    count = lst[1]
    return count + sum_odd_indices(lst[2:])


def count_digits(s):
    """
    Count the number of digit characters in a string using recursion.

    @param s: The input string
    @return: The number of digits
    @rtype: int

    Examples:
        >>> count_digits("abc123")
        3
        >>> count_digits("")
        0
    """
    if len(s) == 0:
        return 0
    count = 0
    if s[0].isdigit():
        count += 1
    return count + count_digits(s[1:])


def product_even(n):
    """
    Calculate the product of even numbers from 1 to n using recursion.

    @param n: A positive integer
    @return: The product of even numbers from 1 to n
    @rtype: int

    Examples:
        >>> product_even(6)
        48
        >>> product_even(3)
        2
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return n
    product = 1
    if n % 2 == 0:
        product *= n
    return product * product_even(n-1)


def prepend_to_list(lst, n):
    """
    Create a list of numbers from n down to 1 using recursion.

    @param lst: The list to prepend to (initially empty)
    @param n: A positive integer
    @return: List containing numbers from n to 1
    @rtype: list

    Examples:
        >>> prepend_to_list([], 3)
        [3, 2, 1]
        >>> prepend_to_list([], 1)
        [1]
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        lst.append(n)
        return lst
    lst.append(n)
    return prepend_to_list(lst, n-1)


def count_less(lst, threshold):
    """
    Count the number of elements in a list less than a threshold using recursion.

    @param lst: A list of numbers
    @param threshold: The threshold value
    @return: The number of elements less than threshold
    @rtype: int

    Examples:
        >>> count_less([1, 5, 3, 7, 2], 4)
        3
        >>> count_less([], 0)
        0
    """
    if len(lst) == 0 or threshold == 0:
        return 0
    if threshold < 0:
        raise ValueError("threshold cannot be negative")
    count = 0
    if lst[0] < threshold:
        count += 1
    return count + count_less(lst[1:], threshold)


def to_lowercase(s):
    """
    Convert a string to lowercase using recursion.

    @param s: The input string
    @return: The string in lowercase
    @rtype: str

    Examples:
        >>> to_lowercase("HELLO")
        'hello'
        >>> to_lowercase("")
        ''
    """
    if len(s) == 0:
        return s
    return s[0].lower() + to_lowercase(s[1:])


def sum_multiples_seven(n):
    """
    Calculate the sum of numbers divisible by 7 from 1 to n using recursion.

    @param n: A positive integer
    @return: The sum of numbers divisible by 7 from 1 to n
    @rtype: int

    Examples:
        >>> sum_multiples_seven(14)
        21
        >>> sum_multiples_seven(6)
        0
    """
    if n <= 0:
        raise ValueError("n must be a positive integer between 1 to n")
    if n == 1:
        return n
    total = 0
    if n % 7 == 0:
        total += n
    return total + sum_multiples_seven(n-1)


def recursive_last_index(lst, target):
    """
    Find the index of the last occurrence of a target value in a list using recursion.

    @param lst: A list of elements
    @param target: The value to find
    @return: The index of the last occurrence of target if found, -1 otherwise
    @rtype: int

    Examples:
        >>> recursive_last_index([1, 2, 3, 2], 2)
        3
        >>> recursive_last_index([1, 3, 4], 5)
        -1
    """
    if len(lst) == 0:
        return -1
    if target not in lst:
        return -1
    targe_index = len(lst)-1
    if lst[targe_index] == target:
        return targe_index
    return recursive_last_index(lst[:len(lst)-1], target)


def trim_spaces(s):
    """
    Remove leading and trailing spaces from a string using recursion.

    @param s: The input string
    @return: The string with leading and trailing spaces removed
    @rtype: str

    Examples:
        >>> trim_spaces("  hello  ")
        'hello'
        >>> trim_spaces("")
        ''
    """
    if len(s) == 0:
        return s
    my_str = ""
    if s[0] != " ":
        my_str += s[0]
    return my_str + trim_spaces(s[1:])



def is_power_of_five(n):
    """
    Check if a number is a power of 5 using recursion.

    @param n: A positive integer
    @return: True if n is a power of 5, False otherwise
    @rtype: bool

    Examples:
        >>> is_power_of_five(25)
        True
        >>> is_power_of_five(10)
        False
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return True
    if 1 < n < 5:
        return False
    return is_power_of_five(n // 5)


def sum_first_n_squares(n):
    """
    Calculate the sum of squares of the first n positive integers using recursion.

    @param n: A positive integer
    @return: The sum of squares from 1^2 to n^2
    @rtype: int

    Examples:
        >>> sum_first_n_squares(3)
        14
        >>> sum_first_n_squares(1)
        1
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return n
    count = 0
    count += n*n
    return count + sum_first_n_squares(n-1)


def count_uppercase(s):
    """
    Count the number of uppercase letters in a string using recursion.

    @param s: The input string
    @return: The number of uppercase letters
    @rtype: int

    Examples:
        >>> count_uppercase("Hello")
        1
        >>> count_uppercase("")
        0
    """
    if len(s) == 0:
        return 0
    count = 0
    if s[0].isupper():
        count += 1
    return count + count_uppercase(s[1:])


def product_multiples_four(n):
    """
    Calculate the product of numbers divisible by 4 from 1 to n using recursion.

    @param n: A positive integer
    @return: The product of numbers divisible by 4 from 1 to n
    @rtype: int

    Examples:
        >>> product_multiples_four(8)
        32
        >>> product_multiples_four(3)
        1
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return n
    product = 1
    if n % 4 == 0:
        product *= n
    return product * product_multiples_four(n-1)


def interleave_lists(lst1, lst2):
    """
    Interleave two lists of equal length into a single list using recursion.

    @param lst1: First list
    @param lst2: Second list
    @return: A list with elements interleaved from lst1 and lst2
    @rtype: list

    Examples:
        >>> interleave_lists([1, 3], [2, 4])
        [1, 2, 3, 4]
        >>> interleave_lists([], [])
        []
    """
    if len(lst1) != len(lst2):
        raise ValueError("lists must be of equal lengths")
    if len(lst1) == 0 and len(lst2) == 0:
        return lst1
    interleaved = []
    interleaved.insert(0, lst1[0])
    interleaved.insert(1, lst2[0])
    if len(lst1) == 1 and len(lst2) == 1:
        return interleaved
    return interleaved + interleave_lists(lst1[1:], lst2[1:])

def count_equal(lst, target):
    """
    Count the number of elements in a list equal to a target value using recursion.

    @param lst: A list of elements
    @param target: The value to count
    @return: The number of elements equal to target
    @rtype: int

    Examples:
        >>> count_equal([1, 2, 2, 3], 2)
        2
        >>> count_equal([], 1)
        0
    """
    if len(lst) == 0:
        return 0
    count = 0
    if lst[0] == target:
        count += 1
    return count + count_equal(lst[1:], target)


def alternate_case(s):
    """
    Convert a string to alternate case (first uppercase, second lowercase, etc.) using recursion.

    @param s: The input string
    @return: The string with alternating case
    @rtype: str

    Examples:
        >>> alternate_case("hello")
        'HeLlO'
        >>> alternate_case("louder")
        'LoUdEr'
        >>> alternate_case("")
        ''
    """
    if len(s) == 0:
        return s
    if len(s) == 1:
        return s.upper()
    new_str = ""
    if len(s) >= 2:
        new_str = s[0].upper() + s[1].lower()
    return new_str + alternate_case(s[2:])


def sum_multiples_nine(n):
    """
    Calculate the sum of numbers divisible by 9 from 1 to n using recursion.

    @param n: A positive integer
    @return: The sum of numbers divisible by 9 from 1 to n
    @rtype: int

    Examples:
        >>> sum_multiples_nine(18)
        27
        >>> sum_multiples_nine(8)
        0
    """
    if n <= 0:
        raise ValueError("n must be a positive integer greater than 0")
    if 0 < n < 9:
        return 0
    if n == 9:
        return n
    count = 0
    if n % 9 == 0:
        count += n
    return count + sum_multiples_nine(n-1)


def recursive_contains(lst, target):
    """
    Check if a list contains a target value using recursion.

    @param lst: A list of elements
    @param target: The value to find
    @return: True if target is in the list, False otherwise
    @rtype: bool

    Examples:
        >>> recursive_contains([1, 2, 3], 2)
        True
        >>> recursive_contains([1, 3, 4], 5)
        False
    """
    if len(lst) == 0:
        return False
    if lst[0] == target:
        return True
    return recursive_contains(lst[1:], target)


def remove_vowels(s):
    """
    Remove all vowels from a string using recursion.

    @param s: The input string
    @return: The string with all vowels removed
    @rtype: str

    Examples:
        >>> remove_vowels("hello")
        'hll'
        >>> remove_vowels("")
        ''
    """
    if len(s) == 0:
        return s
    vowels = ["a", "e", "i", "o", "u", "y"]
    new_s = ""
    if s[0].lower not in vowels:
        new_s += s[0]
    return new_s + remove_vowels(s[1:])


def is_power_of_ten(n):
    """
    Check if a number is a power of 10 using recursion.

    @param n: A positive integer
    @return: True if n is a power of 10, False otherwise
    @rtype: bool

    Examples:
        >>> is_power_of_ten(100)
        True
        >>> is_power_of_ten(50)
        False
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return True
    if 1 < n < 10:
        return False
    return True and is_power_of_ten(n//10)


def merge_alternate_strings(s1, s2):
    """
    Merge two strings by alternating their characters using recursion.

    @param s1: First string
    @param s2: Second string
    @return: A string with characters alternated from s1 and s2
    @rtype: str

    Examples:
        >>> merge_alternate_strings("abc", "xyz")
        'axbycz'
        >>> merge_alternate_strings("", "")
        ''
    """
    if len(s1) == 0 and len(s2) == 0:
        return s1
    if len(s1) == 0 and len(s2) > 0:
        return s2
    if len(s1) > 0 and len(s2) == 0:
        return s1
    s = s1[0] + s2[0]
    return s + merge_alternate_strings(s1[1:], s2[1:])


def count_pairs(lst, target_sum):
    """
    Count the number of adjacent pairs in a list that sum to a target value using recursion.

    @param lst: A list of numbers
    @param target_sum: The target sum for adjacent pairs
    @return: The number of adjacent pairs summing to target_sum
    @rtype: int

    Examples:
        >>> count_pairs([1, 2, 3, 4], 5)
        1
        >>> count_pairs([], 5)
        0
    """
    if len(lst) == 0 or len(lst) == 1:
        return 0
    count = 0
    if lst[0] + lst[1] == target_sum:
        count +=1
    return count + count_pairs(lst[1:], target_sum)


def split_by_sign(lst):
    """
    Split a list into two lists of positive and negative numbers using recursion.

    @param lst: A list of numbers
    @return: A tuple of two lists (positive numbers, negative numbers)
    @rtype: tuple

    Examples:
        >>> split_by_sign([1, -2, 3, -4])
        ([1, 3], [-2, -4])
        >>> split_by_sign([])
        ([], [])
    """
    if len(lst) == 0:
        return lst, lst
    positive = []
    negative = []
    if lst[0] > 0:
        positive.append(lst[0])
    else:
        negative.append(lst[0])
    return positive + split_by_sign(lst[1:])[0], negative + split_by_sign(lst[1:])[1]


def recursive_swap_case(s):
    """
    Swap the case of each letter in a string using recursion.

    @param s: The input string
    @return: The string with each letter's case swapped
    @rtype: str

    Examples:
        >>> recursive_swap_case("Hello")
        'hELLO'
        >>> recursive_swap_case("")
        ''
    """
    if len(s) == 0:
        return s
    new_s = ""
    if s[0].isupper():
        new_s += s[0].lower()
    else:
        new_s += s[0].upper()
    return new_s + recursive_swap_case(s[1:])


def max_difference(lst):
    """
    Find the maximum difference between any two adjacent elements in a list using recursion.

    @param lst: A list of numbers
    @return: The maximum difference between adjacent elements, 0 if list has fewer than 2 elements
    @rtype: int or float

    Examples:
        >>> max_difference([1, 5, 2, 8])
        6
        >>> max_difference([1])
        0
    """
    if len(lst) == 0 or len(lst) == 1:
        return 0
    curr_diff = abs(lst[0] - lst[1])
    difference = curr_diff
    next_diff = max_difference(lst[1:])
    if curr_diff < next_diff:
        difference = next_diff
    return difference


def count_alternating(lst):
    """
    Count the number of elements in a list that alternate in sign (positive, negative, positive, ...) using recursion.

    @param lst: A list of numbers
    @return: The length of the longest prefix with alternating signs
    @rtype: int

    Examples:
        >>> count_alternating([1, -2, 3, -4, 5])
        2
        >>> count_alternating([1, 2, -3])
        1
    """
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return 1
    count = 0
    if lst[0] > 0 > lst[1]:
        count += 1
    if lst[0] < 0 < lst[1]:
        count += 1
    if lst[0] > 0 and lst[1] > 0:
        count += 1
        return count
    if lst[0] < 0 and lst[1] < 0:
        count += 1
        return count
    return count + count_alternating(lst[1:])


def recursive_join(strings, separator):
    """
    Join a list of strings with a separator using recursion.

    @param strings: A list of strings
    @param separator: The separator string
    @return: The joined string
    @rtype: str

    Examples:
        >>> recursive_join(["a", "b", "c"], "-")
        'a-b-c'
        >>> recursive_join([], "-")
        ''
    """
    if len(strings) == 0:
        return ""
    if len(strings) == 1:
        return strings[0]
    new_s = strings[0] + separator
    return new_s + recursive_join(strings[1:], separator)


def remove_consecutive_numbers(lst):
    """
    Remove consecutive identical numbers from a list using recursion.

    @param lst: A list of numbers
    @return: The list with consecutive identical numbers reduced to one
    @rtype: list

    Examples:
        >>> remove_consecutive_numbers([1, 1, 2, 2, 3])
        [1, 2, 3]
        >>> remove_consecutive_numbers([])
        []
    """
    if len(lst) == 0:
        return lst
    new_lst = [lst[0]]
    return new_lst + remove_consecutive_numbers(lst[2::])


def count_valid_substrings(s):
    """
    Count the number of substrings with equal numbers of 'a' and 'b' characters using recursion.

    @param s: A string containing only 'a' and 'b'
    @return: The number of substrings with equal 'a' and 'b' counts
    @rtype: int

    Examples:
        >>> count_valid_substrings("aabb")
        2
        >>> count_valid_substrings("ab")
        1
    """
    pass


def recursive_partition(lst, n):
    """
    Partition a list into sublists of size n using recursion.

    @param lst: A list of elements
    @param n: Size of each sublist
    @return: A list of sublists, each of size n (last may be smaller)
    @rtype: list

    Examples:
        >>> recursive_partition([1, 2, 3, 4, 5], 2)
        [[1, 2], [3, 4], [5]]
        >>> recursive_partition([], 3)
        []
    """
    if len(lst) == 0 or n == 0:
        return lst
    if len(lst) == 1:
        return [[lst[0]]]
    if len(lst) <= n:
        return lst
    new_lst = lst[0:n]
    return [new_lst] + recursive_partition(lst[n:], n)


def sum_alternating_series(n):
    """
    Calculate the sum of the series n + (n-2) + (n-4) + ... until the term <= 0 using recursion.

    @param n: A positive integer
    @return: The sum of the series
    @rtype: int

    Examples:
        >>> sum_alternating_series(6)
        12  # 6 + 4 + 2
        >>> sum_alternating_series(5)
        9   # 5 + 3 + 1
        >>> sum_alternating_series(4)
        6   # 4 + 2
    """
    if n <= 0:
        return 0
    return n + sum_alternating_series(n-2)


def harmonic_sum(n):
    """
    Calculate the sum of the harmonic series up to n terms: 1 + 1/2 + 1/3 + ... + 1/n using recursion.

    @param n: A positive integer
    @return: The sum of the harmonic series up to n terms
    @rtype: float

    Examples:
        >>> harmonic_sum(3)
        1.8333333333333333  # 1 + 1/2 + 1/3
        >>> harmonic_sum(1)
        1.0
        >>> harmonic_sum(5)
        2.283333333333333
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return n
    return 1/n + harmonic_sum(n-1)


def geometric_sum(n):
    """
    Calculate the sum of the geometric series up to n terms with r=2: 1 + 2 + 4 + ... + 2^{n-1} using recursion.

    @param n: A positive integer
    @return: The sum of the geometric series
    @rtype: int

    Examples:
        >>> geometric_sum(3)
        7  # 1 + 2 + 4
        >>> geometric_sum(1)
        1  # 1
        >>> geometric_sum(5)
        31  # 1 + 2 + 4 + 8 + 16
    """
    if n < 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return n
    return 2**(n-1) + geometric_sum(n-1)


def gcd(a, b):
    """
    Find the greatest common divisor of two positive integers a and b using recursion.

    @param a: First positive integer
    @param b: Second positive integer
    @return: GCD of a and b
    @rtype: int

    Examples:
        >>> gcd(48, 18)
        6
        >>> gcd(17, 13)
        1
        >>> gcd(100, 80)
        20
        >>> gcd(128, 96)
        32
    """
    if a <= 0 or b <= 0:
        raise ValueError("parameters must be positive")
    if a == b:
        return a
    if a > b:
        return gcd(a - b, b)
    return gcd(a, b - a)



def climb_stairs(n):
    """
    Calculate the number of ways to climb n stairs, taking 1 or 2 steps at a time, using recursion.

    @param n: Number of stairs, non-negative integer
    @return: Number of ways to climb
    @rtype: int

    Examples:
        >>> climb_stairs(6)
        13
        >>> climb_stairs(5)
        8
        >>> climb_stairs(4)
        5
        >>> climb_stairs(3)
        3  # 1+1+1, 1+2, 2+1
        >>> climb_stairs(2)
        2  # 1+1, 2
        >>> climb_stairs(1)
        1  # 1
    """
    if n < 0:
        raise ValueError("n must be a positive integer")
    if n == 1 or n == 0:
        return 1
    if n == 2:
        return n
    return climb_stairs(n - 2) + climb_stairs(n - 1)



def merge_sorted_lists(lst1, lst2):
    """
    Merge two sorted lists into one sorted list using recursion.

    @param lst1: First sorted list
    @param lst2: Second sorted list
    @return: Merged sorted list
    @rtype: list

    Examples:
        >>> merge_sorted_lists([1, 3, 5], [2, 4, 6])
        [1, 2, 3, 4, 5, 6]
        >>> merge_sorted_lists([1, 2, 3], [])
        [1, 2, 3]
        >>> merge_sorted_lists([], [4, 5, 6])
        [4, 5, 6]
    """
    if len(lst1) == 0 and len(lst2) != 0:
        return lst2
    if len(lst1) != 0 and len(lst2) == 0:
        return lst1
    if lst1[0] < lst2[0]:
        return [lst1[0]] + merge_sorted_lists(lst1[1:], lst2[0:])
    else:
        return [lst2[0]] + merge_sorted_lists(lst1[0:], lst2[1:])

def longest_common_prefix(str1, str2):
    """
    Find the longest common prefix of two strings using recursion.

    @param str1: First string
    @param str2: Second string
    @return: The longest common prefix
    @rtype: str

    Examples:
        >>> longest_common_prefix("flower", "flow")
        "flow"
        >>> longest_common_prefix("interspecies", "interstellar")
        "inters"
        >>> longest_common_prefix("dog", "cat")
        ""
    """
    if len(str1) == 0 or len(str2) == 0:
        return ""
    if str1[0] != str2[0]:
        return ""
    prefix = ""
    if str1[0] == str2[0]:
        prefix += str1[0]
    return prefix + longest_common_prefix(str1[1:], str2[1:])


def contains_string(main, sub):
    """
    Determine if main string contains sub string using recursion.

    @param main: The main string to search in
    @param sub: The substring to search for
    @return: True if main contains sub, False otherwise
    @rtype: bool

    Examples:
        >>> contains_string("hello world", "world")
        True
        >>> contains_string("hello", "bye")
        False
        >>> contains_string("", "")
        True  # Empty string contains empty string
    """
    if len(main) == 0 and len(sub) != 0:
        return False
    if len(main) == 0 and len(sub) == 0:
        return True
    if len(main) < len(sub):
        return False
    if " " in main:
        compare = main[0:len(sub)]
        if compare.startswith(" "):
            compare = main[1:len(sub)+1]
        if compare.endswith(" "):
            compare = main[0:len(sub)-1]
    else:
        compare = main[:len(sub)]
    if compare == sub:
        return True
    return compare and contains_string(main[1:], sub)


def count_nested_depth(lst):
    """
    Calculate the maximum nesting depth of a nested list using recursion.

    @param lst: A list that may contain nested lists
    @return: The maximum nesting depth (empty list has depth 0)
    @rtype: int

    Examples:
        >>> count_nested_depth([1, [2, 3], [4, [5]]])
        3
        >>> count_nested_depth([])
        0
        >>> count_nested_depth([1, 2, 3])
        1
    """
    if len(lst) == 0:
        return 0
    depth = 0
    if isinstance(lst, list):
        depth += 1
    return depth + count_nested_depth(lst[1:])


def interleave_strings(s1, s2, k):
    """
    Interleave two strings, taking up to k characters from each at a time, using recursion.

    @param s1: First string
    @param s2: Second string
    @param k: Maximum number of characters to take from each string at a time
    @return: Interleaved string
    @rtype: str

    Examples:
        >>> interleave_strings("abc", "xyz", 2)
        'abxy'
        >>> interleave_strings("hello", "world", 1)
        'hweolrllod'
        >>> interleave_strings("", "abc", 2)
        'abc'
    """
    if k < 0:
        raise ValueError("k must be a positive integer")
    if k == 0:
        return s1 + s2
    if len(s1) == 0 and not len(s2) == 0:
        return s2
    if len(s1) != 0 and len(s2) == 0:
        return s1
    s = s1[0:k] + s2[0:k]
    if len(s1[k:]) < k or len(s2[k:]) < k:
        return s
    return s + interleave_strings(s1[k:], s2[k:], k)


def sum_digits_recursive(n):
    """
    Calculate the sum of digits in a non-negative integer using recursion.

    @param n: A non-negative integer
    @return: Sum of its digits
    @rtype: int

    Examples:
        >>> sum_digits_recursive(123)
        6  # 1 + 2 + 3
        >>> sum_digits_recursive(0)
        0
        >>> sum_digits_recursive(9999)
        36  # 9 + 9 + 9 + 9
    """
    if n == 0:
        return n
    total = n % 10
    return total + sum_digits_recursive(n // 10)


def count_substring_occurrences(main, sub):
    """
    Count the number of non-overlapping occurrences of a substring in a string using recursion.

    @param main: The main string to search in
    @param sub: The substring to search for
    @return: Number of non-overlapping occurrences
    @rtype: int

    Examples:
        >>> count_substring_occurrences("banana", "ana")
        2  # "ana" at positions 2-4 and 4-6
        >>> count_substring_occurrences("aaaa", "aa")
        2  # "aa" at positions 1-2 and 3-4
        >>> count_substring_occurrences("abc", "xyz")
        0
    """
    pass


def flatten_list(lst):
    """
    Flatten a nested list into a single list using recursion.

    @param lst: A list that may contain nested lists
    @return: A flattened list containing all non-list elements
    @rtype: list

    Examples:
        >>> flatten_list([1, [2, 3], [4, [5]]])
        [1, 2, 3, 4, 5]
        >>> flatten_list([])
        []
        >>> flatten_list([[1], [2], [3]])
        [1, 2, 3]
    """
    if len(lst) == 0:
        return lst
    new_lst = []
    if isinstance(lst[0], list):
        for i in range len(lst)


def recursive_palindrome(s):
    """
    Check if a string is a palindrome, ignoring non-alphanumeric characters, using recursion.

    @param s: The input string
    @return: True if the string is a palindrome, False otherwise
    @rtype: bool

    Examples:
        >>> recursive_palindrome("A man, a plan, a canal: Panama")
        True
        >>> recursive_palindrome("race a car")
        False
        >>> recursive_palindrome("")
        True
    """
    pass


def count_paths(m, n):
    """
    Count the number of ways to move from top-left to bottom-right in an m x n grid, moving only right or down, using recursion.

    @param m: Number of rows
    @param n: Number of columns
    @return: Number of possible paths
    @rtype: int

    Examples:
        >>> count_paths(2, 2)
        2  # Paths: right-down, down-right
        >>> count_paths(3, 3)
        6
        >>> count_paths(1, 1)
        1
    """
    pass


def recursive_split(s, sep):
    """
    Split a string into a list of substrings based on a separator using recursion.

    @param s: The input string
    @param sep: The separator character
    @return: List of substrings
    @rtype: list

    Examples:
        >>> recursive_split("a,b,c", ",")
        ['a', 'b', 'c']
        >>> recursive_split("hello", " ")
        ['hello']
        >>> recursive_split("", ",")
        []
    """
    pass

def max_element_nested(lst):
    """
    Find the maximum element in a nested list using recursion.

    @param lst: A list containing numbers and/or nested lists of numbers
    @return: The maximum number in the list
    @rtype: int or float

    Examples:
        >>> max_element_nested([1, [2, 3], [4, [5]]])
        5
        >>> max_element_nested([1, 2, 3])
        3
        >>> max_element_nested([[1], [2], [3]])
        3
    """
    pass

def count_balanced_prefixes(s):
    """
    Count the number of prefixes in a string of '(' and ')' that are balanced using recursion.

    @param s: A string containing only '(' and ')'
    @return: Number of balanced prefixes
    @rtype: int

    Examples:
        >>> count_balanced_prefixes("()")
        1  # Prefix: "()"
        >>> count_balanced_prefixes("(())")
        2  # Prefixes: "()", "(())"
        >>> count_balanced_prefixes("(()")
        1  # Prefix: "()"
    """
    pass

if __name__ == "__main__":
    print(sum_digits_recursive(9999))
