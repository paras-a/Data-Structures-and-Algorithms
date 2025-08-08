from gc import get_threshold


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
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]
    max_sum = arr[0]
    rolling_sum = 0
    for i in range(len(arr)):
        rolling_sum += arr[i]
        max_sum = max(rolling_sum, max_sum)
    next_sum = find_maximum_subarray_sum(arr[1:])
    max_sum = max(next_sum, max_sum)
    return max_sum


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
    if len(arr) < k or k == 0:
        return arr
    return arr[-k:] + arr[:len(arr)-k]


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
    missing = 0
    for i in range(n):
        if i + 1 not in arr:
            missing = i + 1
    return missing


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
    if not arr1 and not arr2:
        return arr1
    if not arr1 and arr2:
        return arr2
    if not arr2 and arr1:
        return arr1
    merged = []
    if arr1[0] < arr2[0]:
        merged.append(arr1[0])
        return merged + merge_sorted_arrays(arr1[1:], arr2)
    elif arr1[0] == arr2[0]:
        merged.append(arr1[0])
        merged.append(arr2[0])
        return merged + merge_sorted_arrays(arr1[1:], arr2[1:])
    else:
        merged.append(arr2[0])
        return merged + merge_sorted_arrays(arr1, arr2[1:])


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
    if not arr:
        return 0
    duplicate = 0
    for i in range(len(arr)):
        current_number = arr[i]
        for j in range(len(arr)):
            next_number = arr[j]
            if i != j and current_number == next_number:
                duplicate = current_number
    return duplicate


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
    for i in range(len(arr)):
        if arr[i] == 0:
            arr.pop(i)
            arr.append(0)
    return arr


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
    if len(arr) == 0:
        return None
    duplicate = []
    for i in range(len(arr)):
        current_element = arr[i]
        for j in range(len(arr)):
            next_element = arr[j]
            if i != j and current_element == next_element:
                duplicate.append(current_element)
    if len(duplicate) == 0:
        return arr[0]
    unique = set(arr).difference(set(duplicate))
    if len(unique) > 0:
        return unique.pop()
    return None


def find_kth_largest(arr, k):
    """
    Find the kth largest element in an unsorted array.

    @param arr: List[int] -- Array of integers
    @param k: int -- Position of the largest element (1-based)
    @return: int -- kth largest element
    @example:
        >>> find_kth_largest([3, 2, 1, 5, 6, 4], 2)
        5  # Second largest element in [6, 5, 4, 3, 2, 1]
        >>> find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
        4  # Fourth largest element in [6, 5, 5, 4, 3, 3, 2, 2, 1]
        >>> find_kth_largest([1], 1)
        1  # First largest element in [1]
        >>> find_kth_largest([7, 4, 6, 3, 9, 1], 3)
        6  # Third largest element in [9, 7, 6, 4, 3, 1]
        >>> find_kth_largest([10, -1, 2, 5, 0, 8], 1)
        10  # First largest element in [10, 8, 5, 2, 0, -1]
        >>> find_kth_largest([3, 3, 3, 3], 2)
        3  # Second largest element in [3, 3, 3, 3]
        >>> find_kth_largest([-5, -2, -10, -1, -3], 3)
        -3  # Third largest element in [-1, -2, -3, -5, -10]
        >>> find_kth_largest([1, 2, 3, 4, 5], 5)
        1  # Fifth largest element in [5, 4, 3, 2, 1]
        >>> find_kth_largest([8, 8, 7, 7, 6, 6], 4)
        7  # Fourth largest element in [8, 8, 7, 7, 6, 6]
        >>> find_kth_largest([100, 50, 25, 75, 10], 2)
        75  # Second largest element in [100, 75, 50, 25, 10]
    """
    return sorted(arr)[len(arr)-k]


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
    product_list = []
    for i in range(len(arr)):
        product = 1
        for j in range(len(arr)):
            if i != j:
                product *= arr[j]
        product_list.append(product)
    return product_list


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
    if not arr:
        return 0
    sorted_arr_set = set(arr)
    sorted_arr_set_list = sorted(list(sorted_arr_set))
    sequence_count = 1
    for i in range(len(sorted_arr_set_list)-1):
        if sorted_arr_set_list[i+1] - sorted_arr_set_list[i] == 1:
            sequence_count += 1
    return sequence_count


def sum_array(arr):
    """
    Calculate the sum of all elements in the array.

    @param arr: List[int] -- Array of integers
    @return: int -- Sum of all elements
    @example:
        >>> sum_array([1, 2, 3, 4])
        10
        >>> sum_array([])
        0
        >>> sum_array([-1, 1])
        0
    """
    return sum(arr)

