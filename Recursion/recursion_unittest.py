import unittest

# from io import StringIO
# import sys
from recursion import *


class TestRecursionProblems(unittest.TestCase):
    def test_factorial(self):
        """Test factorial function for various inputs."""
        self.assertEqual(factorial(4), 24, "factorial(4) should return 24")
        self.assertEqual(factorial(0), 1, "factorial(0) should return 1")
        self.assertEqual(factorial(1), 1, "factorial(1) should return 1")
        self.assertEqual(factorial(5), 120, "factorial(5) should return 120")
        with self.assertRaises(ValueError):
            factorial(-1)  # Assuming negative inputs raise ValueError

    def test_sum_to_n(self):
        """Test sum_to_n function for summing integers from 1 to n."""
        self.assertEqual(sum_to_n(5), 15, "sum_to_n(5) should return 15")
        self.assertEqual(sum_to_n(1), 1, "sum_to_n(1) should return 1")
        self.assertEqual(sum_to_n(3), 6, "sum_to_n(3) should return 6")
        with self.assertRaises(ValueError):
            sum_to_n(0)  # Assuming non-positive inputs raise ValueError

    # def test_print_numbers(self):
    #     """Test print_numbers function by capturing printed output."""
    #     captured_output = StringIO()
    #     sys.stdout = captured_output
    #     print_numbers(3)
    #     sys.stdout = sys.__stdout__
    #     self.assertEqual(captured_output.getvalue(), "3\n2\n1\n", "print_numbers(3) should print 3, 2, 1")
    #     captured_output = StringIO()
    #     sys.stdout = captured_output
    #     print_numbers(1)
    #     sys.stdout = sys.__stdout__
    #     self.assertEqual(captured_output.getvalue(), "1\n", "print_numbers(1) should print 1")

    # def test_count_up(self):
    #     """Test count_up function by capturing printed output."""
    #     captured_output = StringIO()
    #     sys.stdout = captured_output
    #     count_up(3)
    #     sys.stdout = sys.__stdout__
    #     self.assertEqual(captured_output.getvalue(), "1\n2\n3\n", "count_up(3) should print 1, 2, 3")
    #     captured_output = StringIO()
    #     sys.stdout = captured_output
    #     count_up(1)
    #     sys.stdout = sys.__stdout__
    #     self.assertEqual(captured_output.getvalue(), "1\n", "count_up(1) should print 1")

    def test_sum_list(self):
        """Test sum_list function for various lists."""
        self.assertEqual(sum_array([1, 2, 3]), 6, "sum_list([1, 2, 3]) should return 6")
        self.assertEqual(sum_array([]), 0, "sum_list([]) should return 0")
        self.assertEqual(sum_array([5]), 5, "sum_list([5]) should return 5")
        self.assertEqual(sum_array([1.5, 2.5]), 4.0, "sum_list([1.5, 2.5]) should return 4.0")

    def test_count_elements(self):
        """Test count_elements function for various lists."""
        self.assertEqual(count_elements([1, 2, 3, 4]), 4, "count_elements([1, 2, 3, 4]) should return 4")
        self.assertEqual(count_elements([]), 0, "count_elements([]) should return 0")
        self.assertEqual(count_elements(["a"]), 1, "count_elements(['a']) should return 1")
        self.assertEqual(count_elements([None, None]), 2, "count_elements([None, None]) should return 2")

    def test_reverse_string(self):
        """Test reverse_string function for various strings."""
        self.assertEqual(reverse_string("hello"), "olleh", "reverse_string('hello') should return 'olleh'")
        self.assertEqual(reverse_string(""), "", "reverse_string('') should return ''")
        self.assertEqual(reverse_string("a"), "a", "reverse_string('a') should return 'a'")
        self.assertEqual(reverse_string("123"), "321", "reverse_string('123') should return '321'")

    def test_power(self):
        """Test power function for various base and exponent inputs."""
        self.assertEqual(power(2, 3), 8, "power(2, 3) should return 8")
        self.assertEqual(power(3, 2), 9, "power(3, 2) should return 9")
        self.assertEqual(power(5, 0), 1, "power(5, 0) should return 1")
        self.assertEqual(power(2.5, 2), 6.25, "power(2.5, 2) should return 6.25")
        with self.assertRaises(ValueError):
            power(2, -1)  # Assuming negative exponents raise ValueError

    def test_is_palindrome(self):
        """Test is_palindrome function for various strings."""
        self.assertTrue(is_palindrome("racecar"), "is_palindrome('racecar') should return True")
        self.assertFalse(is_palindrome("hello"), "is_palindrome('hello') should return False")
        self.assertTrue(is_palindrome(""), "is_palindrome('') should return True")
        self.assertTrue(is_palindrome("a"), "is_palindrome('a') should return True")

    def test_sum_digits(self):
        """Test sum_digits function for various integers."""
        self.assertEqual(sum_digits(123), 6, "sum_digits(123) should return 6")
        self.assertEqual(sum_digits(0), 0, "sum_digits(0) should return 0")
        self.assertEqual(sum_digits(999), 27, "sum_digits(999) should return 27")
        self.assertEqual(sum_digits(1), 1, "sum_digits(1) should return 1")
        with self.assertRaises(ValueError):
            sum_digits(-123)  # Assuming negative inputs raise ValueError

    def test_fibonacci(self):
        """Test fibonacci function for various positions."""
        self.assertEqual(fibonacci(5), 5, "fibonacci(5) should return 5")
        self.assertEqual(fibonacci(0), 0, "fibonacci(0) should return 0")
        self.assertEqual(fibonacci(1), 1, "fibonacci(1) should return 1")
        self.assertEqual(fibonacci(7), 13, "fibonacci(7) should return 13")
        with self.assertRaises(ValueError):
            fibonacci(-1)  # Assuming negative inputs raise ValueError

    def test_find_max(self):
        """Test find_max function for various lists."""
        self.assertEqual(max_element([1, 4, 2, 8, 5]), 8, "find_max([1, 4, 2, 8, 5]) should return 8")
        self.assertEqual(max_element([3]), 3, "find_max([3]) should return 3")
        self.assertEqual(max_element([-1, -5, -2]), -1, "find_max([-1, -5, -2]) should return -1")
        self.assertEqual(max_element([1.5, 2.5, 0.5]), 2.5, "find_max([1.5, 2.5, 0.5]) should return 2.5")

    def test_count_char(self):
        """Test count_char function for various strings and characters."""
        self.assertEqual(count_char("banana", "a"), 3, "count_char('banana', 'a') should return 3")
        self.assertEqual(count_char("hello", "z"), 0, "count_char('hello', 'z') should return 0")
        self.assertEqual(count_char("", "a"), 0, "count_char('', 'a') should return 0")
        self.assertEqual(count_char("aaa", "a"), 3, "count_char('aaa', 'a') should return 3")

    def test_multiply(self):
        """Test multiply function for various inputs."""
        self.assertEqual(multiply(3, 4), 12, "multiply(3, 4) should return 12")
        self.assertEqual(multiply(5, 0), 0, "multiply(5, 0) should return 0")
        self.assertEqual(multiply(0, 5), 0, "multiply(0, 5) should return 0")
        self.assertEqual(multiply(1, 7), 7, "multiply(1, 7) should return 7")
        with self.assertRaises(ValueError):
            multiply(-1, 2)  # Assuming negative inputs raise ValueError

    # def test_print_reverse(self):
    #     """Test print_reverse function by capturing printed output."""
    #     captured_output = StringIO()
    #     sys.stdout = captured_output
    #     print_reverse("abc")
    #     sys.stdout = sys.__stdout__
    #     self.assertEqual(captured_output.getvalue(), "c\nb\na\n", "print_reverse('abc') should print c, b, a")
    #     captured_output = StringIO()
    #     sys.stdout = captured_output
    #     print_reverse("")
    #     sys.stdout = sys.__stdout__
    #     self.assertEqual(captured_output.getvalue(), "", "print_reverse('') should print nothing")

    def test_even_sum(self):
        """Test even_sum function for summing even numbers."""
        self.assertEqual(even_sum(6), 12, "even_sum(6) should return 12 (2+4+6)")
        self.assertEqual(even_sum(3), 2, "even_sum(3) should return 2 (2)")
        self.assertEqual(even_sum(4), 6, "even_sum(4) should return 6 (2+4)")
        self.assertEqual(even_sum(1), 0, "even_sum(1) should return 0")
        with self.assertRaises(ValueError):
            even_sum(0)  # Assuming non-positive inputs raise ValueError

    def test_remove_char(self):
        """Test remove_char function for various strings and characters."""
        self.assertEqual(remove_char("banana", "a"), "bnn", "remove_char('banana', 'a') should return 'bnn'")
        self.assertEqual(remove_char("hello", "l"), "heo", "remove_char('hello', 'l') should return 'heo'")
        self.assertEqual(remove_char("", "a"), "", "remove_char('', 'a') should return ''")
        self.assertEqual(remove_char("test", "x"), "test", "remove_char('test', 'x') should return 'test'")

    def test_sum_squares(self):
        """Test sum_squares function for summing squares."""
        self.assertEqual(sum_squares(3), 14, "sum_squares(3) should return 14 (1+4+9)")
        self.assertEqual(sum_squares(1), 1, "sum_squares(1) should return 1")
        self.assertEqual(sum_squares(4), 30, "sum_squares(4) should return 30 (1+4+9+16)")
        self.assertEqual(sum_squares(2), 5, "sum_squares(2) should return 5 (1+4)")
        with self.assertRaises(ValueError):
            sum_squares(0)  # Assuming non-positive inputs raise ValueError

    def test_is_power_of_two(self):
        """Test is_power_of_two function for various inputs."""
        self.assertTrue(is_power_of_two(8), "is_power_of_two(8) should return True")
        self.assertFalse(is_power_of_two(6), "is_power_of_two(6) should return False")
        self.assertTrue(is_power_of_two(1), "is_power_of_two(1) should return True")
        self.assertTrue(is_power_of_two(4), "is_power_of_two(4) should return True")
        with self.assertRaises(ValueError):
            is_power_of_two(0)  # Assuming non-positive inputs raise ValueError

    def test_append_to_list(self):
        """Test append_to_list function for creating lists."""
        self.assertEqual(append_to_list([], 3), [1, 2, 3], "append_to_list([], 3) should return [1, 2, 3]")
        self.assertEqual(append_to_list([], 1), [1], "append_to_list([], 1) should return [1]")
        self.assertEqual(append_to_list([], 5), [1, 2, 3, 4, 5], "append_to_list([], 5) should return [1, 2, 3, 4, 5]")
        with self.assertRaises(ValueError):
            append_to_list([], 0)  # Assuming non-positive inputs raise ValueError

    def test_product_list(self):
        """Test product_list function for various lists."""
        self.assertEqual(product_list([2, 3, 4]), 24, "product_list([2, 3, 4]) should return 24")
        self.assertEqual(product_list([]), 1, "product_list([]) should return 1")
        self.assertEqual(product_list([5]), 5, "product_list([5]) should return 5")
        self.assertEqual(product_list([1.5, 2]), 3.0, "product_list([1.5, 2]) should return 3.0")
        with self.assertRaises(ValueError):
            product_list([0, 1, 2])  # Assuming zero in list raises ValueError for clarity

    def test_count_vowels(self):
        """Test count_vowels function for various strings."""
        self.assertEqual(count_vowels("hello"), 2, "count_vowels('hello') should return 2")
        self.assertEqual(count_vowels(""), 0, "count_vowels('') should return 0")
        self.assertEqual(count_vowels("python"), 1, "count_vowels('python') should return 1")
        self.assertEqual(count_vowels("AeIoU"), 5, "count_vowels('AeIoU') should return 5")
        self.assertEqual(count_vowels("xyz"), 0, "count_vowels('xyz') should return 0")

    def test_sum_odd(self):
        """Test sum_odd function for summing odd numbers."""
        self.assertEqual(sum_odd(5), 9, "sum_odd(5) should return 9 (1+3+5)")
        self.assertEqual(sum_odd(4), 4, "sum_odd(4) should return 4 (1+3)")
        self.assertEqual(sum_odd(1), 1, "sum_odd(1) should return 1")
        self.assertEqual(sum_odd(6), 9, "sum_odd(6) should return 9 (1+3+5)")
        with self.assertRaises(ValueError):
            sum_odd(0)  # Assuming non-positive inputs raise ValueError

    def test_replace_char(self):
        """Test replace_char function for various strings and characters."""
        self.assertEqual(replace_char("hello", "l", "x"), "hexxo",
                         "replace_char('hello', 'l', 'x') should return 'hexxo'")
        self.assertEqual(replace_char("", "a", "b"), "", "replace_char('', 'a', 'b') should return ''")
        self.assertEqual(replace_char("test", "z", "y"), "test", "replace_char('test', 'z', 'y') should return 'test'")
        self.assertEqual(replace_char("aaa", "a", "b"), "bbb", "replace_char('aaa', 'a', 'b') should return 'bbb'")
        with self.assertRaises(ValueError):
            replace_char("hello", "", "x")  # Assuming empty old char raises ValueError

    def test_find_min(self):
        """Test find_min function for various lists."""
        self.assertEqual(find_min([4, 2, 7, 1, 9]), 1, "find_min([4, 2, 7, 1, 9]) should return 1")
        self.assertEqual(find_min([5]), 5, "find_min([5]) should return 5")
        self.assertEqual(find_min([-1, -5, -2]), -5, "find_min([-1, -5, -2]) should return -5")
        self.assertEqual(find_min([1.5, 0.5, 2.5]), 0.5, "find_min([1.5, 0.5, 2.5]) should return 0.5")
        with self.assertRaises(ValueError):
            find_min([])  # Assuming empty list raises ValueError

    def test_capitalize_string(self):
        """Test capitalize_string function for various strings."""
        self.assertEqual(capitalize_string("hello"), "Hello", "capitalize_string('hello') should return 'Hello'")
        self.assertEqual(capitalize_string(""), "", "capitalize_string('') should return ''")
        self.assertEqual(capitalize_string("a"), "A", "capitalize_string('a') should return 'A'")
        self.assertEqual(capitalize_string("Python"), "Python", "capitalize_string('Python') should return 'Python'")
        self.assertEqual(capitalize_string("123abc"), "123abc", "capitalize_string('123abc') should return '123abc'")
        self.assertEqual(capitalize_string("this is a sample text"),
                         "This Is A Sample Text",
                         "capitalize_string('this is a sample text') should return 'This Is A Sample Text'")

    def test_is_sorted(self):
        """Test is_sorted function for various lists."""
        self.assertTrue(is_sorted([1, 2, 3, 4]), "is_sorted([1, 2, 3, 4]) should return True")
        self.assertFalse(is_sorted([1, 3, 2, 4]), "is_sorted([1, 3, 2, 4]) should return False")
        self.assertTrue(is_sorted([1]), "is_sorted([1]) should return True")
        self.assertTrue(is_sorted([]), "is_sorted([]) should return True")
        self.assertTrue(is_sorted([1.5, 2.5, 3.5]), "is_sorted([1.5, 2.5, 3.5]) should return True")
        self.assertFalse(is_sorted([2, 2, 1]), "is_sorted([2, 2, 1]) should return False")

    def test_sum_even_indices(self):
        """Test sum_even_indices function for various lists."""
        self.assertEqual(sum_even_indices([1, 2, 3, 4, 5]), 9,
                         "sum_even_indices([1, 2, 3, 4, 5]) should return 9 (1+3+5)")
        self.assertEqual(sum_even_indices([]), 0, "sum_even_indices([]) should return 0")
        self.assertEqual(sum_even_indices([1]), 1, "sum_even_indices([1]) should return 1")
        self.assertEqual(sum_even_indices([1.5, 2, 3.5, 4]), 5.0,
                         "sum_even_indices([1.5, 2, 3.5, 4]) should return 5.0 (1.5+3.5)")
        self.assertEqual(sum_even_indices([2, 3, 4]), 6, "sum_even_indices([2, 3, 4]) should return 6 (2+4)")

    def test_count_consonants(self):
        """Test count_consonants function for various strings."""
        self.assertEqual(count_consonants("hello"), 3, "count_consonants('hello') should return 3")
        self.assertEqual(count_consonants(""), 0, "count_consonants('') should return 0")
        self.assertEqual(count_consonants("aeiou"), 0, "count_consonants('aeiou') should return 0")
        self.assertEqual(count_consonants("python"), 4, "count_consonants('python') should return 4")
        self.assertEqual(count_consonants("HELLO"), 3, "count_consonants('HELLO') should return 3")

    def test_product_odd(self):
        """Test product_odd function for multiplying odd numbers."""
        self.assertEqual(product_odd(5), 15, "product_odd(5) should return 15 (1*3*5)")
        self.assertEqual(product_odd(4), 3, "product_odd(4) should return 3 (1*3)")
        self.assertEqual(product_odd(1), 1, "product_odd(1) should return 1")
        self.assertEqual(product_odd(6), 15, "product_odd(6) should return 15 (1*3*5)")
        with self.assertRaises(ValueError):
            product_odd(0)  # Assuming non-positive inputs raise ValueError

    def test_reverse_list(self):
        """Test reverse_list function for various lists."""
        self.assertEqual(reverse_list([1, 2, 3]), [3, 2, 1], "reverse_list([1, 2, 3]) should return [3, 2, 1]")
        self.assertEqual(reverse_list([]), [], "reverse_list([]) should return []")
        self.assertEqual(reverse_list([1]), [1], "reverse_list([1]) should return [1]")
        self.assertEqual(reverse_list(["a", "b", "c"]), ["c", "b", "a"],
                         "reverse_list(['a', 'b', 'c']) should return ['c', 'b', 'a']")
        self.assertEqual(reverse_list([1.5, 2.5]), [2.5, 1.5], "reverse_list([1.5, 2.5]) should return [2.5, 1.5]")

    def test_count_greater(self):
        """Test count_greater function for various lists and thresholds."""
        self.assertEqual(count_greater([1, 5, 3, 7, 2], 3), 2, "count_greater([1, 5, 3, 7, 2], 3) should return 2")
        self.assertEqual(count_greater([], 0), 0, "count_greater([], 0) should return 0")
        self.assertEqual(count_greater([1, 2, 3], 5), 0, "count_greater([1, 2, 3], 5) should return 0")
        self.assertEqual(count_greater([4, 4, 4], 4), 0, "count_greater([4, 4, 4], 4) should return 0")
        self.assertEqual(count_greater([1.5, 2.5, 3.5], 2.0), 2, "count_greater([1.5, 2.5, 3.5], 2.0) should return 2")

    def test_to_uppercase(self):
        """Test to_uppercase function for various strings."""
        self.assertEqual(to_uppercase("hello"), "HELLO", "to_uppercase('hello') should return 'HELLO'")
        self.assertEqual(to_uppercase(""), "", "to_uppercase('') should return ''")
        self.assertEqual(to_uppercase("Python"), "PYTHON", "to_uppercase('Python') should return 'PYTHON'")
        self.assertEqual(to_uppercase("123abc"), "123ABC", "to_uppercase('123abc') should return '123ABC'")
        self.assertEqual(to_uppercase("A"), "A", "to_uppercase('A') should return 'A'")

    def test_sum_divisible_by_five(self):
        """Test sum_divisible_by_five function for summing multiples of 5."""
        self.assertEqual(sum_divisible_by_five(15), 30, "sum_divisible_by_five(15) should return 30 (5+10+15)")
        self.assertEqual(sum_divisible_by_five(4), 0, "sum_divisible_by_five(4) should return 0")
        self.assertEqual(sum_divisible_by_five(5), 5, "sum_divisible_by_five(5) should return 5")
        self.assertEqual(sum_divisible_by_five(20), 50, "sum_divisible_by_five(20) should return 50 (5+10+15+20)")
        with self.assertRaises(ValueError):
            sum_divisible_by_five(0)  # Assuming non-positive inputs raise ValueError

    def test_recursive_index(self):
        """Test recursive_index function for finding indices."""
        self.assertEqual(recursive_index([1, 2, 3, 2], 2), 1, "recursive_index([1, 2, 3, 2], 2) should return 1")
        self.assertEqual(recursive_index([1, 3, 4], 5), -1, "recursive_index([1, 3, 4], 5) should return -1")
        self.assertEqual(recursive_index([1], 1), 0, "recursive_index([1], 1) should return 0")
        self.assertEqual(recursive_index([], 1), -1, "recursive_index([], 1) should return -1")
        self.assertEqual(recursive_index(["a", "b", "a"], "a"), 0,
                         "recursive_index(['a', 'b', 'a'], 'a') should return 0")

    def test_remove_duplicates(self):
        """Test remove_duplicates function for removing consecutive duplicates."""
        self.assertEqual(remove_duplicates("hello"), "helo", "remove_duplicates('hello') should return 'helo'")
        self.assertEqual(remove_duplicates(""), "", "remove_duplicates('') should return ''")
        self.assertEqual(remove_duplicates("aaa"), "a", "remove_duplicates('aaa') should return 'a'")
        self.assertEqual(remove_duplicates("abcd"), "abcd", "remove_duplicates('abcd') should return 'abcd'")
        self.assertEqual(remove_duplicates("aabbcc"), "abc", "remove_duplicates('aabbcc') should return 'abc'")

    def test_is_power_of_three(self):
        """Test is_power_of_three function for various inputs."""
        self.assertTrue(is_power_of_three(9), "is_power_of_three(9) should return True")
        self.assertFalse(is_power_of_three(10), "is_power_of_three(10) should return False")
        self.assertTrue(is_power_of_three(1), "is_power_of_three(1) should return True")
        self.assertTrue(is_power_of_three(27), "is_power_of_three(27) should return True")
        self.assertFalse(is_power_of_three(6), "is_power_of_three(6) should return False")
        with self.assertRaises(ValueError):
            is_power_of_three(0)  # Assuming non-positive inputs raise ValueError

    def test_sum_odd_indices(self):
        """Test sum_odd_indices function for various lists."""
        self.assertEqual(sum_odd_indices([1, 2, 3, 4, 5]), 6, "sum_odd_indices([1, 2, 3, 4, 5]) should return 6 (2+4)")
        self.assertEqual(sum_odd_indices([]), 0, "sum_odd_indices([]) should return 0")
        self.assertEqual(sum_odd_indices([1]), 0, "sum_odd_indices([1]) should return 0")
        self.assertEqual(sum_odd_indices([1.5, 2.5, 3.5, 4.5]), 7.0,
                         "sum_odd_indices([1.5, 2.5, 3.5, 4.5]) should return 7.0 (2.5+4.5)")
        self.assertEqual(sum_odd_indices([2, 3, 4, 5]), 8, "sum_odd_indices([2, 3, 4, 5]) should return 8 (3+5)")

    def test_count_digits(self):
        """Test count_digits function for various strings."""
        self.assertEqual(count_digits("abc123"), 3, "count_digits('abc123') should return 3")
        self.assertEqual(count_digits(""), 0, "count_digits('') should return 0")
        self.assertEqual(count_digits("no digits"), 0, "count_digits('no digits') should return 0")
        self.assertEqual(count_digits("12345"), 5, "count_digits('12345') should return 5")
        self.assertEqual(count_digits("a1b2c3"), 3, "count_digits('a1b2c3') should return 3")

    def test_product_even(self):
        """Test product_even function for multiplying even numbers."""
        self.assertEqual(product_even(6), 48, "product_even(6) should return 48 (2*4*6)")
        self.assertEqual(product_even(3), 2, "product_even(3) should return 2")
        self.assertEqual(product_even(1), 1, "product_even(1) should return 1")
        self.assertEqual(product_even(8), 384, "product_even(8) should return 384 (2*4*6*8)")
        with self.assertRaises(ValueError):
            product_even(0)  # Assuming non-positive inputs raise ValueError

    def test_prepend_to_list(self):
        """Test prepend_to_list function for creating descending lists."""
        self.assertEqual(prepend_to_list([], 3), [3, 2, 1], "prepend_to_list([], 3) should return [3, 2, 1]")
        self.assertEqual(prepend_to_list([], 1), [1], "prepend_to_list([], 1) should return [1]")
        self.assertEqual(prepend_to_list([], 5), [5, 4, 3, 2, 1],
                         "prepend_to_list([], 5) should return [5, 4, 3, 2, 1]")
        with self.assertRaises(ValueError):
            prepend_to_list([], 0)  # Assuming non-positive inputs raise ValueError
        self.assertEqual(prepend_to_list([0], 2), [2, 1, 0], "prepend_to_list([0], 2) should return [2, 1, 0]")

    def test_count_less(self):
        """Test count_less function for various lists and thresholds."""
        self.assertEqual(count_less([1, 5, 3, 7, 2], 4), 3, "count_less([1, 5, 3, 7, 2], 4) should return 3")
        self.assertEqual(count_less([], 0), 0, "count_less([], 0) should return 0")
        self.assertEqual(count_less([1, 2, 3], 0), 0, "count_less([1, 2, 3], 0) should return 0")
        self.assertEqual(count_less([4, 4, 4], 4), 0, "count_less([4, 4, 4], 4) should return 0")
        self.assertEqual(count_less([1.5, 2.5, 3.5], 3.0), 2, "count_less([1.5, 2.5, 3.5], 3.0) should return 2")

    def test_to_lowercase(self):
        """Test to_lowercase function for various strings."""
        self.assertEqual(to_lowercase("HELLO"), "hello", "to_lowercase('HELLO') should return 'hello'")
        self.assertEqual(to_lowercase(""), "", "to_lowercase('') should return ''")
        self.assertEqual(to_lowercase("Python"), "python", "to_lowercase('Python') should return 'python'")
        self.assertEqual(to_lowercase("123ABC"), "123abc", "to_lowercase('123ABC') should return '123abc'")
        self.assertEqual(to_lowercase("a"), "a", "to_lowercase('a') should return 'a'")

    def test_sum_multiples_seven(self):
        """Test sum_multiples_seven function for summing multiples of 7."""
        self.assertEqual(sum_multiples_seven(14), 21, "sum_multiples_seven(14) should return 21 (7+14)")
        self.assertEqual(sum_multiples_seven(6), 0, "sum_multiples_seven(6) should return 0")
        self.assertEqual(sum_multiples_seven(7), 7, "sum_multiples_seven(7) should return 7")
        self.assertEqual(sum_multiples_seven(21), 42, "sum_multiples_seven(21) should return 42 (7+14+21)")
        with self.assertRaises(ValueError):
            sum_multiples_seven(0)  # Assuming non-positive inputs raise ValueError

    def test_recursive_last_index(self):
        """Test recursive_last_index function for finding last indices."""
        self.assertEqual(recursive_last_index([1, 2, 3, 2], 2), 3,
                         "recursive_last_index([1, 2, 3, 2], 2) should return 3")
        self.assertEqual(recursive_last_index([1, 3, 4], 5), -1, "recursive_last_index([1, 3, 4], 5) should return -1")
        self.assertEqual(recursive_last_index([1], 1), 0, "recursive_last_index([1], 1) should return 0")
        self.assertEqual(recursive_last_index([], 1), -1, "recursive_last_index([], 1) should return -1")
        self.assertEqual(recursive_last_index(["a", "b", "a"], "a"), 2,
                         "recursive_last_index(['a', 'b', 'a'], 'a') should return 2")

    def test_trim_spaces(self):
        """Test trim_spaces function for removing leading and trailing spaces."""
        self.assertEqual(trim_spaces("  hello  "), "hello", "trim_spaces('  hello  ') should return 'hello'")
        self.assertEqual(trim_spaces(""), "", "trim_spaces('') should return ''")
        self.assertEqual(trim_spaces("hello"), "hello", "trim_spaces('hello') should return 'hello'")
        self.assertEqual(trim_spaces("   "), "", "trim_spaces('   ') should return ''")
        self.assertEqual(trim_spaces(" hi "), "hi", "trim_spaces(' hi ') should return 'hi'")

    def test_is_power_of_five(self):
        """Test is_power_of_five function for various inputs."""
        self.assertTrue(is_power_of_five(25), "is_power_of_five(25) should return True")
        self.assertFalse(is_power_of_five(10), "is_power_of_five(10) should return False")
        self.assertTrue(is_power_of_five(1), "is_power_of_five(1) should return True")
        self.assertTrue(is_power_of_five(125), "is_power_of_five(125) should return True")
        self.assertFalse(is_power_of_five(15), "is_power_of_five(15) should return False")
        with self.assertRaises(ValueError):
            is_power_of_five(0)  # Assuming non-positive inputs raise ValueError

    def test_sum_first_n_squares(self):
        """Test sum_first_n_squares function for summing squares."""
        self.assertEqual(sum_first_n_squares(3), 14, "sum_first_n_squares(3) should return 14 (1+4+9)")
        self.assertEqual(sum_first_n_squares(1), 1, "sum_first_n_squares(1) should return 1")
        self.assertEqual(sum_first_n_squares(4), 30, "sum_first_n_squares(4) should return 30 (1+4+9+16)")
        self.assertEqual(sum_first_n_squares(2), 5, "sum_first_n_squares(2) should return 5 (1+4)")
        with self.assertRaises(ValueError):
            sum_first_n_squares(0)  # Assuming non-positive inputs raise ValueError

    def test_count_uppercase(self):
        """Test count_uppercase function for counting uppercase letters."""
        self.assertEqual(count_uppercase("Hello"), 1, "count_uppercase('Hello') should return 1")
        self.assertEqual(count_uppercase(""), 0, "count_uppercase('') should return 0")
        self.assertEqual(count_uppercase("PYTHON"), 6, "count_uppercase('PYTHON') should return 6")
        self.assertEqual(count_uppercase("hello"), 0, "count_uppercase('hello') should return 0")
        self.assertEqual(count_uppercase("Hi123"), 1, "count_uppercase('Hi123') should return 1")

    def test_product_multiples_four(self):
        """Test product_multiples_four function for multiplying multiples of 4."""
        self.assertEqual(product_multiples_four(8), 32, "product_multiples_four(8) should return 32 (4*8)")
        self.assertEqual(product_multiples_four(3), 1, "product_multiples_four(3) should return 1")
        self.assertEqual(product_multiples_four(4), 4, "product_multiples_four(4) should return 4")
        self.assertEqual(product_multiples_four(12), 192, "product_multiples_four(12) should return 192 (4*8*12)")
        with self.assertRaises(ValueError):
            product_multiples_four(0)  # Assuming non-positive inputs raise ValueError

    def test_interleave_lists(self):
        """Test interleave_lists function for interleaving two lists."""
        self.assertEqual(interleave_lists([1, 3], [2, 4]), [1, 2, 3, 4],
                         "interleave_lists([1, 3], [2, 4]) should return [1, 2, 3, 4]")
        self.assertEqual(interleave_lists([], []), [], "interleave_lists([], []) should return []")
        self.assertEqual(interleave_lists([1], [2]), [1, 2], "interleave_lists([1], [2]) should return [1, 2]")
        self.assertEqual(interleave_lists(["a", "c"], ["b", "d"]), ["a", "b", "c", "d"],
                         "interleave_lists(['a', 'c'], ['b', 'd']) should return ['a', 'b', 'c', 'd']")
        with self.assertRaises(ValueError):
            interleave_lists([1, 2], [3])  # Assuming unequal lengths raise ValueError

    def test_count_equal(self):
        """Test count_equal function for counting elements equal to target."""
        self.assertEqual(count_equal([1, 2, 2, 3], 2), 2, "count_equal([1, 2, 2, 3], 2) should return 2")
        self.assertEqual(count_equal([], 1), 0, "count_equal([], 1) should return 0")
        self.assertEqual(count_equal([1, 1, 1], 1), 3, "count_equal([1, 1, 1], 1) should return 3")
        self.assertEqual(count_equal([1, 2, 3], 4), 0, "count_equal([1, 2, 3], 4) should return 0")
        self.assertEqual(count_equal(["a", "b", "a"], "a"), 2, "count_equal(['a', 'b', 'a'], 'a') should return 2")

    def test_alternate_case(self):
        """Test alternate_case function for alternating case."""
        self.assertEqual(alternate_case("hello"), "HeLlO", "alternate_case('hello') should return 'HeLlO'")
        self.assertEqual(alternate_case(""), "", "alternate_case('') should return ''")
        self.assertEqual(alternate_case("python"), "PyThOn", "alternate_case('python') should return 'PyThOn'")
        self.assertEqual(alternate_case("A"), "A", "alternate_case('A') should return 'A'")
        self.assertEqual(alternate_case("hi"), "Hi", "alternate_case('hi') should return 'Hi'")

    def test_sum_multiples_nine(self):
        """Test sum_multiples_nine function for summing multiples of 9."""
        self.assertEqual(sum_multiples_nine(18), 27, "sum_multiples_nine(18) should return 27 (9+18)")
        self.assertEqual(sum_multiples_nine(8), 0, "sum_multiples_nine(8) should return 0")
        self.assertEqual(sum_multiples_nine(9), 9, "sum_multiples_nine(9) should return 9")
        self.assertEqual(sum_multiples_nine(27), 54, "sum_multiples_nine(27) should return 54 (9+18+27)")
        with self.assertRaises(ValueError):
            sum_multiples_nine(0)  # Assuming non-positive inputs raise ValueError

    def test_recursive_contains(self):
        """Test recursive_contains function for checking if target is in list."""
        self.assertTrue(recursive_contains([1, 2, 3], 2), "recursive_contains([1, 2, 3], 2) should return True")
        self.assertFalse(recursive_contains([1, 3, 4], 5), "recursive_contains([1, 3, 4], 5) should return False")
        self.assertTrue(recursive_contains([1], 1), "recursive_contains([1], 1) should return True")
        self.assertFalse(recursive_contains([], 1), "recursive_contains([], 1) should return False")
        self.assertTrue(recursive_contains(["a", "b"], "a"), "recursive_contains(['a', 'b'], 'a') should return True")

    def test_remove_vowels(self):
        """Test remove_vowels function for removing vowels."""
        self.assertEqual(remove_vowels("hello"), "hll", "remove_vowels('hello') should return 'hll'")
        self.assertEqual(remove_vowels(""), "", "remove_vowels('') should return ''")
        self.assertEqual(remove_vowels("aeiou"), "", "remove_vowels('aeiou') should return ''")
        self.assertEqual(remove_vowels("python"), "pythn", "remove_vowels('python') should return 'pythn'")
        self.assertEqual(remove_vowels("HELLO"), "HLL", "remove_vowels('HELLO') should return 'HLL'")

    def test_is_power_of_ten(self):
        """Test is_power_of_ten function for checking powers of 10."""
        self.assertTrue(is_power_of_ten(100), "is_power_of_ten(100) should return True")
        self.assertFalse(is_power_of_ten(50), "is_power_of_ten(50) should return False")
        self.assertTrue(is_power_of_ten(1), "is_power_of_ten(1) should return True")
        self.assertTrue(is_power_of_ten(1000), "is_power_of_ten(1000) should return True")
        self.assertFalse(is_power_of_ten(20), "is_power_of_ten(20) should return False")
        with self.assertRaises(ValueError):
            is_power_of_ten(0)  # Assuming non-positive inputs raise ValueError

    def test_merge_alternate_strings(self):
        """Test merge_alternate_strings for various string pairs."""
        self.assertEqual(merge_alternate_strings("abc", "xyz"), "axbycz", "Should alternate equal length strings")
        self.assertEqual(merge_alternate_strings("abcd", "xy"), "axbycd", "Should handle s1 longer than s2")
        self.assertEqual(merge_alternate_strings("ab", "xyz"), "axbyz", "Should handle s2 longer than s1")
        self.assertEqual(merge_alternate_strings("", ""), "", "Should handle empty strings")
        self.assertEqual(merge_alternate_strings("", "abc"), "abc", "Should handle empty s1")
        self.assertEqual(merge_alternate_strings("abc", ""), "abc", "Should handle empty s2")

    def test_count_pairs(self):
        """Test count_pairs for various lists and target sums."""
        self.assertEqual(count_pairs([1, 2, 3, 4], 5), 1, "Should count one pair summing to 5")
        self.assertEqual(count_pairs([1, 2, 3, 4], 10), 0, "Should find no pairs summing to 10")
        self.assertEqual(count_pairs([1], 5), 0, "Should return 0 for single element")
        self.assertEqual(count_pairs([], 5), 0, "Should return 0 for empty list")
        self.assertEqual(count_pairs([1, 4, 1, 4], 5), 3, "Should count three pairs summing to 5")
        self.assertEqual(count_pairs([-1, 6, -1, 6], 5), 3, "Should handle negative numbers")

    def test_split_by_sign(self):
        """Test split_by_sign for various number lists."""
        self.assertEqual(split_by_sign([1, -2, 3, -4]), ([1, 3], [-2, -4]), "Should split mixed signs")
        self.assertEqual(split_by_sign([1, 2, 3]), ([1, 2, 3], []), "Should handle all positive")
        self.assertEqual(split_by_sign([-1, -2, -3]), ([], [-1, -2, -3]), "Should handle all negative")
        self.assertEqual(split_by_sign([0, 1, -1, 0]), ([1], [-1]), "Should exclude zeros")
        self.assertEqual(split_by_sign([]), ([], []), "Should handle empty list")
        self.assertEqual(split_by_sign([0]), ([], []), "Should handle single zero")

    def test_recursive_swap_case(self):
        """Test recursive_swap_case for various strings."""
        self.assertEqual(recursive_swap_case("Hello"), "hELLO", "Should swap mixed case")
        self.assertEqual(recursive_swap_case("HELLO"), "hello", "Should swap all uppercase")
        self.assertEqual(recursive_swap_case("hello"), "HELLO", "Should swap all lowercase")
        self.assertEqual(recursive_swap_case(""), "", "Should handle empty string")
        self.assertEqual(recursive_swap_case("123!@"), "123!@", "Should preserve non-letters")
        self.assertEqual(recursive_swap_case("Hello, World!"), "hELLO, wORLD!", "Should handle mixed content")

    def test_max_difference(self):
        """Test max_difference for various number lists."""
        self.assertEqual(max_difference([1, 5, 2, 8]), 6, "Should find max difference |8-2|=6")
        self.assertEqual(max_difference([1, 2]), 1, "Should handle two elements")
        self.assertEqual(max_difference([3, 3, 3]), 0, "Should return 0 for same elements")
        self.assertEqual(max_difference([-1, -5, -2]), 4, "Should handle negative numbers")
        self.assertEqual(max_difference([1]), 0, "Should return 0 for single element")
        self.assertEqual(max_difference([]), 0, "Should return 0 for empty list")

    def test_count_alternating(self):
        """Test count_alternating for various number lists."""
        self.assertEqual(count_alternating([1, -2, 3, -4, 5]), 5, "Should count full alternating prefix")
        self.assertEqual(count_alternating([1, 2, -3]), 1, "Should match example (possible typo)")
        self.assertEqual(count_alternating([1]), 1, "Should handle single element")
        self.assertEqual(count_alternating([]), 0, "Should handle empty list")
        self.assertEqual(count_alternating([1, -1]), 2, "Should count one alternating elements")
        self.assertEqual(count_alternating([1, 1]), 1, "Should stop at same sign")
        self.assertEqual(count_alternating([-1, 1, -1]), 3, "Should count two alternating elements")
        self.assertEqual(count_alternating([-1, -1, 1]), 1, "Should stop at same sign")
        self.assertEqual(count_alternating([1, 0, 0, -1]), 1, "Should count full alternating prefix")
        self.assertEqual(count_alternating([3]), 1, "Should return 1 for single positive element")
        self.assertEqual(count_alternating([-5]), 1, "Should return 1 for single negative element")
        self.assertEqual(count_alternating([1, 1, -3]), 1, "Should stop at second positive (1, 1)")
        self.assertEqual(count_alternating([-2, -3, 4]), 1, "Should stop at second negative (-2, -3)")
        self.assertEqual(count_alternating([1, -2, 2]), 3, "Should stop at second positive (-2, 2) after alternating")
        self.assertEqual(count_alternating([1, -2, 0, -4]), 2, "Should stop at zero after alternating [1, -2]")
        self.assertEqual(count_alternating([0, 1, -2]), 2, "Should stop immediately at zero")
        self.assertEqual(count_alternating([-1, 0]), 1, "Should count first negative before zero")
        self.assertEqual(count_alternating([2, -2, 2, -2, 2, -2]), 6,  "Should count 6 for full alternating sequence")
        self.assertEqual(count_alternating([-1, 2, -3, 4, -5, -6]), 5,  "Should stop at second negative (-5, -6) after 5 alternating elements")
        self.assertEqual(count_alternating([1.5, -2.7, 3.2, -4.1]), 4,  "Should count 4 for full alternating floating-point sequence")
        self.assertEqual(count_alternating([-0.5, 1.2, -2.3, 3.4]), 4,  "Should count 4 starting with negative")
        self.assertEqual(count_alternating([1, -1, 1, 1]), 3,  "Should stop at second positive (1, 1) after 3 alternating")
        self.assertEqual(count_alternating([-1, 1, -1, 0]), 3,  "Should stop at zero after 3 alternating")
        self.assertEqual(count_alternating([1.0, -1.0, 1.0]), 3,  "Should count 3 for exact floating-point alternation")

    def test_recursive_join(self):
        """Test recursive_join for various string lists and separators."""
        self.assertEqual(recursive_join(["a", "b", "c"], "-"), "a-b-c", "Should join with hyphen")
        self.assertEqual(recursive_join([], "-"), "", "Should handle empty list")
        self.assertEqual(recursive_join(["a"], "-"), "a", "Should handle single string")
        self.assertEqual(recursive_join(["a", "b"], ""), "ab", "Should handle empty separator")
        self.assertEqual(recursive_join(["hello", "world"], " "), "hello world", "Should join with space")

    def test_remove_consecutive_numbers(self):
        """Test remove_consecutive_numbers for various number lists."""
        self.assertEqual(remove_consecutive_numbers([1, 1, 2, 2, 3]), [1, 2, 3], "Should remove duplicates")
        self.assertEqual(remove_consecutive_numbers([]), [], "Should handle empty list")
        self.assertEqual(remove_consecutive_numbers([1]), [1], "Should handle single element")
        self.assertEqual(remove_consecutive_numbers([1, 2, 3]), [1, 2, 3], "Should preserve unique elements")
        self.assertEqual(remove_consecutive_numbers([1, 1, 1, 2, 2, 3, 3, 3]), [1, 2, 3],
                         "Should handle multiple duplicates")

    def test_count_valid_substrings(self):
        """Test count_valid_substrings for various 'a' and 'b' strings."""
        self.assertEqual(count_valid_substrings("aabb"), 2, "Should count 'ab' and 'aabb'")
        self.assertEqual(count_valid_substrings("ab"), 1, "Should count 'ab'")
        self.assertEqual(count_valid_substrings("aba"), 2, "Should count 'ab' and 'ba'")
        self.assertEqual(count_valid_substrings(""), 0, "Should handle empty string")
        self.assertEqual(count_valid_substrings("a"), 0, "Should handle single 'a'")
        self.assertEqual(count_valid_substrings("b"), 0, "Should handle single 'b'")
        self.assertEqual(count_valid_substrings("aa"), 0, "Should handle all 'a's")
        self.assertEqual(count_valid_substrings("bb"), 0, "Should handle all 'b's")
        self.assertEqual(count_valid_substrings("abab"), 4, "Should count 'ab', 'ba', 'ab', 'abab'")

    def test_recursive_partition(self):
        """Test recursive_partition for various lists and partition sizes."""
        self.assertEqual(recursive_partition([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]], "Should partition into size 2")
        self.assertEqual(recursive_partition([], 3), [], "Should handle empty list")
        self.assertEqual(recursive_partition([1], 1), [[1]], "Should handle single element")
        self.assertEqual(recursive_partition([1, 2, 3], 4), [[1, 2, 3]], "Should handle n > list length")
        self.assertEqual(recursive_partition([1, 2, 3, 4], 1), [[1], [2], [3], [4]], "Should partition into size 1")
        self.assertEqual(recursive_partition([1, 2, 3, 4, 5, 6], 3), [[1, 2, 3], [4, 5, 6]],
                         "Should partition into size 3")

    def test_sum_alternating_series(self):
        """Test sum_alternating_series for various inputs."""
        self.assertEqual(sum_alternating_series(6), 12, "Should return 12 (6+4+2)")
        self.assertEqual(sum_alternating_series(5), 9, "Should return 9 (5+3+1)")
        self.assertEqual(sum_alternating_series(4), 6, "Should return 6 (4+2)")
        self.assertEqual(sum_alternating_series(1), 1, "Should return 1")
        with self.assertRaises(ValueError):
            sum_alternating_series(0)  # Assuming non-positive inputs raise ValueError

    def test_harmonic_sum(self):
        """Test harmonic_sum for various inputs."""
        self.assertAlmostEqual(harmonic_sum(3), 1.8333333333333333, places=10, msg="Should return 1 + 1/2 + 1/3")
        self.assertEqual(harmonic_sum(1), 1.0, "Should return 1.0")
        self.assertAlmostEqual(harmonic_sum(5), 2.283333333333333, places=10,
                               msg="Should return 1 + 1/2 + 1/3 + 1/4 + 1/5")
        self.assertAlmostEqual(harmonic_sum(2), 1.5, places=10, msg="Should return 1 + 1/2")
        with self.assertRaises(ValueError):
            harmonic_sum(0)  # Assuming non-positive inputs raise ValueError

    def test_geometric_sum(self):
        """Test geometric_sum for various inputs."""
        self.assertEqual(geometric_sum(3), 7, "Should return 7 (1+2+4)")
        self.assertEqual(geometric_sum(1), 1, "Should return 1")
        self.assertEqual(geometric_sum(5), 31, "Should return 31 (1+2+4+8+16)")
        self.assertEqual(geometric_sum(2), 3, "Should return 3 (1+2)")
        with self.assertRaises(ValueError):
            geometric_sum(0)  # Assuming non-positive inputs raise ValueError

    def test_gcd(self):
        """Test gcd for various pairs of positive integers."""
        self.assertEqual(gcd(48, 18), 6, "Should return 6")
        self.assertEqual(gcd(17, 13), 1, "Should return 1")
        self.assertEqual(gcd(100, 80), 20, "Should return 20")
        self.assertEqual(gcd(7, 7), 7, "Should return 7")
        with self.assertRaises(ValueError):
            gcd(0, 5)  # Assuming non-positive inputs raise ValueError
        with self.assertRaises(ValueError):
            gcd(5, 0)  # Assuming non-positive inputs raise ValueError

    def test_climb_stairs(self):
        """Test climb_stairs for various stair counts."""
        self.assertEqual(climb_stairs(3), 3, "Should return 3 (1+1+1, 1+2, 2+1)")
        self.assertEqual(climb_stairs(2), 2, "Should return 2 (1+1, 2)")
        self.assertEqual(climb_stairs(1), 1, "Should return 1")
        self.assertEqual(climb_stairs(0), 1, "Should return 1 (no steps)")
        self.assertEqual(climb_stairs(4), 5, "Should return 5")
        with self.assertRaises(ValueError):
            climb_stairs(-1)  # Assuming negative inputs raise ValueError

    def test_merge_sorted_lists(self):
        """Test merge_sorted_lists for various sorted list pairs."""
        self.assertEqual(merge_sorted_lists([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6], "Should merge sorted lists")
        self.assertEqual(merge_sorted_lists([1, 2, 3], []), [1, 2, 3], "Should handle empty second list")
        self.assertEqual(merge_sorted_lists([], [4, 5, 6]), [4, 5, 6], "Should handle empty first list")
        self.assertEqual(merge_sorted_lists([], []), [], "Should handle both empty lists")
        self.assertEqual(merge_sorted_lists([1], [2]), [1, 2], "Should merge single-element lists")
        self.assertEqual(merge_sorted_lists([1, 1], [1, 1]), [1, 1, 1, 1], "Should handle duplicate elements")

    def test_longest_common_prefix(self):
        """Test longest_common_prefix for various string pairs."""
        self.assertEqual(longest_common_prefix("flower", "flow"), "flow", "Should return 'flow'")
        self.assertEqual(longest_common_prefix("interspecies", "interstellar"), "inters", "Should return 'inters'")
        self.assertEqual(longest_common_prefix("dog", "cat"), "", "Should return ''")
        self.assertEqual(longest_common_prefix("", ""), "", "Should return '' for empty strings")
        self.assertEqual(longest_common_prefix("abc", ""), "", "Should return '' for one empty string")
        self.assertEqual(longest_common_prefix("xyz", "xyz"), "xyz", "Should return entire string if identical")

    def test_contains_string(self):
        """Test contains_string for various main and sub strings."""
        self.assertTrue(contains_string("hello world", "world"), "Should return True")
        self.assertFalse(contains_string("hello", "bye"), "Should return False")
        self.assertTrue(contains_string("", ""), "Should return True for empty strings")
        self.assertFalse(contains_string("abc", "abcd"), "Should return False if sub is longer")
        self.assertTrue(contains_string("abc", ""), "Should return True for empty sub")
        self.assertTrue(contains_string("hello", "ll"), "Should return True for substring in middle")
        self.assertTrue(contains_string("abc", "a"), "Should return True for single char")

    def test_count_nested_depth(self):
        """Test count_nested_depth function with various inputs."""
        self.assertEqual(count_nested_depth([1, [2, 3], [4, [5]]]), 3, "Should return 3 for nested list with depth 3")
        self.assertEqual(count_nested_depth([]), 1, "Empty list should return 1")
        self.assertEqual(count_nested_depth([1, 2, 3]), 1, "Flat list should return 1")
        self.assertEqual(count_nested_depth([[]]), 2, "List with empty list should return 2")
        self.assertEqual(count_nested_depth([1, [], [2, []]]), 3, "List with empty and nested lists should return 3")
        self.assertEqual(count_nested_depth([[[[]]]]), 4, "Deeply nested empty lists should return 4")
        self.assertEqual(count_nested_depth([[1], [2, [3]], [4]]), 3, "Multiple nested lists should return 3")
        self.assertEqual(count_nested_depth([1, [2, [3, [4]]]]), 4, "Deep nesting should return 4")
        self.assertEqual(count_nested_depth([[], [], []]), 2, "List with multiple empty lists should return 2")
        self.assertEqual(count_nested_depth([1, [[2, 3], [4]], []]), 3, "Mixed nesting should return 3")
        self.assertEqual(count_nested_depth([1, [2, 3, [4, [5]]], 6]), 4, "Complex nesting should return 4")
        self.assertEqual(count_nested_depth([[[]], [[]], []]), 3, "Nested empty lists should return 3")


    def test_interleave_strings(self):
        """Test interleave_strings function with various inputs."""
        self.assertEqual(interleave_strings("abc", "xyz", 2), "abxy", "k=2 should interleave 2 chars each")
        self.assertEqual(interleave_strings("hello", "world", 1), "hweolrllod", "k=1 should interleave 1 char each")
        self.assertEqual(interleave_strings("", "abc", 2), "abc", "Empty s1 should return s2")
        self.assertEqual(interleave_strings("abc", "", 2), "abc", "Empty s2 should return s1")
        self.assertEqual(interleave_strings("", "", 1), "", "Both empty strings should return empty")
        self.assertEqual(interleave_strings("abcdef", "xyz", 3), "abcxyz",
                         "Unequal lengths should interleave up to k")
        with self.assertRaises(ValueError):
            interleave_strings("abc", "xyz", -1)  # Negative k should raise ValueError

    def test_sum_digits_recursive(self):
        """Test sum_digits_recursive function with various inputs."""
        self.assertEqual(sum_digits_recursive(123), 6, "123 should return 1+2+3=6")
        self.assertEqual(sum_digits_recursive(0), 0, "0 should return 0")
        self.assertEqual(sum_digits_recursive(9999), 36, "9999 should return 9+9+9+9=36")
        self.assertEqual(sum_digits_recursive(1), 1, "Single digit should return itself")
        self.assertEqual(sum_digits_recursive(1000), 1, "1000 should return 1+0+0+0=1")

    def test_flatten_list(self):
        """Test flatten_list function with various inputs."""
        self.assertEqual(flatten_list([1, [2, 3], [4, [5]]]), [1, 2, 3, 4, 5], "Nested list should flatten")
        self.assertEqual(flatten_list([]), [], "Empty list should return empty list")
        self.assertEqual(flatten_list([[1], [2], [3]]), [1, 2, 3], "List of single-element lists should flatten")
        self.assertEqual(flatten_list([[]]), [], "List with empty list should return empty")
        self.assertEqual(flatten_list([[[]]]), [], "Deeply nested empty lists should return empty")
        self.assertEqual(flatten_list([1, [2, [3, [4]]], 5]), [1, 2, 3, 4, 5], "Deeply nested list should flatten")

    def test_recursive_palindrome(self):
        """Test recursive_palindrome function with various inputs."""
        self.assertTrue(recursive_palindrome("A man, a plan, a canal: Panama"), "Should be a palindrome")
        self.assertFalse(recursive_palindrome("race a car"), "Should not be a palindrome")
        self.assertTrue(recursive_palindrome(""), "Empty string should be a palindrome")
        self.assertTrue(recursive_palindrome("A"), "Single character should be a palindrome")
        self.assertTrue(recursive_palindrome("!!"), "Non-alphanumeric string should be a palindrome")
        self.assertTrue(recursive_palindrome("Was it a car or a cat I saw?"),
                        "Complex palindrome should return True")
        self.assertFalse(recursive_palindrome("hello"), "Non-palindrome should return False")


if __name__ == '__main__':
    unittest.main()
