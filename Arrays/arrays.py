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
    sorted_array = sorted(arr)
    zeros_index = 0
    for i in range(len(sorted_array)):
        if sorted_array[i] == 0:
            zeros_index += 1
    zeros_array = sorted_array[:zeros_index]
    arr = sorted_array[zeros_index:] + zeros_array
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
    return list(set(arr))

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
    if len(arr) <= shift:
        return [0] * len(arr)
    index = 0
    while shift > 0:
        arr[index] = arr[len(arr)-shift]
        arr[len(arr)-shift] = 0
        shift -= 1
        index += 1
    return arr

def group_by_sum(arr, target_sum):
    """
    Group array elements into subarrays where each subarray sums to target_sum.

    @param arr: List[int] -- Array of integers
    @param target_sum: int -- Target sum for each subarray
    @return: List[List[int]] -- List of subarrays summing to target_sum, or empty list if not possible
    @example:
        >>> group_by_sum([1, 2, 3, 4, 5], 5)
        [[1, 4], [2, 3], [5]]
        >>> group_by_sum([1, 2, 3], 10)
        []
        >>> group_by_sum([], 5)
        []
    """
    sum_list = []
    for i in range(len(arr)):
        current_element = arr[i]
        for j in range(len(arr)):
            if j != i:
                next_element = arr[j]
                if current_element + next_element == target_sum:
                    if (not [current_element, next_element] in sum_list and
                            not [next_element, current_element] in sum_list):
                        sum_list.append([current_element, next_element])
        if current_element == target_sum:
            sum_list.append([target_sum])
    return sum_list

