def find_maximum_subarray_sum(arr):
    """
    Find the maximum sum of any contiguous subarray within the given array.

    @param arr: List[int] -- Array of integers
    @return: int -- Maximum sum of any contiguous subarray
    @example:
        >>> find_maximum_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        6  # The subarray [4, -1, 2, 1] has the maximum sum
        >>> find_maximum_subarray_sum([1])
        1
        >>> find_maximum_subarray_sum([-1, -2, -3, -4])
        -1  # The subarray [-1] has the maximum sum
        >>> find_maximum_subarray_sum([5, 4, -1, 7, 8])
        23  # The subarray [5, 4, -1, 7, 8] has the maximum sum
    """
    pass

def rotate_array(arr, k):
    """
    Rotate the array to the right by k steps.

    @param arr: List[int] -- Array of integers
    @param k: int -- Number of steps to rotate
    @return: List[int] -- Rotated array
    @example:
        >>> rotate_array([1, 2, 3, 4, 5], 2)
        [4, 5, 1, 2, 3]
        >>> rotate_array([1, 2, 3], 0)
        [1, 2, 3]
        >>> rotate_array([1, 2, 3, 4], 4)
        [1, 2, 3, 4]  # Rotating by array length returns original array
        >>> rotate_array([1], 3)
        [1]  # Single element array remains unchanged
    """
    pass

def find_missing_number(arr, n):
    """
    Find the missing number in an array containing n-1 numbers from 1 to n.

    @param arr: List[int] -- Array of n-1 integers
    @param n: int -- Range of numbers (1 to n)
    @return: int -- Missing number
    @example:
        >>> find_missing_number([1, 2, 4, 6, 3, 7, 8], 8)
        5
        >>> find_missing_number([1], 2)
        2
        >>> find_missing_number([2, 3, 4, 1], 5)
        5
        >>> find_missing_number([1, 2, 3], 4)
        4
    """
    pass

def merge_sorted_arrays(arr1, arr2):
    """
    Merge two sorted arrays into a single sorted array.

    @param arr1: List[int] -- First sorted array
    @param arr2: List[int] -- Second sorted array
    @return: List[int] -- Merged sorted array
    @example:
        >>> merge_sorted_arrays([1, 3, 5], [2, 4, 6])
        [1, 2, 3, 4, 5, 6]
        >>> merge_sorted_arrays([1, 2], [])
        [1, 2]
        >>> merge_sorted_arrays([], [1, 2, 3])
        [1, 2, 3]
        >>> merge_sorted_arrays([1, 1, 1], [2, 2, 2])
        [1, 1, 1, 2, 2, 2]
    """
    pass

def find_duplicate_number(arr):
    """
    Find the duplicate number in an array containing n+1 integers between 1 and n.

    @param arr: List[int] -- Array with one duplicate
    @return: int -- Duplicate number
    @example:
        >>> find_duplicate_number([1, 3, 4, 2, 2])
        2
        >>> find_duplicate_number([3, 1, 3, 4, 2])
        3
        >>> find_duplicate_number([1, 1, 2, 3])
        1
        >>> find_duplicate_number([4, 2, 1, 3, 2])
        2
    """
    pass

def move_zeros_to_end(arr):
    """
    Move all zeros to the end of the array while maintaining the relative order of non-zero elements.

    @param arr: List[int] -- Array of integers
    @return: List[int] -- Array with zeros at the end
    @example:
        >>> move_zeros_to_end([0, 1, 0, 3, 12])
        [1, 3, 12, 0, 0]
        >>> move_zeros_to_end([1, 2, 3])
        [1, 2, 3]
        >>> move_zeros_to_end([0, 0, 0, 1])
        [1, 0, 0, 0]
        >>> move_zeros_to_end([1, 0, 0, 2, 0, 3])
        [1, 2, 3, 0, 0, 0]
    """
    pass

def find_first_unique_element(arr):
    """
    Find the first non-repeating element in the array.

    @param arr: List[int] -- Array of integers
    @return: int -- First non-repeating element, or None if none exists
    @example:
        >>> find_first_unique_element([7, 3, 5, 3, 5, 7, 4])
        4
        >>> find_first_unique_element([1, 1, 2, 2])
        None
        >>> find_first_unique_element([1, 2, 3, 4])
        1
        >>> find_first_unique_element([2, 2, 3, 3, 1])
        1
    """
    pass

def find_kth_largest(arr, k):
    """
    Find the kth largest element in an unsorted array.

    @param arr: List[int] -- Array of integers
    @param k: int -- Position of the largest element (1-based)
    @return: int -- kth largest element
    @example:
        >>> find_kth_largest([3, 2, 1, 5, 6, 4], 2)
        5
        >>> find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
        4
        >>> find_kth_largest([1], 1)
        1
        >>> find_kth_largest([7, 4, 6, 3, 9, 1], 3)
        6
    """
    pass

def product_except_self(arr):
    """
    Return an array where each element is the product of all other elements.

    @param arr: List[int] -- Array of integers
    @return: List[int] -- Array of products
    @example:
        >>> product_except_self([1, 2, 3, 4])
        [24, 12, 8, 6]
        >>> product_except_self([2, 3])
        [3, 2]
        >>> product_except_self([1, 1, 1, 1])
        [1, 1, 1, 1]
        >>> product_except_self([2, 3, 0, 4])
        [0, 0, 24, 0]
    """
    pass

def find_longest_consecutive_sequence(arr):
    """
    Find the length of the longest consecutive sequence in an unsorted array.

    @param arr: List[int] -- Array of integers
    @return: int -- Length of the longest consecutive sequence
    @example:
        >>> find_longest_consecutive_sequence([100, 4, 200, 1, 3, 2])
        4  # The longest consecutive sequence is [1, 2, 3, 4]
        >>> find_longest_consecutive_sequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
        9
        >>> find_longest_consecutive_sequence([1, 2, 0, 1])
        3  # The longest consecutive sequence is [0, 1, 2]
        >>> find_longest_consecutive_sequence([])
        0
    """
    pass