def count_evens(arr):
    """
    Count the number of even elements in the array.

    @param arr: List[int] -- Array of integers
    @return: int -- Number of even elements
    @example:
        >>> count_evens([2, 4, 1, 6, 3])
        3
        >>> count_evens([1, 3, 5])
        0
        >>> count_evens([])
        0
    """
    evens = 0
    for element in arr:
        if element % 2 == 0:
            evens += 1
    return evens

def reverse_array(arr):
    """
    Reverse the elements of the array.

    @param arr: List[int] -- Array of integers
    @return: List[int] -- Reversed array
    @example:
        >>> reverse_array([1, 2, 3, 4])
        [4, 3, 2, 1]
        >>> reverse_array([1])
        [1]
        >>> reverse_array([])
        []
    """
    # can also use the inbuilt method to reverse the array but this is more fun!
    head_index = 0
    tail_index = len(arr) - 1
    while tail_index > head_index:
        current_element = arr[head_index]
        arr[head_index] = arr[tail_index]
        arr[tail_index] = current_element
        tail_index -= 1
        head_index += 1
    return arr

def find_max_element(arr):
    """
    Find the maximum element in the array.

    @param arr: List[int] -- Array of integers
    @return: int -- Maximum element, or None if array is empty
    @example:
        >>> find_max_element([3, 5, 1, 4, 2])
        5
        >>> find_max_element([1])
        1
        >>> find_max_element([])
        None
    """
    # can also use the max method to get the maximum element but this is more fun!
    if not arr:
        return None
    max_element = arr[0]
    for element in arr:
        if element > max_element:
            max_element = element
    return max_element

def replace_negatives(arr):
    """
    Replace all negative elements in the array with 0.

    @param arr: List[int] -- Array of integers
    @return: List[int] -- Array with negative elements replaced by 0
    @example:
        >>> replace_negatives([-1, 2, -3, 4])
        [0, 2, 0, 4]
        >>> replace_negatives([1, 2, 3])
        [1, 2, 3]
        >>> replace_negatives([-1, -2])
        [0, 0]
    """
    for i in range(len(arr)):
        arr[i] = 0 if arr[i] < 0 else arr[i]
    return arr

def find_element_index(arr, target):
    """
    Find the index of the first occurrence of the target element.

    @param arr: List[int] -- Array of integers
    @param target: int -- Element to find
    @return: int -- Index of first occurrence, or -1 if not found
    @example:
        >>> find_element_index([1, 2, 3, 2], 2)
        1
        >>> find_element_index([1, 3, 4], 5)
        -1
        >>> find_element_index([], 1)
        -1
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def filter_greater_than(arr, threshold):
    """
    Return a new array containing elements greater than the threshold.

    @param arr: List[int] -- Array of integers
    @param threshold: int -- Threshold value
    @return: List[int] -- Array with elements greater than threshold
    @example:
        >>> filter_greater_than([1, 5, 2, 6, 3], 3)
        [5, 6]
        >>> filter_greater_than([1, 2, 3], 5)
        []
        >>> filter_greater_than([], 0)
        []
    """
    greater_than_list = []
    for i in range(len(arr)):
        if arr[i] > threshold:
            greater_than_list.append(arr[i])
    return greater_than_list

def multiply_array(arr, factor):
    """
    Multiply each element in the array by a given factor.

    @param arr: List[int] -- Array of integers
    @param factor: int -- Factor to multiply by
    @return: List[int] -- Array with elements multiplied by factor
    @example:
        >>> multiply_array([1, 2, 3], 2)
        [2, 4, 6]
        >>> multiply_array([0, 1, -2], 3)
        [0, 3, -6]
        >>> multiply_array([], 5)
        []
    """
    if not arr:
        return []
    return [arr[0] * factor] + multiply_array(arr[1:], factor)

def remove_duplicates(arr):
    """
    Remove duplicate elements from the array, keeping the first occurrence.

    @param arr: List[int] -- Array of integers
    @return: List[int] -- Array with duplicates removed
    @example:
        >>> remove_duplicates([1, 2, 2, 3, 1])
        [1, 2, 3]
        >>> remove_duplicates([1, 1, 1])
        [1]
        >>> remove_duplicates([])
        []
    """
    # TODO

def shift_elements(arr, shift):
    """
    Shift all elements in the array to the left by the given shift amount, filling with 0.

    @param arr: List[int] -- Array of integers
    @param shift: int -- Number of positions to shift left
    @return: List[int] -- Array after shifting
    @example:
        >>> shift_elements([1, 2, 3, 4], 2)
        [3, 4, 0, 0]
        >>> shift_elements([1, 2, 3], 0)
        [1, 2, 3]
        >>> shift_elements([1], 5)
        [0]
    """
    # TODO

if __name__ == "__main__":
    print(multiply_array([0, 1, -2], 3))