def split_array_equal_sums(arr):
    """
    Split the array into two parts with equal sums.

    @param arr: List[int] -- Array of integers
    @return: int -- Index where array can be split, or -1 if not possible
    @example:
        >>> split_array_equal_sums([1, 2, 3, 4, 5, 5])
        4  # Split at index 4: [1, 2, 3, 4] and [5, 5], both sum to 10
        >>> split_array_equal_sums([1, 2, 3])
        2  # Split at index 2: [1, 2] and [3], both sum to 3
        >>> split_array_equal_sums([])
        -1  # No split possible
        >>> split_array_equal_sums([2, 3, 5, 0])
        2  # Split at index 2: [2, 3] and [5, 0], both sum to 5
        >>> split_array_equal_sums([1, -1, 1, -1])
        2  # Split at index 2: [1, -1] and [1, -1], both sum to 0
        >>> split_array_equal_sums([0, 0, 0])
        1  # Split at index 1: [0] and [0, 0], both sum to 0
        >>> split_array_equal_sums([10, 20, 30])
        2  # Split at index 2: [10, 20] and [30], both sum to 30
        >>> split_array_equal_sums([1, 2, 3, 4])
        -1  # No split possible
        >>> split_array_equal_sums([5, 5, 5, 5, 5, 5])
        3  # Split at index 3: [5, 5, 5] and [5, 5, 5], both sum to 15
    """
    arr_a = arr[:len(arr)//2]
    arr_b = arr[len(arr)//2:]
    difference = (sum(arr_a) - sum(arr_b))//2
    if difference < 0:
        if abs(difference) in arr_b:
            return len(arr_a) + 1
    elif difference > 0:
        if difference in arr_a:
            return len(arr_b) + 1
    elif difference == 0:
        return len(arr)//2
    return -1

def max_product_pair(arr):
    """
    Find the pair of elements with the maximum product.

    @param arr: List[int] -- Array of integers
    @return: tuple[int, int] -- Pair of integers with maximum product, or None if array has less than 2 elements
    @example:
        >>> max_product_pair([1, 2, 3, 4])
        (3, 4)  # 3 * 4 = 12
        >>> max_product_pair([-4, -3, 0, 2])
        (-4, -3)  # -4 * -3 = 12
        >>> max_product_pair([1])
        None  # Fewer than 2 elements
        >>> max_product_pair([5, -2, 3, -4])
        (5, 3)  # 5 * 3 = 15
        >>> max_product_pair([0, 0, 0, 0])
        (0, 0)  # 0 * 0 = 0
        >>> max_product_pair([-5, -5, -5])
        (-5, -5)  # -5 * -5 = 25
        >>> max_product_pair([1, 2])
        (1, 2)  # 1 * 2 = 2
        >>> max_product_pair([-10, 2, 3, 4, -2])
        (-10, -2)  # -10 * -2 = 20
        >>> max_product_pair([])
        None  # No elements
    """
    if len(arr) <= 1:
        return None

    product_dict = {}
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i] * arr[j] not in product_dict:
                product_dict[arr[i] * arr[j]] = (arr[i], arr[j])
    return product_dict[max(list(product_dict.keys()))]


def find_common_elements(arr1, arr2):
    """
    Find common elements between two arrays, preserving the order of first array.

    @param arr1: List[int] -- First array of integers
    @param arr2: List[int] -- Second array of integers
    @return: List[int] -- List of common elements in order of arr1
    @example:
        >>> find_common_elements([1, 2, 3, 4], [2, 4, 6])
        [2, 4]
        >>> find_common_elements([1, 2], [3, 4])
        []
        >>> find_common_elements([], [1, 2])
        []
    """
    a = set(arr1)
    b = set(arr2)
    if len(a) > len(b):
        return list(a.intersection(b))
    return list(b.intersection(a))

def rotate_left_by_one(arr):
    """
    Rotate the array left by one position.

    @param arr: List[int] -- Array of integers
    @return: List[int] -- Array rotated left by one position
    @example:
        >>> rotate_left_by_one([1, 2, 3, 4])
        [2, 3, 4, 1]
        >>> rotate_left_by_one([1])
        [1]
        >>> rotate_left_by_one([])
        []
    """
    first = arr[0]
    arr[0] = arr[len(arr)-1]
    arr[len(arr)-1] = first
    return arr

def find_pairs_with_sum(arr, target):
    """
    Find all pairs of elements that sum to the target value.

    @param arr: List[int] -- Array of integers
    @param target: int -- Target sum
    @return: List[tuple[int, int]] -- List of pairs (i, j) where i + j = target
    @example:
        >>> find_pairs_with_sum([1, 2, 3, 4], 5)
        [(1, 4), (2, 3)]
        >>> find_pairs_with_sum([1, 2, 3], 10)
        []
        >>> find_pairs_with_sum([2, 2, 2], 4)
        [(2, 2)]
    """
    if sum(arr) < target:
        return []

    sum_list = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and ((arr[i], arr[j]) and (arr[j], arr[i]) not in sum_list) and (arr[i] + arr[j] == target):
                sum_list.append((arr[i], arr[j]))
    return sum_list

def segregate_pos_neg(arr):
    """
    Segregate positive and negative numbers, maintaining relative order within each group.

    @param arr: List[int] -- Array of integers
    @return: List[int] -- Array with positives followed by negatives
    @example:
        >>> segregate_pos_neg([-1, 2, -3, 4, -5])
        [2, 4, -1, -3, -5]
        >>> segregate_pos_neg([1, 2, 3])
        [1, 2, 3]
        >>> segregate_pos_neg([-1, -2, -3])
        [-1, -2, -3]
        >>> segregate_pos_neg([])
        []
        >>> segregate_pos_neg([0, 1, -1, 0])
        [0, 1, 0, -1]
        >>> segregate_pos_neg([2, 2, -2, -2])
        [2, 2, -2, -2]
        >>> segregate_pos_neg([5])
        [5]
        >>> segregate_pos_neg([-5])
        [-5]
        >>> segregate_pos_neg([0, 0, 0])
        [0, 0, 0]
        >>> segregate_pos_neg([1, -1, 1, -1])
        [1, 1, -1, -1]
        >>> segregate_pos_neg([10, -10, 20, -20, 0])
        [10, 20, 0, -10, -20]
    """
    # TODO

def find_subarray_with_sum(arr, target_sum):
    """
    Find the first subarray with the given sum.

    @param arr: List[int] -- Array of integers
    @param target_sum: int -- Target sum
    @return: tuple[int, int] -- Start and end indices of subarray, or (-1, -1) if not found
    @example:
        >>> find_subarray_with_sum([1, 2, 3, 4], 5)
        (0, 1)  # Subarray [1, 2]
        >>> find_subarray_with_sum([1, 2, 3], 10)
        (-1, -1)
        >>> find_subarray_with_sum([], 0)
        (-1, -1)
    """
    # TODO

def alternate_elements(arr):
    """
    Create a new array with elements in alternate positions (0, 2, 4, ...).

    @param arr: List[int] -- Array of integers
    @return: List[int] -- Array with elements from even indices
    @example:
        >>> alternate_elements([1, 2, 3, 4, 5])
        [1, 3, 5]
        >>> alternate_elements([1])
        [1]
        >>> alternate_elements([])
        []
    """
    # TODO

def count_frequency(arr):
    """
    Count the frequency of each element in the array.

    @param arr: List[int] -- Array of integers
    @return: dict[int, int] -- Dictionary with elements as keys and their frequencies as values
    @example:
        >>> count_frequency([1, 2, 2, 3, 1])
        {1: 2, 2: 2, 3: 1}
        >>> count_frequency([])
        {}
        >>> count_frequency([1, 1, 1])
        {1: 3}
    """
    # TODO

def find_subarray_product(arr, target_product):
    """
    Find the first subarray with the given product.

    @param arr: List[int] -- Array of integers
    @param target_product: int -- Target product
    @return: tuple[int, int] -- Start and end indices of subarray, or (-1, -1) if not found
    @example:
        >>> find_subarray_product([2, 3, 4, 2], 6)
        (0, 1)  # Subarray [2, 3]
        >>> find_subarray_product([1, 2, 3], 10)
        (-1, -1)
        >>> find_subarray_product([], 1)
        (-1, -1)
    """
    # TODO

def merge_alternate(arr1, arr2):
    """
    Merge two arrays by alternating their elements.

    @param arr1: List[int] -- First array of integers
    @param arr2: List[int] -- Second array of integers
    @return: List[int] -- Array with alternating elements from arr1 and arr2
    @example:
        >>> merge_alternate([1, 3, 5], [2, 4, 6])
        [1, 2, 3, 4, 5, 6]
        >>> merge_alternate([1], [2])
        [1, 2]
        >>> merge_alternate([], [1, 2])
        [1, 2]
    """
    # TODO

def find_min_max_difference(arr):
    """
    Find the difference between the maximum and minimum elements in the array.

    @param arr: List[int] -- Array of integers
    @return: int -- Difference between max and min, or 0 if array is empty
    @example:
        >>> find_min_max_difference([3, 1, 4, 2])
        3  # Max 4 - Min 1 = 3
        >>> find_min_max_difference([5])
        0
        >>> find_min_max_difference([])
        0
    """
    # TODO

def partition_array(arr, pivot):
    """
    Partition the array around a pivot value, placing smaller elements before and larger after.

    @param arr: List[int] -- Array of integers
    @param pivot: int -- Pivot value
    @return: List[int] -- Array with elements < pivot, then pivot, then elements > pivot
    @example:
        >>> partition_array([3, 1, 4, 2, 3], 3)
        [1, 2, 3, 3, 4]
        >>> partition_array([1, 2], 5)
        [1, 2]
        >>> partition_array([], 0)
        []
    """
    # TODO

def find_unique_elements(arr1, arr2):
    """
    Find elements that are unique to each array (not present in the other).

    @param arr1: List[int] -- First array of integers
    @param arr2: List[int] -- Second array of integers
    @return: List[int] -- List of elements unique to either array
    @example:
        >>> find_unique_elements([1, 2, 3], [2, 3, 4])
        [1, 4]
        >>> find_unique_elements([1, 1], [2, 2])
        [1, 2]
        >>> find_unique_elements([], [1])
        [1]
    """
    # TODO

def sum_pairs_to_target(arr, target):
    """
    Sum all elements in pairs that add up to the target value.

    @param arr: List[int] -- Array of integers
    @param target: int -- Target sum for pairs
    @return: int -- Sum of all elements in valid pairs
    @example:
        >>> sum_pairs_to_target([1, 2, 3, 4], 5)
        10  # Pairs (1, 4) and (2, 3) -> 1 + 4 + 2 + 3 = 10
        >>> sum_pairs_to_target([1, 2, 3], 10)
        0
        >>> sum_pairs_to_target([2, 2], 4)
        4  # Pair (2, 2) -> 2 + 2 = 4
    """
    # TODO

def swap_elements(arr, k):
    """
    Swap every k-th element with the element k positions ahead, if possible.

    @param arr: List[int] -- Array of integers
    @param k: int -- Distance for swapping
    @return: List[int] -- Array after swapping elements
    @example:
        >>> swap_elements([1, 2, 3, 4, 5], 2)
        [3, 2, 1, 4, 5]  # Swap 1 with 3
        >>> swap_elements([1, 2, 3], 5)
        [1, 2, 3]  # No swap possible
        >>> swap_elements([], 1)
        []
    """
    # TODO

def count_subarrays_with_sum(arr, target_sum):
    """
    Count the number of subarrays with the given sum.

    @param arr: List[int] -- Array of integers
    @param target_sum: int -- Target sum
    @return: int -- Number of subarrays with target sum
    @example:
        >>> count_subarrays_with_sum([1, 2, 3, -2], 3)
        2  # Subarrays [1, 2] and [3]
        >>> count_subarrays_with_sum([1, 2, 3], 10)
        0
        >>> count_subarrays_with_sum([], 0)
        0
    """
    # TODO

def interleave_arrays(arr1, arr2):
    """
    Interleave two arrays, taking elements alternately until one is exhausted, then append the rest.

    @param arr1: List[int] -- First array of integers
    @param arr2: List[int] -- Second array of integers
    @return: List[int] -- Interleaved array
    @example:
        >>> interleave_arrays([1, 3, 5], [2, 4])
        [1, 2, 3, 4, 5]
        >>> interleave_arrays([1], [2, 3, 4])
        [1, 2, 3, 4]
        >>> interleave_arrays([], [])
        []
    """
    if len(arr1) == 0 or len(arr2) == 0:
        return arr2 if len(arr1) == 0 else arr1
    interleaved_array = [arr1[0]] + [arr2[0]]
    return interleaved_array + interleave_arrays(arr1[1:], arr2[1:])

def find_most_frequent(arr):
    """
    Find the most frequent element in the array.

    @param arr: List[int] -- Array of integers
    @return: int -- Most frequent element, or None if array is empty
    @example:
        >>> find_most_frequent([1, 2, 2, 3, 1])
        1  # 1 and 2 appear twice, 1 is first
        >>> find_most_frequent([1])
        1
        >>> find_most_frequent([])
        None
        >>> find_most_frequent([2, 2, 2, 3])
        2  # 2 appears three times
        >>> find_most_frequent([-1, -1, 0, 0])
        -1  # -1 and 0 appear twice, -1 is first
        >>> find_most_frequent([1, 1, 1, 1])
        1  # 1 appears four times
        >>> find_most_frequent([0, 1, 0, 1])
        0  # 0 and 1 appear twice, 0 is first
        >>> find_most_frequent([-2, -2, -3, -2, -3])
        -2  # -2 appears three times
    """
    if not arr:
        return None
    element = 0
    num_appearances = 0
    for i in range(len(arr)):
        count = arr.count(arr[i])
        if num_appearances < count:
            num_appearances = count
            element = arr[i]
    return element

if __name__ == "__main__":
    print(count_subarrays_with_sum([1, 2, 3, -2], 3))