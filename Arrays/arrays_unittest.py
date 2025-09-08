import unittest

from arrays import *


class TestArrayProblems(unittest.TestCase):
    def test_find_maximum_subarray_sum(self):
        """Test find_maximum_subarray_sum function."""
        self.assertEqual(
            find_maximum_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6,
            msg="Failed to find maximum subarray sum for [-2, 1, -3, 4, -1, 2, 1, -5, 4], expected 6"
        )
        self.assertEqual(
            find_maximum_subarray_sum([1]), 1,
            msg="Failed for single-element array [1], expected 1"
        )
        self.assertEqual(
            find_maximum_subarray_sum([-1, -2, -3, -4]), -1,
            msg="Failed for all-negative array [-1, -2, -3, -4], expected -1"
        )
        self.assertEqual(
            find_maximum_subarray_sum([5, 4, -1, 7, 8]), 23,
            msg="Failed for array [5, 4, -1, 7, 8], expected 23"
        )
        self.assertEqual(
            find_maximum_subarray_sum([]), None,
            msg="Failed for empty array, expected None"
        )
        self.assertEqual(
            find_maximum_subarray_sum([0, 0, 0]), 0,
            msg="Failed for all-zero array [0, 0, 0], expected 0"
        )
        self.assertEqual(
            find_maximum_subarray_sum([2, -3, 4, -2, 5, -1]), 7,
            msg="Failed for [2, -3, 4, -2, 5, -1], expected 7"
        )
        self.assertEqual(
            find_maximum_subarray_sum([-5]), -5,
            msg="Failed for single negative array [-5], expected -5"
        )

    def test_rotate_array(self):
        """Test rotate_array function."""
        self.assertEqual(
            rotate_array([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3],
            msg="Failed to rotate [1, 2, 3, 4, 5] by 2 steps, expected [4, 5, 1, 2, 3]"
        )
        self.assertEqual(
            rotate_array([1, 2, 3], 0), [1, 2, 3],
            msg="Failed for zero rotation of [1, 2, 3], expected [1, 2, 3]"
        )
        self.assertEqual(
            rotate_array([1, 2, 3, 4], 4), [1, 2, 3, 4],
            msg="Failed for full rotation of [1, 2, 3, 4] by 4, expected [1, 2, 3, 4]"
        )
        self.assertEqual(
            rotate_array([1], 3), [1],
            msg="Failed for single-element array [1] with k=3, expected [1]"
        )
        self.assertEqual(
            rotate_array([], 5), [],
            msg="Failed for empty array with k=5, expected []"
        )
        self.assertEqual(
            rotate_array([-1, -2, -3], 1), [-2, -3, -1],
            msg="Failed for [-1, -2, -3] with k=1, expected [-2, -3, -1]"
        )
        self.assertEqual(
            rotate_array([1, 2, 3, 4], 6), [3, 4, 1, 2],
            msg="Failed for [1, 2, 3, 4] with k=6, expected [3, 4, 1, 2]"
        )
        self.assertEqual(
            rotate_array([2, 2, 2], 2), [2, 2, 2],
            msg="Failed for [2, 2, 2] with k=2, expected [2, 2, 2]"
        )

    def test_find_missing_number(self):
        """Test find_missing_number function."""
        self.assertEqual(
            find_missing_number([1, 2, 4, 6, 3, 7, 8], 8), 5,
            msg="Failed to find missing number in [1, 2, 4, 6, 3, 7, 8] with n=8, expected 5"
        )
        self.assertEqual(
            find_missing_number([1], 2), 2,
            msg="Failed for array [1] with n=2, expected 2"
        )
        self.assertEqual(
            find_missing_number([2, 3, 4, 1], 5), 5,
            msg="Failed for array [2, 3, 4, 1] with n=5, expected 5"
        )
        self.assertEqual(
            find_missing_number([1, 2, 3], 4), 4,
            msg="Failed for array [1, 2, 3] with n=4, expected 4"
        )
        self.assertEqual(
            find_missing_number([], 1), 1,
            msg="Failed for empty array with n=1, expected 1"
        )
        self.assertEqual(
            find_missing_number([1, 2, 3], 3), None,
            msg="Failed for [1, 2, 3] with n=3, expected None"
        )
        self.assertEqual(
            find_missing_number([1, -1, 2], 4), -2,
            msg="Failed for [1, -1, 2] with n=4, expected -2"
        )
        self.assertEqual(
            find_missing_number([1, 3, 5], 6), 2,
            msg="Failed for [1, 3, 5] with n=6, expected 2"
        )

    def test_merge_sorted_arrays(self):
        """Test merge_sorted_arrays function."""
        self.assertEqual(
            merge_sorted_arrays([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6],
            msg="Failed to merge [1, 3, 5] and [2, 4, 6], expected [1, 2, 3, 4, 5, 6]"
        )
        self.assertEqual(
            merge_sorted_arrays([1, 2], []), [1, 2],
            msg="Failed to merge [1, 2] with empty array, expected [1, 2]"
        )
        self.assertEqual(
            merge_sorted_arrays([], [1, 2, 3]), [1, 2, 3],
            msg="Failed to merge empty array with [1, 2, 3], expected [1, 2, 3]"
        )
        self.assertEqual(
            merge_sorted_arrays([1, 1, 1], [2, 2, 2]), [1, 1, 1, 2, 2, 2],
            msg="Failed to merge [1, 1, 1] and [2, 2, 2], expected [1, 1, 1, 2, 2, 2]"
        )
        self.assertEqual(
            merge_sorted_arrays([], []), [],
            msg="Failed to merge two empty arrays, expected []"
        )
        self.assertEqual(
            merge_sorted_arrays([1, 2, 3], [4]), [1, 2, 3, 4],
            msg="Failed to merge [1, 2, 3] and [4], expected [1, 2, 3, 4]"
        )
        self.assertEqual(
            merge_sorted_arrays([-2, -1], [-3, 0]), [-3, -2, -1, 0],
            msg="Failed to merge [-2, -1] and [-3, 0], expected [-3, -2, -1, 0]"
        )
        self.assertEqual(
            merge_sorted_arrays([1, 2, 2], [2, 3]), [1, 2, 2, 2, 3],
            msg="Failed to merge [1, 2, 2] and [2, 3], expected [1, 2, 2, 2, 3]"
        )

    def test_find_duplicate_number(self):
        """Test find_duplicate_number function."""
        self.assertEqual(
            find_duplicate_number([1, 3, 4, 2, 2]), 2,
            msg="Failed to find duplicate in [1, 3, 4, 2, 2], expected 2"
        )
        self.assertEqual(
            find_duplicate_number([3, 1, 3, 4, 2]), 3,
            msg="Failed to find duplicate in [3, 1, 3, 4, 2], expected 3"
        )
        self.assertEqual(
            find_duplicate_number([1, 1, 2, 3]), 1,
            msg="Failed to find duplicate in [1, 1, 2, 3], expected 1"
        )
        self.assertEqual(
            find_duplicate_number([4, 2, 1, 3, 2]), 2,
            msg="Failed to find duplicate in [4, 2, 1, 3, 2], expected 2"
        )
        self.assertEqual(
            find_duplicate_number([1, 1]), 1,
            msg="Failed for minimal array [1, 1], expected 1"
        )
        self.assertEqual(
            find_duplicate_number([1, 2, 2, 2, 3]), 2,
            msg="Failed for [1, 2, 2, 2, 3], expected 2"
        )
        self.assertEqual(
            find_duplicate_number([-1, -1, 2, 3]), -1,
            msg="Failed for [-1, -1, 2, 3], expected -1"
        )
        self.assertEqual(
            find_duplicate_number([5, 3, 1, 4, 3, 2, 6]), 3,
            msg="Failed for [5, 3, 1, 4, 3, 2, 6], expected 3"
        )

    def test_move_zeros_to_end(self):
        """Test move_zeros_to_end function."""
        self.assertEqual(
            move_zeros_to_end([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0],
            msg="Failed to move zeros in [0, 1, 0, 3, 12], expected [1, 3, 12, 0, 0]"
        )
        self.assertEqual(
            move_zeros_to_end([1, 2, 3]), [1, 2, 3],
            msg="Failed for array [1, 2, 3] with no zeros, expected [1, 2, 3]"
        )
        self.assertEqual(
            move_zeros_to_end([0, 0, 0, 1]), [1, 0, 0, 0],
            msg="Failed for array [0, 0, 0, 1], expected [1, 0, 0, 0]"
        )
        self.assertEqual(
            move_zeros_to_end([1, 0, 0, 2, 0, 3]), [1, 2, 3, 0, 0, 0],
            msg="Failed for array [1, 0, 0, 2, 0, 3], expected [1, 2, 3, 0, 0, 0]"
        )
        self.assertEqual(
            move_zeros_to_end([]), [],
            msg="Failed for empty array, expected []"
        )
        self.assertEqual(
            move_zeros_to_end([0, 0, 0]), [0, 0, 0],
            msg="Failed for [0, 0, 0], expected [0, 0, 0]"
        )
        self.assertEqual(
            move_zeros_to_end([-1, 0, -2, 0]), [-1, -2, 0, 0],
            msg="Failed for [-1, 0, -2, 0], expected [-1, -2, 0, 0]"
        )
        self.assertEqual(
            move_zeros_to_end([1, 2, 0]), [1, 2, 0],
            msg="Failed for [1, 2, 0], expected [1, 2, 0]"
        )

    def test_find_first_unique_element(self):
        """Test find_first_unique_element function."""
        self.assertEqual(
            find_first_unique_element([7, 3, 5, 3, 5, 7, 4]), 4,
            msg="Failed to find first unique in [7, 3, 5, 3, 5, 7, 4], expected 4"
        )
        self.assertEqual(
            find_first_unique_element([1, 1, 2, 2]), None,
            msg="Failed for array [1, 1, 2, 2] with no unique elements, expected None"
        )
        self.assertEqual(
            find_first_unique_element([1, 2, 3, 4]), 1,
            msg="Failed for array [1, 2, 3, 4], expected 1"
        )
        self.assertEqual(
            find_first_unique_element([2, 2, 3, 3, 1]), 1,
            msg="Failed for array [2, 2, 3, 3, 1], expected 1"
        )
        self.assertEqual(
            find_first_unique_element([]), None,
            msg="Failed for empty array, expected None"
        )
        self.assertEqual(
            find_first_unique_element([5, 4, 3]), 5,
            msg="Failed for [5, 4, 3], expected 5"
        )
        self.assertEqual(
            find_first_unique_element([-1, -1, 2, 3, 3]), 2,
            msg="Failed for [-1, -1, 2, 3, 3], expected 2"
        )
        self.assertEqual(
            find_first_unique_element([0, 1, 0, 2]), 1,
            msg="Failed for [0, 1, 0, 2], expected 1"
        )

    def test_find_kth_largest(self):
        """Test find_kth_largest function."""
        self.assertEqual(
            find_kth_largest([3, 2, 1, 5, 6, 4], 2), 5,
            msg="Failed to find 2nd largest in [3, 2, 1, 5, 6, 4], expected 5"
        )
        self.assertEqual(
            find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4,
            msg="Failed to find 4th largest in [3, 2, 3, 1, 2, 4, 5, 5, 6], expected 4"
        )
        self.assertEqual(
            find_kth_largest([1], 1), 1,
            msg="Failed for single-element array [1] with k=1, expected 1"
        )
        self.assertEqual(
            find_kth_largest([7, 4, 6, 3, 9, 1], 3), 6,
            msg="Failed to find 3rd largest in [7, 4, 6, 3, 9, 1], expected 6"
        )
        self.assertEqual(
            find_kth_largest([2, 1], 2), 1,
            msg="Failed to find 2nd largest in [2, 1], expected 1"
        )
        self.assertEqual(
            find_kth_largest([4, 4, 4], 2), 4,
            msg="Failed for [4, 4, 4] with k=2, expected 4"
        )
        self.assertEqual(
            find_kth_largest([-3, -2, -1], 1), -1,
            msg="Failed for [-3, -2, -1] with k=1, expected -1"
        )
        self.assertEqual(
            find_kth_largest([1, 2, 3, 4], 4), 1,
            msg="Failed for [1, 2, 3, 4] with k=4, expected 1"
        )

    def test_product_except_self(self):
        """Test product_except_self function."""
        self.assertEqual(
            product_except_self([1, 2, 3, 4]), [24, 12, 8, 6],
            msg="Failed for array [1, 2, 3, 4], expected [24, 12, 8, 6]"
        )
        self.assertEqual(
            product_except_self([2, 3]), [3, 2],
            msg="Failed for array [2, 3], expected [3, 2]"
        )
        self.assertEqual(
            product_except_self([1, 1, 1, 1]), [1, 1, 1, 1],
            msg="Failed for array [1, 1, 1, 1], expected [1, 1, 1, 1]"
        )
        self.assertEqual(
            product_except_self([2, 3, 0, 4]), [0, 0, 24, 0],
            msg="Failed for array [2, 3, 0, 4], expected [0, 0, 24, 0]"
        )
        self.assertEqual(
            product_except_self([0, 0]), [0, 0],
            msg="Failed for array [0, 0], expected [0, 0]"
        )
        self.assertEqual(
            product_except_self([-1, -2, -3]), [6, 3, 2],
            msg="Failed for [-1, -2, -3], expected [6, 3, 2]"
        )
        self.assertEqual(
            product_except_self([0, 0, 1]), [0, 0, 0],
            msg="Failed for [0, 0, 1], expected [0, 0, 0]"
        )
        self.assertEqual(
            product_except_self([1, 0, 0]), [0, 1, 1],
            msg="Failed for [1, 0, 0], expected [0, 1, 1]"
        )

    def test_find_longest_consecutive_sequence(self):
        """Test find_longest_consecutive_sequence function."""
        self.assertEqual(
            find_longest_consecutive_sequence([100, 4, 200, 1, 3, 2]), 4,
            msg="Failed for array [100, 4, 200, 1, 3, 2], expected 4"
        )
        self.assertEqual(
            find_longest_consecutive_sequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9,
            msg="Failed for array [0, 3, 7, 2, 5, 8, 4, 6, 0, 1], expected 9"
        )
        self.assertEqual(
            find_longest_consecutive_sequence([1, 2, 0, 1]), 3,
            msg="Failed for array [1, 2, 0, 1], expected 3"
        )
        self.assertEqual(
            find_longest_consecutive_sequence([]), 0,
            msg="Failed for empty array, expected 0"
        )
        self.assertEqual(
            find_longest_consecutive_sequence([1]), 1,
            msg="Failed for single-element array [1], expected 1"
        )
        self.assertEqual(
            find_longest_consecutive_sequence([-1, 0, 1, -2]), 4,
            msg="Failed for [-1, 0, 1, -2], expected 4"
        )
        self.assertEqual(
            find_longest_consecutive_sequence([1, 3, 5]), 1,
            msg="Failed for [1, 3, 5], expected 1"
        )
        self.assertEqual(
            find_longest_consecutive_sequence([10, 8, 7, 9, 6]), 5,
            msg="Failed for [10, 8, 7, 9, 6], expected 5"
        )

    def test_sum_array(self):
        """Test sum_array function."""
        self.assertEqual(
            sum_array([1, 2, 3, 4]), 10,
            msg="Failed to sum [1, 2, 3, 4], expected 10"
        )
        self.assertEqual(
            sum_array([]), 0,
            msg="Failed for empty array, expected 0"
        )
        self.assertEqual(
            sum_array([-1, 1]), 0,
            msg="Failed for array [-1, 1], expected 0"
        )
        self.assertEqual(
            sum_array([5]), 5,
            msg="Failed for single-element array [5], expected 5"
        )
        self.assertEqual(
            sum_array([-2, -3, -4]), -9,
            msg="Failed for all-negative array [-2, -3, -4], expected -9"
        )
        self.assertEqual(
            sum_array([0, 0, 0]), 0,
            msg="Failed for [0, 0, 0], expected 0"
        )
        self.assertEqual(
            sum_array([2, -2, 3, -3]), 0,
            msg="Failed for [2, -2, 3, -3], expected 0"
        )
        self.assertEqual(
            sum_array([100, 200, 300]), 600,
            msg="Failed for [100, 200, 300], expected 600"
        )

    def test_count_evens(self):
        """Test count_evens function."""
        self.assertEqual(
            count_evens([2, 4, 1, 6, 3]), 3,
            msg="Failed to count evens in [2, 4, 1, 6, 3], expected 3"
        )
        self.assertEqual(
            count_evens([1, 3, 5]), 0,
            msg="Failed for array [1, 3, 5] with no evens, expected 0"
        )
        self.assertEqual(
            count_evens([]), 0,
            msg="Failed for empty array, expected 0"
        )
        self.assertEqual(
            count_evens([2, 4, 6]), 3,
            msg="Failed for all-even array [2, 4, 6], expected 3"
        )
        self.assertEqual(
            count_evens([1]), 0,
            msg="Failed for single-element array [1], expected 0"
        )
        self.assertEqual(
            count_evens([-2, -4, 1]), 2,
            msg="Failed for [-2, -4, 1], expected 2"
        )
        self.assertEqual(
            count_evens([0, 1, 0]), 2,
            msg="Failed for [0, 1, 0], expected 2"
        )
        self.assertEqual(
            count_evens([4, 6, 8]), 3,
            msg="Failed for [4, 6, 8], expected 3"
        )

    def test_reverse_array(self):
        """Test reverse_array function."""
        self.assertEqual(
            reverse_array([1, 2, 3, 4]), [4, 3, 2, 1],
            msg="Failed to reverse [1, 2, 3, 4], expected [4, 3, 2, 1]"
        )
        self.assertEqual(
            reverse_array([1]), [1],
            msg="Failed for single-element array [1], expected [1]"
        )
        self.assertEqual(
            reverse_array([]), [],
            msg="Failed for empty array, expected []"
        )
        self.assertEqual(
            reverse_array([5, 5, 5]), [5, 5, 5],
            msg="Failed for array [5, 5, 5], expected [5, 5, 5]"
        )
        self.assertEqual(
            reverse_array([-1, 0, 1]), [1, 0, -1],
            msg="Failed for array [-1, 0, 1], expected [1, 0, -1]"
        )
        self.assertEqual(
            reverse_array([0, 0, 0]), [0, 0, 0],
            msg="Failed for [0, 0, 0], expected [0, 0, 0]"
        )
        self.assertEqual(
            reverse_array([-1, 2, -3]), [-3, 2, -1],
            msg="Failed for [-1, 2, -3], expected [-3, 2, -1]"
        )
        self.assertEqual(
            reverse_array([1, 2, 3, 4, 5, 6]), [6, 5, 4, 3, 2, 1],
            msg="Failed for [1, 2, 3, 4, 5, 6], expected [6, 5, 4, 3, 2, 1]"
        )

    def test_find_max_element(self):
        """Test find_max_element function."""
        self.assertEqual(
            find_max_element([3, 5, 1, 4, 2]), 5,
            msg="Failed to find max in [3, 5, 1, 4, 2], expected 5"
        )
        self.assertEqual(
            find_max_element([1]), 1,
            msg="Failed for single-element array [1], expected 1"
        )
        self.assertEqual(
            find_max_element([]), None,
            msg="Failed for empty array, expected None"
        )
        self.assertEqual(
            find_max_element([-1, -2, -3]), -1,
            msg="Failed for all-negative array [-1, -2, -3], expected -1"
        )
        self.assertEqual(
            find_max_element([0, 0, 0]), 0,
            msg="Failed for all-zero array [0, 0, 0], expected 0"
        )
        self.assertEqual(
            find_max_element([-5, 0, 5]), 5,
            msg="Failed for [-5, 0, 5], expected 5"
        )
        self.assertEqual(
            find_max_element([3, 3, 3]), 3,
            msg="Failed for [3, 3, 3], expected 3"
        )
        self.assertEqual(
            find_max_element([1, 100, 2]), 100,
            msg="Failed for [1, 100, 2], expected 100"
        )

    def test_replace_negatives(self):
        """Test replace_negatives function."""
        self.assertEqual(
            replace_negatives([-1, 2, -3, 4]), [0, 2, 0, 4],
            msg="Failed to replace negatives in [-1, 2, -3, 4], expected [0, 2, 0, 4]"
        )
        self.assertEqual(
            replace_negatives([1, 2, 3]), [1, 2, 3],
            msg="Failed for array [1, 2, 3] with no negatives, expected [1, 2, 3]"
        )
        self.assertEqual(
            replace_negatives([-1, -2]), [0, 0],
            msg="Failed for array [-1, -2], expected [0, 0]"
        )
        self.assertEqual(
            replace_negatives([]), [],
            msg="Failed for empty array, expected []"
        )
        self.assertEqual(
            replace_negatives([0, 1, 0]), [0, 1, 0],
            msg="Failed for array [0, 1, 0], expected [0, 1, 0]"
        )
        self.assertEqual(
            replace_negatives([-1, 0, -2]), [0, 0, 0],
            msg="Failed for [-1, 0, -2], expected [0, 0, 0]"
        )
        self.assertEqual(
            replace_negatives([-5]), [0],
            msg="Failed for [-5], expected [0]"
        )
        self.assertEqual(
            replace_negatives([-10, -20]), [0, 0],
            msg="Failed for [-10, -20], expected [0, 0]"
        )

    def test_find_element_index(self):
        """Test find_element_index function."""
        self.assertEqual(
            find_element_index([1, 2, 3, 2], 2), 1,
            msg="Failed to find index of 2 in [1, 2, 3, 2], expected 1"
        )
        self.assertEqual(
            find_element_index([1, 3, 4], 5), -1,
            msg="Failed for target 5 in [1, 3, 4], expected -1"
        )
        self.assertEqual(
            find_element_index([], 1), -1,
            msg="Failed for empty array with target 1, expected -1"
        )
        self.assertEqual(
            find_element_index([1], 1), 0,
            msg="Failed for single-element array [1] with target 1, expected 0"
        )
        self.assertEqual(
            find_element_index([2, 2, 2], 2), 0,
            msg="Failed for array [2, 2, 2] with target 2, expected 0"
        )
        self.assertEqual(
            find_element_index([-1, 2, 3], -1), 0,
            msg="Failed for [-1, 2, 3] with target -1, expected 0"
        )
        self.assertEqual(
            find_element_index([0, 1, 0], 0), 0,
            msg="Failed for [0, 1, 0] with target 0, expected 0"
        )
        self.assertEqual(
            find_element_index([1, 2, 3], 3), 2,
            msg="Failed for [1, 2, 3] with target 3, expected 2"
        )

    def test_filter_greater_than(self):
        """Test filter_greater_than function."""
        self.assertEqual(
            filter_greater_than([1, 5, 2, 6, 3], 3), [5, 6],
            msg="Failed to filter [1, 5, 2, 6, 3] with threshold 3, expected [5, 6]"
        )
        self.assertEqual(
            filter_greater_than([1, 2, 3], 5), [],
            msg="Failed for [1, 2, 3] with threshold 5, expected []"
        )
        self.assertEqual(
            filter_greater_than([], 0), [],
            msg="Failed for empty array with threshold 0, expected []"
        )
        self.assertEqual(
            filter_greater_than([4, 4, 4], 3), [4, 4, 4],
            msg="Failed for [4, 4, 4] with threshold 3, expected [4, 4, 4]"
        )
        self.assertEqual(
            filter_greater_than([-1, -2, -3], -4), [-1, -2, -3],
            msg="Failed for [-1, -2, -3] with threshold -4, expected [-1, -2, -3]"
        )
        self.assertEqual(
            filter_greater_than([0, 1, -1], 0), [1],
            msg="Failed for [0, 1, -1] with threshold 0, expected [1]"
        )
        self.assertEqual(
            filter_greater_than([1, 2, 3], 4), [],
            msg="Failed for [1, 2, 3] with threshold 4, expected []"
        )
        self.assertEqual(
            filter_greater_than([10, 20, 30], 15), [20, 30],
            msg="Failed for [10, 20, 30] with threshold 15, expected [20, 30]"
        )

    def test_multiply_array(self):
        """Test multiply_array function."""
        self.assertEqual(
            multiply_array([1, 2, 3], 2), [2, 4, 6],
            msg="Failed to multiply [1, 2, 3] by 2, expected [2, 4, 6]"
        )
        self.assertEqual(
            multiply_array([0, 1, -2], 3), [0, 3, -6],
            msg="Failed to multiply [0, 1, -2] by 3, expected [0, 3, -6]"
        )
        self.assertEqual(
            multiply_array([], 5), [],
            msg="Failed for empty array with factor 5, expected []"
        )
        self.assertEqual(
            multiply_array([1], 0), [0],
            msg="Failed for [1] with factor 0, expected [0]"
        )
        self.assertEqual(
            multiply_array([-1, -1], -2), [2, 2],
            msg="Failed for [-1, -1] with factor -2, expected [2, 2]"
        )
        self.assertEqual(
            multiply_array([1, 2], -1), [-1, -2],
            msg="Failed for [1, 2] with factor -1, expected [-1, -2]"
        )
        self.assertEqual(
            multiply_array([0, 0], 5), [0, 0],
            msg="Failed for [0, 0] with factor 5, expected [0, 0]"
        )
        self.assertEqual(
            multiply_array([1, 2], 10), [10, 20],
            msg="Failed for [1, 2] with factor 10, expected [10, 20]"
        )

    def test_remove_duplicates(self):
        """Test remove_duplicates function."""
        self.assertEqual(
            remove_duplicates([1, 2, 2, 3, 1]), [1, 2, 3],
            msg="Failed to remove duplicates from [1, 2, 2, 3, 1], expected [1, 2, 3]"
        )
        self.assertEqual(
            remove_duplicates([1, 1, 1]), [1],
            msg="Failed for [1, 1, 1], expected [1]"
        )
        self.assertEqual(
            remove_duplicates([]), [],
            msg="Failed for empty array, expected []"
        )
        self.assertEqual(
            remove_duplicates([2, 3, 4]), [2, 3, 4],
            msg="Failed for [2, 3, 4] with no duplicates, expected [2, 3, 4]"
        )
        self.assertEqual(
            remove_duplicates([1, 1, 2, 2, 3, 3]), [1, 2, 3],
            msg="Failed for [1, 1, 2, 2, 3, 3], expected [1, 2, 3]"
        )
        self.assertEqual(
            remove_duplicates([-1, -1, 2, 2]), [-1, 2],
            msg="Failed for [-1, -1, 2, 2], expected [-1, 2]"
        )
        self.assertEqual(
            remove_duplicates([0, 0, 1]), [0, 1],
            msg="Failed for [0, 0, 1], expected [0, 1]"
        )
        self.assertEqual(
            remove_duplicates([1, 2, 2, 3, 3, 3]), [1, 2, 3],
            msg="Failed for [1, 2, 2, 3, 3, 3], expected [1, 2, 3]"
        )

    def test_shift_elements(self):
        """Test shift_elements function."""
        self.assertEqual(
            shift_elements([1, 2, 3, 4], 2), [3, 4, 0, 0],
            msg="Failed to shift [1, 2, 3, 4] by 2, expected [3, 4, 0, 0]"
        )
        self.assertEqual(
            shift_elements([1, 2, 3], 0), [1, 2, 3],
            msg="Failed for [1, 2, 3] with shift 0, expected [1, 2, 3]"
        )
        self.assertEqual(
            shift_elements([1], 5), [0],
            msg="Failed for [1] with shift 5, expected [0]"
        )
        self.assertEqual(
            shift_elements([], 3), [],
            msg="Failed for empty array with shift 3, expected []"
        )
        self.assertEqual(
            shift_elements([1, 2], 1), [2, 0],
            msg="Failed for [1, 2] with shift 1, expected [2, 0]"
        )
        self.assertEqual(
            shift_elements([-1, -2, -3], 1), [-2, -3, 0],
            msg="Failed for [-1, -2, -3] with shift 1, expected [-2, -3, 0]"
        )
        self.assertEqual(
            shift_elements([1, 2, 3], 5), [0, 0, 0],
            msg="Failed for [1, 2, 3] with shift 5, expected [0, 0, 0]"
        )
        self.assertEqual(
            shift_elements([0, 1, 2], 2), [2, 0, 0],
            msg="Failed for [0, 1, 2] with shift 2, expected [2, 0, 0]"
        )

    def test_group_by_sum(self):
        """Test group_by_sum function."""
        self.assertEqual(
            group_by_sum([1, 2, 3, 4, 5], 5), [[1, 4], [2, 3], [5]],
            msg="Failed to group [1, 2, 3, 4, 5] with sum 5, expected [[1, 4], [2, 3], [5]]"
        )
        self.assertEqual(
            group_by_sum([1, 2, 3], 10), [],
            msg="Failed for [1, 2, 3] with sum 10, expected []"
        )
        self.assertEqual(
            group_by_sum([], 5), [],
            msg="Failed for empty array with sum 5, expected []"
        )
        self.assertEqual(
            group_by_sum([2, 2, 1, 1], 3), [[2, 1], [2, 1]],
            msg="Failed for [2, 2, 1, 1] with sum 3, expected [[2, 1], [2, 1]]"
        )
        self.assertEqual(
            group_by_sum([1], 1), [[1]],
            msg="Failed for [1] with sum 1, expected [[1]]"
        )
        self.assertEqual(
            group_by_sum([-1, -2, 3, 2], 1), [[-1, 2], [-2, 3]],
            msg="Failed for [-1, -2, 3, 2] with sum 1, expected [[-1, 2], [-2, 3]]"
        )
        self.assertEqual(
            group_by_sum([0, 0, 1], 0), [[0, 0]],
            msg="Failed for [0, 0, 1] with sum 0, expected [[0, 0]]"
        )
        self.assertEqual(
            group_by_sum([1, 2, 3], 10), [],
            msg="Failed for [1, 2, 3] with sum 10, expected []"
        )

    def test_split_array_equal_sums(self):
        """Test split_array_equal_sums function."""
        self.assertEqual(
            split_array_equal_sums([1, 2, 3, 4, 5, 5]), 4,
            msg="Failed to split [1, 2, 3, 4, 5, 5], expected index 4"
        )
        self.assertEqual(
            split_array_equal_sums([1, 2, 3]), 2,
            msg="Failed for [1, 2, 3], expected index 2"
        )
        self.assertEqual(
            split_array_equal_sums([]), -1,
            msg="Failed for empty array, expected -1"
        )
        self.assertEqual(
            split_array_equal_sums([2, 2]), 1,
            msg="Failed for [2, 2], expected index 1"
        )
        self.assertEqual(
            split_array_equal_sums([1, 1, 1, 1, 4]), 4,
            msg="Failed for [1, 1, 1, 1, 4], expected index 4"
        )
        self.assertEqual(
            split_array_equal_sums([1, -1, 1, -1]), 2,
            msg="Failed for [1, -1, 1, -1], expected index 2"
        )
        self.assertEqual(
            split_array_equal_sums([0, 0, 0]), 1,
            msg="Failed for [0, 0, 0], expected index 1"
        )
        self.assertEqual(
            split_array_equal_sums([2, 3, 5, 5]), 2,
            msg="Failed for [2, 3, 5, 5], expected index 2"
        )

    def test_max_product_pair(self):
        """Test max_product_pair function."""
        self.assertEqual(
            max_product_pair([1, 2, 3, 4]), (3, 4),
            msg="Failed to find max product pair in [1, 2, 3, 4], expected (3, 4)"
        )
        self.assertEqual(
            max_product_pair([-4, -3, 0, 2]), (-4, -3),
            msg="Failed for [-4, -3, 0, 2], expected (-4, -3)"
        )
        self.assertEqual(
            max_product_pair([1]), None,
            msg="Failed for single-element array [1], expected None"
        )
        self.assertEqual(
            max_product_pair([]), None,
            msg="Failed for empty array, expected None"
        )
        self.assertEqual(
            max_product_pair([-2, -2, 1, 1]), (-2, -2),
            msg="Failed for [-2, -2, 1, 1], expected (-2, -2)"
        )
        self.assertEqual(
            max_product_pair([0, 0, 1]), (0, 1),
            msg="Failed for [0, 0, 1], expected (0, 1)"
        )
        self.assertEqual(
            max_product_pair([10, 20, 30]), (20, 30),
            msg="Failed for [10, 20, 30], expected (20, 30)"
        )
        self.assertEqual(
            max_product_pair([-5, 2, 3]), (-5, 3),
            msg="Failed for [-5, 2, 3], expected (-5, 3)"
        )

    def test_find_common_elements(self):
        """Test find_common_elements function."""
        self.assertEqual(
            find_common_elements([1, 2, 3, 4], [2, 4, 6]), [2, 4],
            msg="Failed to find common elements in [1, 2, 3, 4] and [2, 4, 6], expected [2, 4]"
        )
        self.assertEqual(
            find_common_elements([1, 2], [3, 4]), [],
            msg="Failed for [1, 2] and [3, 4], expected []"
        )
        self.assertEqual(
            find_common_elements([], [1, 2]), [],
            msg="Failed for empty first array and [1, 2], expected []"
        )
        self.assertEqual(
            find_common_elements([1, 1, 2], [1, 2]), [1, 2],
            msg="Failed for [1, 1, 2] and [1, 2], expected [1, 2]"
        )
        self.assertEqual(
            find_common_elements([3, 3, 3], [3]), [3],
            msg="Failed for [3, 3, 3] and [3], expected [3]"
        )
        self.assertEqual(
            find_common_elements([-1, -2], [-2, -3]), [-2],
            msg="Failed for [-1, -2] and [-2, -3], expected [-2]"
        )
        self.assertEqual(
            find_common_elements([0, 1], [0, 2]), [0],
            msg="Failed for [0, 1] and [0, 2], expected [0]"
        )
        self.assertEqual(
            find_common_elements([1, 2, 3, 4], [2, 3, 5]), [2, 3],
            msg="Failed for [1, 2, 3, 4] and [2, 3, 5], expected [2, 3]"
        )

    def test_rotate_left_by_one(self):
        """Test rotate_left_by_one function."""
        self.assertEqual(
            rotate_left_by_one([1, 2, 3, 4]), [2, 3, 4, 1],
            msg="Failed to rotate [1, 2, 3, 4], expected [2, 3, 4, 1]"
        )
        self.assertEqual(
            rotate_left_by_one([1]), [1],
            msg="Failed for single-element array [1], expected [1]"
        )
        self.assertEqual(
            rotate_left_by_one([]), [],
            msg="Failed for empty array, expected []"
        )
        self.assertEqual(
            rotate_left_by_one([0, 0, 0]), [0, 0, 0],
            msg="Failed for [0, 0, 0], expected [0, 0, 0]"
        )
        self.assertEqual(
            rotate_left_by_one([-1, 2, -3]), [2, -3, -1],
            msg="Failed for [-1, 2, -3], expected [2, -3, -1]"
        )
        self.assertEqual(
            rotate_left_by_one([2, 2, 2]), [2, 2, 2],
            msg="Failed for [2, 2, 2], expected [2, 2, 2]"
        )
        self.assertEqual(
            rotate_left_by_one([-1, 0, 1]), [0, 1, -1],
            msg="Failed for [-1, 0, 1], expected [0, 1, -1]"
        )
        self.assertEqual(
            rotate_left_by_one([1, 2, 3, 4, 5]), [2, 3, 4, 5, 1],
            msg="Failed for [1, 2, 3, 4, 5], expected [2, 3, 4, 5, 1]"
        )

    def test_find_pairs_with_sum(self):
        """Test find_pairs_with_sum function."""
        self.assertEqual(
            find_pairs_with_sum([1, 2, 3, 4], 5), [(1, 4), (2, 3)],
            msg="Failed to find pairs in [1, 2, 3, 4] with sum 5, expected [(1, 4), (2, 3)]"
        )
        self.assertEqual(
            find_pairs_with_sum([1, 2, 3], 10), [],
            msg="Failed for [1, 2, 3] with sum 10, expected []"
        )
        self.assertEqual(
            find_pairs_with_sum([2, 2, 2], 4), [(2, 2)],
            msg="Failed for [2, 2, 2] with sum 4, expected [(2, 2)]"
        )
        self.assertEqual(
            find_pairs_with_sum([], 5), [],
            msg="Failed for empty array with sum 5, expected []"
        )
        self.assertEqual(
            find_pairs_with_sum([0, 0], 0), [(0, 0)],
            msg="Failed for [0, 0] with sum 0, expected [(0, 0)]"
        )
        self.assertEqual(
            find_pairs_with_sum([-1, 1, -1], 0), [(-1, 1)],
            msg="Failed for [-1, 1, -1] with sum 0, expected [(-1, 1)]"
        )
        self.assertEqual(
            find_pairs_with_sum([1, 2, 3], 5), [(2, 3)],
            msg="Failed for [1, 2, 3] with sum 5, expected [(2, 3)]"
        )
        self.assertEqual(
            find_pairs_with_sum([1, 1], 3), [],
            msg="Failed for [1, 1] with sum 3, expected []"
        )

    def test_segregate_pos_neg(self):
        """Test segregate_pos_neg function."""
        self.assertEqual(
            segregate_pos_neg([-1, 2, -3, 4, -5]), [2, 4, -1, -3, -5],
            msg="Failed to segregate [-1, 2, -3, 4, -5], expected [2, 4, -1, -3, -5]"
        )
        self.assertEqual(
            segregate_pos_neg([1, 2, 3]), [1, 2, 3],
            msg="Failed for [1, 2, 3], expected [1, 2, 3]"
        )
        self.assertEqual(
            segregate_pos_neg([-1, -2, -3]), [-1, -2, -3],
            msg="Failed for [-1, -2, -3], expected [-1, -2, -3]"
        )
        self.assertEqual(
            segregate_pos_neg([]), [],
            msg="Failed for empty array, expected []"
        )
        self.assertEqual(
            segregate_pos_neg([0, 1, -1, 0]), [0, 1, 0, -1],
            msg="Failed for [0, 1, -1, 0], expected [0, 1, 0, -1]"
        )
        self.assertEqual(
            segregate_pos_neg([2, 2, -2, -2]), [2, 2, -2, -2],
            msg="Failed for [2, 2, -2, -2], expected [2, 2, -2, -2]"
        )
        self.assertEqual(
            segregate_pos_neg([0, -1, 1]), [0, 1, -1],
            msg="Failed for [0, -1, 1], expected [0, 1, -1]"
        )
        self.assertEqual(
            segregate_pos_neg([5, -5, 3, -3, 2]), [5, 3, 2, -5, -3],
            msg="Failed for [5, -5, 3, -3, 2], expected [5, 3, 2, -5, -3]"
        )

    def test_find_subarray_with_sum(self):
        """Test find_subarray_with_sum function."""
        self.assertEqual(
            find_subarray_with_sum([1, 2, 3, 4], 5), (0, 1),
            msg="Failed to find subarray in [1, 2, 3, 4] with sum 5, expected (0, 1)"
        )
        self.assertEqual(
            find_subarray_with_sum([1, 2, 3], 10), (-1, -1),
            msg="Failed for [1, 2, 3] with sum 10, expected (-1, -1)"
        )
        self.assertEqual(
            find_subarray_with_sum([], 0), (-1, -1),
            msg="Failed for empty array with sum 0, expected (-1, -1)"
        )
        self.assertEqual(
            find_subarray_with_sum([5], 5), (0, 0),
            msg="Failed for [5] with sum 5, expected (0, 0)"
        )
        self.assertEqual(
            find_subarray_with_sum([-1, 1, 0], 0), (1, 2),
            msg="Failed for [-1, 1, 0] with sum 0, expected (1, 2)"
        )
        self.assertEqual(
            find_subarray_with_sum([0, 0, 1], 0), (0, 1),
            msg="Failed for [0, 0, 1] with sum 0, expected (0, 1)"
        )
        self.assertEqual(
            find_subarray_with_sum([-2, -1, 1], -3), (0, 1),
            msg="Failed for [-2, -1, 1] with sum -3, expected (0, 1)"
        )
        self.assertEqual(
            find_subarray_with_sum([1, 2, 3, 4], 9), (0, 3),
            msg="Failed for [1, 2, 3, 4] with sum 9, expected (0, 3)"
        )

    def test_alternate_elements(self):
        """Test alternate_elements function."""
        self.assertEqual(
            alternate_elements([1, 2, 3, 4, 5]), [1, 3, 5],
            msg="Failed to get alternate elements from [1, 2, 3, 4, 5], expected [1, 3, 5]"
        )
        self.assertEqual(
            alternate_elements([1]), [1],
            msg="Failed for single-element array [1], expected [1]"
        )
        self.assertEqual(
            alternate_elements([]), [],
            msg="Failed for empty array, expected []"
        )
        self.assertEqual(
            alternate_elements([2, 2, 2, 2]), [2, 2],
            msg="Failed for [2, 2, 2, 2], expected [2, 2]"
        )
        self.assertEqual(
            alternate_elements([-1, 0, 1]), [-1, 1],
            msg="Failed for [-1, 0, 1], expected [-1, 1]"
        )
        self.assertEqual(
            alternate_elements([0, 1, 0, 2]), [0, 0],
            msg="Failed for [0, 1, 0, 2], expected [0, 0]"
        )
        self.assertEqual(
            alternate_elements([1, 2, 3, 4, 5, 6]), [1, 3, 5],
            msg="Failed for [1, 2, 3, 4, 5, 6], expected [1, 3, 5]"
        )
        self.assertEqual(
            alternate_elements([-1, 2, -3, 4]), [-1, -3],
            msg="Failed for [-1, 2, -3, 4], expected [-1, -3]"
        )

    def test_count_frequency(self):
        """Test count_frequency function."""
        self.assertEqual(
            count_frequency([1, 2, 2, 3, 1]), {1: 2, 2: 2, 3: 1},
            msg="Failed to count frequencies in [1, 2, 2, 3, 1], expected {1: 2, 2: 2, 3: 1}"
        )
        self.assertEqual(
            count_frequency([]), {},
            msg="Failed for empty array, expected {}"
        )
        self.assertEqual(
            count_frequency([1, 1, 1]), {1: 3},
            msg="Failed for [1, 1, 1], expected {1: 3}"
        )
        self.assertEqual(
            count_frequency([0, 0, -1]), {0: 2, -1: 1},
            msg="Failed for [0, 0, -1], expected {0: 2, -1: 1}"
        )
        self.assertEqual(
            count_frequency([2]), {2: 1},
            msg="Failed for [2], expected {2: 1}"
        )
        self.assertEqual(
            count_frequency([0, 1, 0]), {0: 2, 1: 1},
            msg="Failed for [0, 1, 0], expected {0: 2, 1: 1}"
        )
        self.assertEqual(
            count_frequency([-1, -1, 2]), {-1: 2, 2: 1},
            msg="Failed for [-1, -1, 2], expected {-1: 2, 2: 1}"
        )
        self.assertEqual(
            count_frequency([1, 1, 2, 2, 3]), {1: 2, 2: 2, 3: 1},
            msg="Failed for [1, 1, 2, 2, 3], expected {1: 2, 2: 2, 3: 1}"
        )

    def test_find_subarray_product(self):
        """Test find_subarray_product function."""
        self.assertEqual(
            find_subarray_product([2, 3, 4, 2], 6), (0, 1),
            msg="Failed to find subarray in [2, 3, 4, 2] with product 6, expected (0, 1)"
        )
        self.assertEqual(
            find_subarray_product([1, 2, 3], 10), (-1, -1),
            msg="Failed for [1, 2, 3] with product 10, expected (-1, -1)"
        )
        self.assertEqual(
            find_subarray_product([], 1), (-1, -1),
            msg="Failed for empty array with product 1, expected (-1, -1)"
        )
        self.assertEqual(
            find_subarray_product([5], 5), (0, 0),
            msg="Failed for [5] with product 5, expected (0, 0)"
        )
        self.assertEqual(
            find_subarray_product([-2, 3, -3], 6), (0, 1),
            msg="Failed for [-2, 3, -3] with product 6, expected (0, 1)"
        )
        self.assertEqual(
            find_subarray_product([0, 1, 0], 0), (0, 0),
            msg="Failed for [0, 1, 0] with product 0, expected (0, 0)"
        )
        self.assertEqual(
            find_subarray_product([-2, -3, 2], 6), (0, 1),
            msg="Failed for [-2, -3, 2] with product 6, expected (0, 1)"
        )
        self.assertEqual(
            find_subarray_product([2, 3, 4], 12), (1, 2),
            msg="Failed for [2, 3, 4] with product 12, expected (1, 2)"
        )

    def test_merge_alternate(self):
        """Test merge_alternate function."""
        self.assertEqual(
            merge_alternate([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6],
            msg="Failed to merge [1, 3, 5] and [2, 4, 6], expected [1, 2, 3, 4, 5, 6]"
        )
        self.assertEqual(
            merge_alternate([1], [2]), [1, 2],
            msg="Failed for [1] and [2], expected [1, 2]"
        )
        self.assertEqual(
            merge_alternate([], [1, 2]), [1, 2],
            msg="Failed for empty first array and [1, 2], expected [1, 2]"
        )
        self.assertEqual(
            merge_alternate([1, 2], []), [1, 2],
            msg="Failed for [1, 2] and empty second array, expected [1, 2]"
        )
        self.assertEqual(
            merge_alternate([1, 3, 5], [2]), [1, 2, 3, 5],
            msg="Failed for [1, 3, 5] and [2], expected [1, 2, 3, 5]"
        )
        self.assertEqual(
            merge_alternate([-1, -2], [1, 2]), [-1, 1, -2, 2],
            msg="Failed for [-1, -2] and [1, 2], expected [-1, 1, -2, 2]"
        )
        self.assertEqual(
            merge_alternate([0, 0], [1]), [0, 1, 0],
            msg="Failed for [0, 0] and [1], expected [0, 1, 0]"
        )
        self.assertEqual(
            merge_alternate([1, 3, 5, 7], [2, 4]), [1, 2, 3, 4, 5, 7],
            msg="Failed for [1, 3, 5, 7] and [2, 4], expected [1, 2, 3, 4, 5, 7]"
        )

    def test_find_min_max_difference(self):
        """Test find_min_max_difference function."""
        self.assertEqual(
            find_min_max_difference([3, 1, 4, 2]), 3,
            msg="Failed for [3, 1, 4, 2], expected 3"
        )
        self.assertEqual(
            find_min_max_difference([5]), 0,
            msg="Failed for single-element array [5], expected 0"
        )
        self.assertEqual(
            find_min_max_difference([]), 0,
            msg="Failed for empty array, expected 0"
        )
        self.assertEqual(
            find_min_max_difference([-1, -5, -3]), 4,
            msg="Failed for [-1, -5, -3], expected 4"
        )
        self.assertEqual(
            find_min_max_difference([2, 2, 2]), 0,
            msg="Failed for [2, 2, 2], expected 0"
        )
        self.assertEqual(
            find_min_max_difference([0, 0, 0]), 0,
            msg="Failed for [0, 0, 0], expected 0"
        )
        self.assertEqual(
            find_min_max_difference([-5, 5]), 10,
            msg="Failed for [-5, 5], expected 10"
        )
        self.assertEqual(
            find_min_max_difference([100, 1, 50]), 99,
            msg="Failed for [100, 1, 50], expected 99"
        )

    def test_partition_array(self):
        """Test partition_array function."""
        self.assertEqual(
            partition_array([3, 1, 4, 2, 3], 3), [1, 2, 3, 3, 4],
            msg="Failed to partition [3, 1, 4, 2, 3] around 3, expected [1, 2, 3, 3, 4]"
        )
        self.assertEqual(
            partition_array([1, 2], 5), [1, 2],
            msg="Failed for [1, 2] with pivot 5, expected [1, 2]"
        )
        self.assertEqual(
            partition_array([], 0), [],
            msg="Failed for empty array with pivot 0, expected []"
        )
        self.assertEqual(
            partition_array([5, 5, 5], 5), [5, 5, 5],
            msg="Failed for [5, 5, 5] with pivot 5, expected [5, 5, 5]"
        )
        self.assertEqual(
            partition_array([-1, 0, 1], 0), [-1, 0, 1],
            msg="Failed for [-1, 0, 1] with pivot 0, expected [-1, 0, 1]"
        )
        self.assertEqual(
            partition_array([-1, 2, -3], -2), [-3, -1, 2],
            msg="Failed for [-1, 2, -3] with pivot -2, expected [-3, -1, 2]"
        )
        self.assertEqual(
            partition_array([0, 1, 0], 0), [0, 0, 1],
            msg="Failed for [0, 1, 0] with pivot 0, expected [0, 0, 1]"
        )
        self.assertEqual(
            partition_array([5, 3, 7, 1], 4), [3, 1, 5, 7],
            msg="Failed for [5, 3, 7, 1] with pivot 4, expected [3, 1, 5, 7]"
        )

    def test_find_unique_elements(self):
        """Test find_unique_elements function."""
        self.assertEqual(
            find_unique_elements([1, 2, 3], [2, 3, 4]), [1, 4],
            msg="Failed for [1, 2, 3] and [2, 3, 4], expected [1, 4]"
        )
        self.assertEqual(
            find_unique_elements([1, 1], [2, 2]), [1, 2],
            msg="Failed for [1, 1] and [2, 2], expected [1, 2]"
        )
        self.assertEqual(
            find_unique_elements([], [1]), [1],
            msg="Failed for empty first array and [1], expected [1]"
        )
        self.assertEqual(
            find_unique_elements([1, 2], []), [1, 2],
            msg="Failed for [1, 2] and empty second array, expected [1, 2]"
        )
        self.assertEqual(
            find_unique_elements([1, 1, 1], [1, 1]), [1],
            msg="Failed for [1, 1, 1] and [1, 1], expected [1]"
        )
        self.assertEqual(
            find_unique_elements([-1, -2], [-2, -3]), [-1, -3],
            msg="Failed for [-1, -2] and [-2, -3], expected [-1, -3]"
        )
        self.assertEqual(
            find_unique_elements([0, 1], [0, 2]), [1, 2],
            msg="Failed for [0, 1] and [0, 2], expected [1, 2]"
        )
        self.assertEqual(
            find_unique_elements([1, 2, 3], [3, 4]), [1, 2, 4],
            msg="Failed for [1, 2, 3] and [3, 4], expected [1, 2, 4]"
        )

    def test_sum_pairs_to_target(self):
        """Test sum_pairs_to_target function."""
        self.assertEqual(
            sum_pairs_to_target([1, 2, 3, 4], 5), 10,
            msg="Failed for [1, 2, 3, 4] with target 5, expected 10"
        )
        self.assertEqual(
            sum_pairs_to_target([1, 2, 3], 10), 0,
            msg="Failed for [1, 2, 3] with target 10, expected 0"
        )
        self.assertEqual(
            sum_pairs_to_target([2, 2], 4), 4,
            msg="Failed for [2, 2] with target 4, expected 4"
        )
        self.assertEqual(
            sum_pairs_to_target([], 5), 0,
            msg="Failed for empty array with target 5, expected 0"
        )
        self.assertEqual(
            sum_pairs_to_target([-1, 1, -1, 1], 0), 0,
            msg="Failed for [-1, 1, -1, 1] with target 0, expected 0"
        )
        self.assertEqual(
            sum_pairs_to_target([0, 0, 1], 0), 0,
            msg="Failed for [0, 0, 1] with target 0, expected 0"
        )
        self.assertEqual(
            sum_pairs_to_target([-1, -2, 3], -3), -3,
            msg="Failed for [-1, -2, 3] with target -3, expected -3"
        )
        self.assertEqual(
            sum_pairs_to_target([1, 2, 3], 6), 0,
            msg="Failed for [1, 2, 3] with target 6, expected 0"
        )

    def test_swap_elements(self):
        """Test swap_elements function."""
        self.assertEqual(
            swap_elements([1, 2, 3, 4, 5], 2), [3, 2, 1, 4, 5],
            msg="Failed to swap [1, 2, 3, 4, 5] with k=2, expected [3, 2, 1, 4, 5]"
        )
        self.assertEqual(
            swap_elements([1, 2, 3], 5), [1, 2, 3],
            msg="Failed for [1, 2, 3] with k=5, expected [1, 2, 3]"
        )
        self.assertEqual(
            swap_elements([], 1), [],
            msg="Failed for empty array with k=1, expected []"
        )
        self.assertEqual(
            swap_elements([1], 1), [1],
            msg="Failed for [1] with k=1, expected [1]"
        )
        self.assertEqual(
            swap_elements([1, 2, 3, 4], 1), [2, 1, 4, 3],
            msg="Failed for [1, 2, 3, 4] with k=1, expected [2, 1, 4, 3]"
        )
        self.assertEqual(
            swap_elements([-1, -2, -3], 1), [-2, -1, -3],
            msg="Failed for [-1, -2, -3] with k=1, expected [-2, -1, -3]"
        )
        self.assertEqual(
            swap_elements([0, 1, 0], 1), [1, 0, 0],
            msg="Failed for [0, 1, 0] with k=1, expected [1, 0, 0]"
        )

    def test_count_subarrays_with_sum(self):
        """Test count_subarrays_with_sum function."""
        self.assertEqual(
            count_subarrays_with_sum([1, 2, 3, -2], 3), 2,
            msg="Failed for [1, 2, 3, -2] with sum 3, expected 2"
        )
        self.assertEqual(
            count_subarrays_with_sum([1, 2, 3], 10), 0,
            msg="Failed for [1, 2, 3] with sum 10, expected 0"
        )
        self.assertEqual(
            count_subarrays_with_sum([], 0), 0,
            msg="Failed for empty array with sum 0, expected 0"
        )
        self.assertEqual(
            count_subarrays_with_sum([0, 0], 0), 3,
            msg="Failed for [0, 0] with sum 0, expected 3"
        )
        self.assertEqual(
            count_subarrays_with_sum([1], 1), 1,
            msg="Failed for [1] with sum 1, expected 1"
        )

    def test_interleave_arrays(self):
        """Test interleave_arrays function."""
        self.assertEqual(
            interleave_arrays([1, 3, 5], [2, 4]), [1, 2, 3, 4, 5],
            msg="Failed to interleave [1, 3, 5] and [2, 4], expected [1, 2, 3, 4, 5]"
        )
        self.assertEqual(
            interleave_arrays([1], [2, 3, 4]), [1, 2, 3, 4],
            msg="Failed for [1] and [2, 3, 4], expected [1, 2, 3, 4]"
        )
        self.assertEqual(
            interleave_arrays([], []), [],
            msg="Failed for two empty arrays, expected []"
        )
        self.assertEqual(
            interleave_arrays([1, 2], [3]), [1, 3, 2],
            msg="Failed for [1, 2] and [3], expected [1, 3, 2]"
        )
        self.assertEqual(
            interleave_arrays([0, 0], [1, 1]), [0, 1, 0, 1],
            msg="Failed for [0, 0] and [1, 1], expected [0, 1, 0, 1]"
        )

    def test_find_most_frequent(self):
        """Test find_most_frequent function."""
        self.assertEqual(
            find_most_frequent([1, 2, 2, 3, 1]), 2,
            msg="Failed for [1, 2, 2, 3, 1], expected 2"
        )
        self.assertEqual(
            find_most_frequent([1]), 1,
            msg="Failed for single-element array [1], expected 1"
        )
        self.assertEqual(
            find_most_frequent([]), None,
            msg="Failed for empty array, expected None"
        )
        self.assertEqual(
            find_most_frequent([1, 1, 2, 2]), 1,
            msg="Failed for [1, 1, 2, 2], expected 1"
        )
        self.assertEqual(
            find_most_frequent([-1, -1, 0]), -1,
            msg="Failed for [-1, -1, 0], expected -1"
        )

    def test_find_all_subarrays_with_sum(self):
        """Test find_all_subarrays_with_sum function."""
        self.assertEqual(
            find_all_subarrays_with_sum([1, 2, 3, -2], 3), [(0, 1), (2, 2)],
            msg="Failed for [1, 2, 3, -2] with sum 3, expected [(0, 1), (2, 2)]"
        )
        self.assertEqual(
            find_all_subarrays_with_sum([1, 2, 3], 10), [],
            msg="Failed for [1, 2, 3] with sum 10, expected []"
        )
        self.assertEqual(
            find_all_subarrays_with_sum([], 0), [],
            msg="Failed for empty array with sum 0, expected []"
        )
        self.assertEqual(
            find_all_subarrays_with_sum([0, 0, 0], 0), [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)],
            msg="Failed for [0, 0, 0] with sum 0, expected [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]"
        )
        self.assertEqual(
            find_all_subarrays_with_sum([-1, 1, 0, 2], 0), [(0, 1), (2, 2)],
            msg="Failed for [-1, 1, 0, 2] with sum 0, expected [(0, 1), (2, 2)]"
        )

    def test_merge_three_arrays(self):
        """Test merge_three_arrays function."""
        self.assertEqual(
            merge_three_arrays([1, 4], [2, 5], [3, 6]), [1, 2, 3, 4, 5, 6],
            msg="Failed to merge [1, 4], [2, 5], [3, 6], expected [1, 2, 3, 4, 5, 6]"
        )
        self.assertEqual(
            merge_three_arrays([1], [2], [3]), [1, 2, 3],
            msg="Failed to merge [1], [2], [3], expected [1, 2, 3]"
        )
        self.assertEqual(
            merge_three_arrays([], [1], [2]), [1, 2],
            msg="Failed to merge [], [1], [2], expected [1, 2]"
        )
        self.assertEqual(
            merge_three_arrays([1, 2], [], [3]), [1, 3, 2],
            msg="Failed to merge [1, 2], [], [3], expected [1, 3, 2]"
        )
        self.assertEqual(
            merge_three_arrays([1, 1], [2, 2], []), [1, 2, 1, 2],
            msg="Failed to merge [1, 1], [2, 2], [], expected [1, 2, 1, 2]"
        )

    def test_max_sum_alternate_elements(self):
        """Test max_sum_alternate_elements function."""
        self.assertEqual(
            max_sum_alternate_elements([1, 2, 3, 4, 5]), 9,
            msg="Failed for [1, 2, 3, 4, 5], expected 9"
        )
        self.assertEqual(
            max_sum_alternate_elements([1]), 1,
            msg="Failed for single-element array [1], expected 1"
        )
        self.assertEqual(
            max_sum_alternate_elements([]), 0,
            msg="Failed for empty array, expected 0"
        )
        self.assertEqual(
            max_sum_alternate_elements([-1, -2, -3, -4]), -4,
            msg="Failed for [-1, -2, -3, -4], expected -4"
        )
        self.assertEqual(
            max_sum_alternate_elements([2, 2, 2, 2]), 4,
            msg="Failed for [2, 2, 2, 2], expected 4"
        )

    def test_find_triplets_with_sum(self):
        """Test find_triplets_with_sum function."""
        self.assertEqual(
            find_triplets_with_sum([1, 2, 3, 4, 5, 7], 12), [(2, 3, 7)],
            msg="Failed for [1, 2, 3, 4, 5, 7] with sum 12, expected [(2, 3, 7)]"
        )
        self.assertEqual(
            find_triplets_with_sum([1, 2, 3], 12), [],
            msg="Failed for [1, 2, 3] with sum 12, expected []"
        )
        self.assertEqual(
            find_triplets_with_sum([], 0), [],
            msg="Failed for empty array with sum 0, expected []"
        )
        self.assertEqual(
            find_triplets_with_sum([0, 0, 0], 0), [(0, 0, 0)],
            msg="Failed for [0, 0, 0] with sum 0, expected [(0, 0, 0)]"
        )
        self.assertEqual(
            find_triplets_with_sum([-1, 1, 0, 2], 2), [(-1, 1, 2)],
            msg="Failed for [-1, 1, 0, 2] with sum 2, expected [(-1, 1, 2)]"
        )

    def test_segregate_even_odd(self):
        """Test segregate_even_odd function."""
        self.assertEqual(
            segregate_even_odd([1, 2, 3, 4, 6]), [2, 4, 6, 1, 3],
            msg="Failed to segregate [1, 2, 3, 4, 6], expected [2, 4, 6, 1, 3]"
        )
        self.assertEqual(
            segregate_even_odd([1, 3, 5]), [1, 3, 5],
            msg="Failed for [1, 3, 5], expected [1, 3, 5]"
        )
        self.assertEqual(
            segregate_even_odd([]), [],
            msg="Failed for empty array, expected []"
        )
        self.assertEqual(
            segregate_even_odd([2, 4, 6]), [2, 4, 6],
            msg="Failed for [2, 4, 6], expected [2, 4, 6]"
        )
        self.assertEqual(
            segregate_even_odd([1, 1, 2, 2]), [2, 2, 1, 1],
            msg="Failed for [1, 1, 2, 2], expected [2, 2, 1, 1]"
        )

    def test_find_k_largest_pairs(self):
        """Test find_k_largest_pairs function."""
        self.assertEqual(
            find_k_largest_pairs([1, 2, 3], [4, 5], 3), [(3, 5), (3, 4), (2, 5)],
            msg="Failed for [1, 2, 3], [4, 5], k=3, expected [(3, 5), (3, 4), (2, 5)]"
        )
        self.assertEqual(
            find_k_largest_pairs([1], [2], 2), [(1, 2)],
            msg="Failed for [1], [2], k=2, expected [(1, 2)]"
        )
        self.assertEqual(
            find_k_largest_pairs([], [1], 1), [],
            msg="Failed for [], [1], k=1, expected []"
        )
        self.assertEqual(
            find_k_largest_pairs([1, 1], [2, 2], 2), [(1, 2), (1, 2)],
            msg="Failed for [1, 1], [2, 2], k=2, expected [(1, 2), (1, 2)]"
        )
        self.assertEqual(
            find_k_largest_pairs([-1, 0], [1, 2], 2), [(0, 2), (0, 1)],
            msg="Failed for [-1, 0], [1, 2], k=2, expected [(0, 2), (0, 1)]"
        )

    def test_replace_with_next_greater(self):
        """Test replace_with_next_greater function."""
        self.assertEqual(
            replace_with_next_greater([1, 3, 2, 4]), [3, 4, 4, -1],
            msg="Failed for [1, 3, 2, 4], expected [3, 4, 4, -1]"
        )
        self.assertEqual(
            replace_with_next_greater([5, 4, 3]), [-1, -1, -1],
            msg="Failed for [5, 4, 3], expected [-1, -1, -1]"
        )
        self.assertEqual(
            replace_with_next_greater([]), [],
            msg="Failed for empty array, expected []"
        )
        self.assertEqual(
            replace_with_next_greater([1]), [-1],
            msg="Failed for [1], expected [-1]"
        )
        self.assertEqual(
            replace_with_next_greater([2, 2, 2]), [-1, -1, -1],
            msg="Failed for [2, 2, 2], expected [-1, -1, -1]"
        )

    def test_find_subarray_max_min_diff(self):
        """Test find_subarray_max_min_diff function."""
        self.assertEqual(
            find_subarray_max_min_diff([1, 2, 3, 4, 5], 3), (0, 2),
            msg="Failed for [1, 2, 3, 4, 5], k=3, expected (0, 2)"
        )
        self.assertEqual(
            find_subarray_max_min_diff([1, 2], 3), (-1, -1),
            msg="Failed for [1, 2], k=3, expected (-1, -1)"
        )
        self.assertEqual(
            find_subarray_max_min_diff([], 1), (-1, -1),
            msg="Failed for empty array, k=1, expected (-1, -1)"
        )
        self.assertEqual(
            find_subarray_max_min_diff([5, 5, 5], 2), (0, 1),
            msg="Failed for [5, 5, 5], k=2, expected (0, 1)"
        )
        self.assertEqual(
            find_subarray_max_min_diff([-1, 0, 2, -2], 2), (0, 1),
            msg="Failed for [-1, 0, 2, -2], k=2, expected (0, 1)"
        )

    def test_find_missing_and_repeated(self):
        """Test find_missing_and_repeated function."""
        self.assertEqual(
            find_missing_and_repeated([1, 2, 2, 4]), (3, 2),
            msg="Failed for [1, 2, 2, 4], expected (3, 2)"
        )
        self.assertEqual(
            find_missing_and_repeated([3, 1, 3]), (2, 3),
            msg="Failed for [3, 1, 3], expected (2, 3)"
        )
        self.assertEqual(
            find_missing_and_repeated([1, 1]), (2, 1),
            msg="Failed for [1, 1], expected (2, 1)"
        )
        self.assertEqual(
            find_missing_and_repeated([2, 2, 2, 2]), (1, 2),
            msg="Failed for [2, 2, 2, 2], expected (1, 2)"
        )
        self.assertEqual(
            find_missing_and_repeated([1, 2, 3, 3]), (4, 3),
            msg="Failed for [1, 2, 3, 3], expected (4, 3)"
        )

    def test_zigzag_array(self):
        """Test zigzag_array function."""
        self.assertEqual(
            zigzag_array([1, 2, 3, 4]), [1, 3, 2, 4],
            msg="Failed for [1, 2, 3, 4], expected [1, 3, 2, 4]"
        )
        self.assertEqual(
            zigzag_array([5]), [5],
            msg="Failed for [5], expected [5]"
        )
        self.assertEqual(
            zigzag_array([]), [],
            msg="Failed for empty array, expected []"
        )
        self.assertEqual(
            zigzag_array([1, 1, 1]), [1, 1, 1],
            msg="Failed for [1, 1, 1], expected [1, 1, 1]"
        )
        self.assertEqual(
            zigzag_array([4, 3, 2, 1]), [3, 4, 1, 2],
            msg="Failed for [4, 3, 2, 1], expected [3, 4, 1, 2]"
        )

    def test_find_all_pairs_with_product(self):
        """Test find_all_pairs_with_product function."""
        self.assertEqual(
            find_all_pairs_with_product([2, 3, 4, 6], 12), [(2, 6), (3, 4)],
            msg="Failed for [2, 3, 4, 6] with product 12, expected [(2, 6), (3, 4)]"
        )
        self.assertEqual(
            find_all_pairs_with_product([1, 2, 3], 10), [],
            msg="Failed for [1, 2, 3] with product 10, expected []"
        )
        self.assertEqual(
            find_all_pairs_with_product([], 1), [],
            msg="Failed for empty array with product 1, expected []"
        )
        self.assertEqual(
            find_all_pairs_with_product([-2, -6, 2, 3], 12), [(-2, -6), (2, 6)],
            msg="Failed for [-2, -6, 2, 3] with product 12, expected [(-2, -6), (2, 6)]"
        )
        self.assertEqual(
            find_all_pairs_with_product([0, 0, 1], 0), [(0, 0), (0, 1)],
            msg="Failed for [0, 0, 1] with product 0, expected [(0, 0), (0, 1)]"
        )

    def test_interleave_with_reverse(self):
        """Test interleave_with_reverse function."""
        self.assertEqual(
            interleave_with_reverse([1, 3, 5], [2, 4, 6]), [1, 6, 3, 4, 5, 2],
            msg="Failed to interleave [1, 3, 5] and [2, 4, 6], expected [1, 6, 3, 4, 5, 2]"
        )
        self.assertEqual(
            interleave_with_reverse([1], [2, 3]), [1, 3, 2],
            msg="Failed for [1] and [2, 3], expected [1, 3, 2]"
        )
        self.assertEqual(
            interleave_with_reverse([], [1, 2]), [2, 1],
            msg="Failed for empty first array and [1, 2], expected [2, 1]"
        )
        self.assertEqual(
            interleave_with_reverse([1, 2], []), [1, 2],
            msg="Failed for [1, 2] and empty second array, expected [1, 2]"
        )
        self.assertEqual(
            interleave_with_reverse([1, 1], [2, 2, 2]), [1, 2, 1, 2, 2],
            msg="Failed for [1, 1] and [2, 2, 2], expected [1, 2, 1, 2, 2]"
        )

    def test_max_sum_subarray_length_k(self):
        """Test max_sum_subarray_length_k function."""
        self.assertEqual(
            max_sum_subarray_length_k([1, 2, 3, 4, 5], 3), 12,
            msg="Failed for [1, 2, 3, 4, 5] with k=3, expected 12"
        )
        self.assertEqual(
            max_sum_subarray_length_k([1, 2], 3), None,
            msg="Failed for [1, 2] with k=3, expected None"
        )
        self.assertEqual(
            max_sum_subarray_length_k([], 1), None,
            msg="Failed for empty array with k=1, expected None"
        )
        self.assertEqual(
            max_sum_subarray_length_k([-1, -2, -3], 2), -3,
            msg="Failed for [-1, -2, -3] with k=2, expected -3"
        )
        self.assertEqual(
            max_sum_subarray_length_k([1, 1, 1], 2), 2,
            msg="Failed for [1, 1, 1] with k=2, expected 2"
        )

    def test_find_elements_with_sum(self):
        """Test find_elements_with_sum function."""
        self.assertEqual(
            find_elements_with_sum([1, 2, 3], [4, 5, 6], 7), [(1, 6), (2, 5), (3, 4)],
            msg="Failed for [1, 2, 3] and [4, 5, 6] with sum 7, expected [(1, 6), (2, 5), (3, 4)]"
        )
        self.assertEqual(
            find_elements_with_sum([1, 2], [3, 4], 10), [],
            msg="Failed for [1, 2] and [3, 4] with sum 10, expected []"
        )
        self.assertEqual(
            find_elements_with_sum([], [1, 2], 3), [],
            msg="Failed for empty first array and [1, 2] with sum 3, expected []"
        )
        self.assertEqual(
            find_elements_with_sum([-1, 0], [1, 2], 1), [(-1, 2), (0, 1)],
            msg="Failed for [-1, 0] and [1, 2] with sum 1, expected [(-1, 2), (0, 1)]"
        )
        self.assertEqual(
            find_elements_with_sum([1, 1], [1, 1], 2), [(1, 1), (1, 1)],
            msg="Failed for [1, 1] and [1, 1] with sum 2, expected [(1, 1), (1, 1)]"
        )


    def test_find_k_smallest_sums(self):
        """Test find_k_smallest_sums function."""
        self.assertEqual(
            find_k_smallest_sums([1, 2], [3, 4], 3), [4, 5, 6],
            msg="Failed for [1, 2] and [3, 4] with k=3, expected [4, 5, 6]"
        )
        self.assertEqual(
            find_k_smallest_sums([1], [2], 2), [3],
            msg="Failed for [1] and [2] with k=2, expected [3]"
        )
        self.assertEqual(
            find_k_smallest_sums([], [1], 1), [],
            msg="Failed for empty first array and [1] with k=1, expected []"
        )
        self.assertEqual(
            find_k_smallest_sums([-1, 0], [1, 2], 2), [-1, 0],
            msg="Failed for [-1, 0] and [1, 2] with k=2, expected [-1, 0]"
        )
        self.assertEqual(
            find_k_smallest_sums([1, 1], [1, 1], 2), [2, 2],
            msg="Failed for [1, 1] and [1, 1] with k=2, expected [2, 2]"
        )

    def test_replace_with_previous_smaller(self):
        """Test replace_with_previous_smaller function."""
        self.assertEqual(
            replace_with_previous_smaller([3, 1, 4, 2]), [-1, -1, 1, 1],
            msg="Failed for [3, 1, 4, 2], expected [-1, -1, 1, 1]"
        )
        self.assertEqual(
            replace_with_previous_smaller([1, 2, 3]), [-1, 1, 2],
            msg="Failed for [1, 2, 3], expected [-1, 1, 2]"
        )
        self.assertEqual(
            replace_with_previous_smaller([]), [],
            msg="Failed for empty array, expected []"
        )
        self.assertEqual(
            replace_with_previous_smaller([5]), [-1],
            msg="Failed for [5], expected [-1]"
        )
        self.assertEqual(
            replace_with_previous_smaller([2, 2, 2]), [-1, -1, -1],
            msg="Failed for [2, 2, 2], expected [-1, -1, -1]"
        )

    def test_find_subarray_with_median(self):
        """Test find_subarray_with_median function."""
        self.assertEqual(
            find_subarray_with_median([1, 2, 3, 4, 5], 3, 3), (0, 2),
            msg="Failed for [1, 2, 3, 4, 5] with k=3, median=3, expected (0, 2)"
        )
        self.assertEqual(
            find_subarray_with_median([1, 2], 3, 1), (-1, -1),
            msg="Failed for [1, 2] with k=3, median=1, expected (-1, -1)"
        )
        self.assertEqual(
            find_subarray_with_median([], 1, 0), (-1, -1),
            msg="Failed for empty array with k=1, median=0, expected (-1, -1)"
        )
        self.assertEqual(
            find_subarray_with_median([2, 2, 2], 3, 2), (0, 2),
            msg="Failed for [2, 2, 2] with k=3, median=2, expected (0, 2)"
        )
        self.assertEqual(
            find_subarray_with_median([-1, 0, 1, 2], 3, 0), (0, 2),
            msg="Failed for [-1, 0, 1, 2] with k=3, median=0, expected (0, 2)"
        )

    def test_count_distinct_in_window(self):
        """Test count_distinct_in_window function."""
        self.assertEqual(
            count_distinct_in_window([1, 2, 1, 3, 4], 3), [3, 3, 3],
            msg="Failed for [1, 2, 1, 3, 4] with k=3, expected [3, 3, 3]"
        )
        self.assertEqual(
            count_distinct_in_window([1, 1], 2), [1],
            msg="Failed for [1, 1] with k=2, expected [1]"
        )
        self.assertEqual(
            count_distinct_in_window([], 1), [],
            msg="Failed for empty array with k=1, expected []"
        )
        self.assertEqual(
            count_distinct_in_window([1, 1, 1], 2), [1, 1],
            msg="Failed for [1, 1, 1] with k=2, expected [1, 1]"
        )
        self.assertEqual(
            count_distinct_in_window([1, 2, 3], 4), [],
            msg="Failed for [1, 2, 3] with k=4, expected []"
        )

    def test_find_maximum_in_each_window(self):
        """Test find_maximum_in_each_window function."""
        self.assertEqual(
            find_maximum_in_each_window([1, 3, 5, 2, 4], 3), [5, 5, 5],
            msg="Failed for [1, 3, 5, 2, 4] with k=3, expected [5, 5, 5]"
        )
        self.assertEqual(
            find_maximum_in_each_window([1], 1), [1],
            msg="Failed for [1] with k=1, expected [1]"
        )
        self.assertEqual(
            find_maximum_in_each_window([], 1), [],
            msg="Failed for empty array with k=1, expected []"
        )
        self.assertEqual(
            find_maximum_in_each_window([-1, -2, -3], 2), [-1, -2],
            msg="Failed for [-1, -2, -3] with k=2, expected [-1, -2]"
        )
        self.assertEqual(
            find_maximum_in_each_window([2, 2, 2], 2), [2, 2],
            msg="Failed for [2, 2, 2] with k=2, expected [2, 2]"
        )

    def test_find_subarrays_with_k_distinct(self):
        """Test find_subarrays_with_k_distinct function."""
        self.assertEqual(
            find_subarrays_with_k_distinct([1, 2, 1, 3], 2), [(0, 1), (0, 2), (1, 3), (2, 3)],
            msg="Failed for [1, 2, 1, 3] with k=2, expected [(0, 1), (0, 2), (1, 3), (2, 3)]"
        )
        self.assertEqual(
            find_subarrays_with_k_distinct([1, 1, 1], 2), [],
            msg="Failed for [1, 1, 1] with k=2, expected []"
        )
        self.assertEqual(
            find_subarrays_with_k_distinct([], 1), [],
            msg="Failed for empty array with k=1, expected []"
        )
        self.assertEqual(
            find_subarrays_with_k_distinct([1, 2, 2, 3], 3), [(0, 3)],
            msg="Failed for [1, 2, 2, 3] with k=3, expected [(0, 3)]"
        )
        self.assertEqual(
            find_subarrays_with_k_distinct([-1, -1, 0], 2), [(0, 2), (1, 2)],
            msg="Failed for [-1, -1, 0] with k=2, expected [(0, 2), (1, 2)]"
        )

    def test_merge_arrays_with_sum(self):
        """Test merge_arrays_with_sum function."""
        self.assertEqual(
            merge_arrays_with_sum([1, 2, 3], [4, 5, 6], 7), [1, 6, 2, 5, 3, 4],
            msg="Failed for [1, 2, 3], [4, 5, 6] with sum 7, expected [1, 6, 2, 5, 3, 4]"
        )
        self.assertEqual(
            merge_arrays_with_sum([1, 2], [3, 4], 10), [],
            msg="Failed for [1, 2], [3, 4] with sum 10, expected []"
        )
        self.assertEqual(
            merge_arrays_with_sum([], [1, 2], 3), [],
            msg="Failed for empty first array, [1, 2] with sum 3, expected []"
        )
        self.assertEqual(
            merge_arrays_with_sum([-1, 0], [1, 2], 1), [-1, 2, 0, 1],
            msg="Failed for [-1, 0], [1, 2] with sum 1, expected [-1, 2, 0, 1]"
        )
        self.assertEqual(
            merge_arrays_with_sum([1, 1], [1, 1], 2), [1, 1, 1, 1],
            msg="Failed for [1, 1], [1, 1] with sum 2, expected [1, 1, 1, 1]"
        )

    def test_max_product_subarray_length_k(self):
        """Test max_product_subarray_length_k function."""
        self.assertEqual(
            max_product_subarray_length_k([1, 2, 3, 4], 2), 12,
            msg="Failed for [1, 2, 3, 4] with k=2, expected 12"
        )
        self.assertEqual(
            max_product_subarray_length_k([1, 2], 3), None,
            msg="Failed for [1, 2] with k=3, expected None"
        )
        self.assertEqual(
            max_product_subarray_length_k([], 1), None,
            msg="Failed for empty array with k=1, expected None"
        )
        self.assertEqual(
            max_product_subarray_length_k([-2, -3, -4], 2), 12,
            msg="Failed for [-2, -3, -4] with k=2, expected 12"
        )
        self.assertEqual(
            max_product_subarray_length_k([0, 1, 0], 2), 0,
            msg="Failed for [0, 1, 0] with k=2, expected 0"
        )

    def test_find_elements_with_product(self):
        """Test find_elements_with_product function."""
        self.assertEqual(
            find_elements_with_product([1, 2, 3], [4, 6, 8], 12), [(2, 6), (3, 4)],
            msg="Failed for [1, 2, 3], [4, 6, 8] with product 12, expected [(2, 6), (3, 4)]"
        )
        self.assertEqual(
            find_elements_with_product([1, 2], [3, 4], 10), [],
            msg="Failed for [1, 2], [3, 4] with product 10, expected []"
        )
        self.assertEqual(
            find_elements_with_product([], [1, 2], 2), [],
            msg="Failed for empty first array, [1, 2] with product 2, expected []"
        )
        self.assertEqual(
            find_elements_with_product([-2, 3], [-6, 4], 12), [(-2, -6), (3, 4)],
            msg="Failed for [-2, 3], [-6, 4] with product 12, expected [(-2, -6), (3, 4)]"
        )
        self.assertEqual(
            find_elements_with_product([0, 1], [0, 2], 0), [(0, 0), (0, 2)],
            msg="Failed for [0, 1], [0, 2] with product 0, expected [(0, 0), (0, 2)]"
        )

    def test_rearrange_alternate_high_low(self):
        """Test rearrange_alternate_high_low function."""
        self.assertEqual(
            rearrange_alternate_high_low([1, 2, 3, 4]), [4, 1, 3, 2],
            msg="Failed for [1, 2, 3, 4], expected [4, 1, 3, 2]"
        )
        self.assertEqual(
            rearrange_alternate_high_low([1]), [1],
            msg="Failed for [1], expected [1]"
        )
        self.assertEqual(
            rearrange_alternate_high_low([]), [],
            msg="Failed for empty array, expected []"
        )
        self.assertEqual(
            rearrange_alternate_high_low([5, 5, 5]), [5, 5, 5],
            msg="Failed for [5, 5, 5], expected [5, 5, 5]"
        )
        self.assertEqual(
            rearrange_alternate_high_low([-1, 0, 1, 2]), [2, -1, 1, 0],
            msg="Failed for [-1, 0, 1, 2], expected [2, -1, 1, 0]"
        )

    def test_count_pairs_with_diff_k(self):
        """Test count_pairs_with_diff_k function."""
        self.assertEqual(
            count_pairs_with_diff_k([1, 2, 3, 4], 1), 3,
            msg="Failed for [1, 2, 3, 4] with k=1, expected 3"
        )
        self.assertEqual(
            count_pairs_with_diff_k([1, 2], 2), 0,
            msg="Failed for [1, 2] with k=2, expected 0"
        )
        self.assertEqual(
            count_pairs_with_diff_k([], 1), 0,
            msg="Failed for empty array with k=1, expected 0"
        )
        self.assertEqual(
            count_pairs_with_diff_k([-1, 1, -2, 2], 3), 4,
            msg="Failed for [-1, 1, -2, 2] with k=3, expected 4"
        )
        self.assertEqual(
            count_pairs_with_diff_k([1, 1, 1], 0), 3,
            msg="Failed for [1, 1, 1] with k=0, expected 3"
        )

    def test_replace_with_nearest_larger(self):
        """Test replace_with_nearest_larger function."""
        self.assertEqual(
            replace_with_nearest_larger([1, 3, 2, 4]), [3, 4, 4, -1],
            msg="Failed for [1, 3, 2, 4], expected [3, 4, 4, -1]"
        )
        self.assertEqual(
            replace_with_nearest_larger([5, 4, 3]), [-1, -1, -1],
            msg="Failed for [5, 4, 3], expected [-1, -1, -1]"
        )
        self.assertEqual(
            replace_with_nearest_larger([]), [],
            msg="Failed for empty array, expected []"
        )
        self.assertEqual(
            replace_with_nearest_larger([1]), [-1],
            msg="Failed for [1], expected [-1]"
        )
        self.assertEqual(
            replace_with_nearest_larger([2, 2, 2]), [-1, -1, -1],
            msg="Failed for [2, 2, 2], expected [-1, -1, -1]"
        )

    def test_find_subarray_with_sum_range(self):
        """Test find_subarray_with_sum_range function."""
        self.assertEqual(
            find_subarray_with_sum_range([1, 2, 3, 4], 5, 7), (0, 2),
            msg="Failed for [1, 2, 3, 4] with min_sum=5, max_sum=7, expected (0, 2)"
        )
        self.assertEqual(
            find_subarray_with_sum_range([1, 2], 10, 12), (-1, -1),
            msg="Failed for [1, 2] with min_sum=10, max_sum=12, expected (-1, -1)"
        )
        self.assertEqual(
            find_subarray_with_sum_range([], 1, 2), (-1, -1),
            msg="Failed for empty array with min_sum=1, max_sum=2, expected (-1, -1)"
        )
        self.assertEqual(
            find_subarray_with_sum_range([-1, 0, 1], 0, 1), (1, 2),
            msg="Failed for [-1, 0, 1] with min_sum=0, max_sum=1, expected (1, 2)"
        )
        self.assertEqual(
            find_subarray_with_sum_range([2, 2, 2], 4, 4), (0, 1),
            msg="Failed for [2, 2, 2] with min_sum=4, max_sum=4, expected (0, 1)"
        )

    def test_count_subarrays_with_product_less_k(self):
        """Test count_subarrays_with_product_less_k function."""
        self.assertEqual(
            count_subarrays_with_product_less_k([1, 2, 3, 4], 10), 4,
            msg="Failed for [1, 2, 3, 4] with k=10, expected 4"
        )
        self.assertEqual(
            count_subarrays_with_product_less_k([1, 2], 1), 0,
            msg="Failed for [1, 2] with k=1, expected 0"
        )
        self.assertEqual(
            count_subarrays_with_product_less_k([], 1), 0,
            msg="Failed for empty array with k=1, expected 0"
        )
        self.assertEqual(
            count_subarrays_with_product_less_k([2, 2], 4), 2,
            msg="Failed for [2, 2] with k=4, expected 2"
        )
        self.assertEqual(
            count_subarrays_with_product_less_k([1, 1, 1], 2), 3,
            msg="Failed for [1, 1, 1] with k=2, expected 3"
        )

    def test_find_min_difference_in_windows(self):
        """Test find_min_difference_in_windows function."""
        self.assertEqual(
            find_min_difference_in_windows([1, 3, 5, 2], 3), [2, 3],
            msg="Failed for [1, 3, 5, 2] with k=3, expected [2, 3]"
        )
        self.assertEqual(
            find_min_difference_in_windows([1], 1), [0],
            msg="Failed for [1] with k=1, expected [0]"
        )
        self.assertEqual(
            find_min_difference_in_windows([], 1), [],
            msg="Failed for empty array with k=1, expected []"
        )
        self.assertEqual(
            find_min_difference_in_windows([-1, -2, -3], 2), [1, 1],
            msg="Failed for [-1, -2, -3] with k=2, expected [1, 1]"
        )
        self.assertEqual(
            find_min_difference_in_windows([2, 2, 2], 2), [0, 0],
            msg="Failed for [2, 2, 2] with k=2, expected [0, 0]"
        )

    def test_find_subarrays_with_k_pairs_sum(self):
        """Test find_subarrays_with_k_pairs_sum function."""
        self.assertEqual(
            find_subarrays_with_k_pairs_sum([1, 2, 3, 4, 2, 5], 2, 5), [(0, 3), (1, 4)],
            msg="Failed for [1, 2, 3, 4, 2, 5] with k=2, target_sum=5, expected [(0, 3), (1, 4)]"
        )
        self.assertEqual(
            find_subarrays_with_k_pairs_sum([1, 2, 3], 1, 10), [],
            msg="Failed for [1, 2, 3] with k=1, target_sum=10, expected []"
        )
        self.assertEqual(
            find_subarrays_with_k_pairs_sum([], 1, 1), [],
            msg="Failed for empty array with k=1, target_sum=1, expected []"
        )
        self.assertEqual(
            find_subarrays_with_k_pairs_sum([-1, 1, -1, 1], 2, 0), [(0, 3)],
            msg="Failed for [-1, 1, -1, 1] with k=2, target_sum=0, expected [(0, 3)]"
        )
        self.assertEqual(
            find_subarrays_with_k_pairs_sum([2, 2, 2, 2], 1, 4), [(0, 1), (1, 2), (2, 3)],
            msg="Failed for [2, 2, 2, 2] with k=1, target_sum=4, expected [(0, 1), (1, 2), (2, 3)]"
        )

    def test_merge_four_arrays_alternate(self):
        """Test merge_four_arrays_alternate function."""
        self.assertEqual(
            merge_four_arrays_alternate([1, 5], [2, 6], [3, 7], [4, 8]), [1, 2, 3, 4, 5, 6, 7, 8],
            msg="Failed for [1, 5], [2, 6], [3, 7], [4, 8], expected [1, 2, 3, 4, 5, 6, 7, 8]"
        )
        self.assertEqual(
            merge_four_arrays_alternate([1], [2], [3], [4]), [1, 2, 3, 4],
            msg="Failed for [1], [2], [3], [4], expected [1, 2, 3, 4]"
        )
        self.assertEqual(
            merge_four_arrays_alternate([], [1], [2], [3]), [],
            msg="Failed for [], [1], [2], [3], expected []"
        )
        self.assertEqual(
            merge_four_arrays_alternate([-1, -2], [1], [2], [3]), [-1, 1, 2, 3],
            msg="Failed for [-1, -2], [1], [2], [3], expected [-1, 1, 2, 3]"
        )
        self.assertEqual(
            merge_four_arrays_alternate([1, 1], [2, 2], [3, 3], []), [],
            msg="Failed for [1, 1], [2, 2], [3, 3], [], expected []"
        )

    def test_max_sum_subarray_with_min_k(self):
        """Test max_sum_subarray_with_min_k function."""
        self.assertEqual(
            max_sum_subarray_with_min_k([1, 2, 3, -1, 4], 3), 9,
            msg="Failed for [1, 2, 3, -1, 4] with k=3, expected 9"
        )
        self.assertEqual(
            max_sum_subarray_with_min_k([1, 2], 3), None,
            msg="Failed for [1, 2] with k=3, expected None"
        )
        self.assertEqual(
            max_sum_subarray_with_min_k([], 1), None,
            msg="Failed for empty array with k=1, expected None"
        )
        self.assertEqual(
            max_sum_subarray_with_min_k([-1, -2, -3, -4], 2), -3,
            msg="Failed for [-1, -2, -3, -4] with k=2, expected -3"
        )
        self.assertEqual(
            max_sum_subarray_with_min_k([0, 0, 0, 0], 2), 0,
            msg="Failed for [0, 0, 0, 0] with k=2, expected 0"
        )

    def test_find_triplets_with_product(self):
        """Test find_triplets_with_product function."""
        self.assertEqual(
            find_triplets_with_product([1, 2, 3, 4, 6], 24), [(1, 4, 6), (2, 3, 4)],
            msg="Failed for [1, 2, 3, 4, 6] with target_product=24, expected [(1, 4, 6), (2, 3, 4)]"
        )
        self.assertEqual(
            find_triplets_with_product([1, 2, 3], 50), [],
            msg="Failed for [1, 2, 3] with target_product=50, expected []"
        )
        self.assertEqual(
            find_triplets_with_product([], 1), [],
            msg="Failed for empty array with target_product=1, expected []"
        )
        self.assertEqual(
            find_triplets_with_product([-2, -3, 2, 3], -12), [(-2, 2, 3), (-3, 2, 2)],
            msg="Failed for [-2, -3, 2, 3] with target_product=-12, expected [(-2, 2, 3), (-3, 2, 2)]"
        )
        self.assertEqual(
            find_triplets_with_product([0, 1, 0], 0), [(0, 0, 1), (0, 1, 0)],
            msg="Failed for [0, 1, 0] with target_product=0, expected [(0, 0, 1), (0, 1, 0)]"
        )

    def test_segregate_by_frequency(self):
        """Test segregate_by_frequency function."""
        self.assertEqual(
            segregate_by_frequency([1, 2, 2, 3, 1, 3]), [1, 1, 2, 2, 3, 3],
            msg="Failed for [1, 2, 2, 3, 1, 3], expected [1, 1, 2, 2, 3, 3]"
        )
        self.assertEqual(
            segregate_by_frequency([1, 1, 1]), [1, 1, 1],
            msg="Failed for [1, 1, 1], expected [1, 1, 1]"
        )
        self.assertEqual(
            segregate_by_frequency([]), [],
            msg="Failed for empty array, expected []"
        )
        self.assertEqual(
            segregate_by_frequency([-1, -1, 0, 0, 0]), [0, 0, 0, -1, -1],
            msg="Failed for [-1, -1, 0, 0, 0], expected [0, 0, 0, -1, -1]"
        )
        self.assertEqual(
            segregate_by_frequency([1, 2, 3]), [1, 2, 3],
            msg="Failed for [1, 2, 3], expected [1, 2, 3]"
        )

    def test_find_k_largest_triplets(self):
        """Test find_k_largest_triplets function."""
        self.assertEqual(
            find_k_largest_triplets([1, 2], [3, 4], [5, 6], 2), [(2, 4, 6), (2, 4, 5)],
            msg="Failed for [1, 2], [3, 4], [5, 6] with k=2, expected [(2, 4, 6), (2, 4, 5)]"
        )
        self.assertEqual(
            find_k_largest_triplets([1], [2], [3], 2), [(1, 2, 3)],
            msg="Failed for [1], [2], [3] with k=2, expected [(1, 2, 3)]"
        )
        self.assertEqual(
            find_k_largest_triplets([], [1], [2], 1), [],
            msg="Failed for [], [1], [2] with k=1, expected []"
        )
        self.assertEqual(
            find_k_largest_triplets([-1, 0], [1, 2], [3], 2), [(0, 2, 3), (0, 1, 3)],
            msg="Failed for [-1, 0], [1, 2], [3] with k=2, expected [(0, 2, 3), (0, 1, 3)]"
        )
        self.assertEqual(
            find_k_largest_triplets([1, 1], [2, 2], [3, 3], 2), [(1, 2, 3), (1, 2, 3)],
            msg="Failed for [1, 1], [2, 2], [3, 3] with k=2, expected [(1, 2, 3), (1, 2, 3)]"
        )

    def test_replace_with_closest_smaller(self):
        """Test replace_with_closest_smaller function."""
        self.assertEqual(
            replace_with_closest_smaller([3, 1, 4, 2, 5]), [-1, -1, 1, 1, 2],
            msg="Failed for [3, 1, 4, 2, 5], expected [-1, -1, 1, 1, 2]"
        )
        self.assertEqual(
            replace_with_closest_smaller([5, 4, 3]), [-1, -1, -1],
            msg="Failed for [5, 4, 3], expected [-1, -1, -1]"
        )
        self.assertEqual(
            replace_with_closest_smaller([]), [],
            msg="Failed for empty array, expected []"
        )
        self.assertEqual(
            replace_with_closest_smaller([1]), [-1],
            msg="Failed for [1], expected [-1]"
        )
        self.assertEqual(
            replace_with_closest_smaller([2, 2, 2]), [-1, -1, -1],
            msg="Failed for [2, 2, 2], expected [-1, -1, -1]"
        )

    def test_find_subarray_with_k_median(self):
        """Test find_subarray_with_k_median function."""
        self.assertEqual(
            find_subarray_with_k_median([1, 2, 3, 4, 5], 3, 3), (0, 2),
            msg="Failed for [1, 2, 3, 4, 5] with k=3, median=3, expected (0, 2)"
        )
        self.assertEqual(
            find_subarray_with_k_median([1, 2], 3, 1), (-1, -1),
            msg="Failed for [1, 2] with k=3, median=1, expected (-1, -1)"
        )
        self.assertEqual(
            find_subarray_with_k_median([], 1, 0), (-1, -1),
            msg="Failed for empty array with k=1, median=0, expected (-1, -1)"
        )
        self.assertEqual(
            find_subarray_with_k_median([2, 2, 2, 2], 4, 2), (0, 3),
            msg="Failed for [2, 2, 2, 2] with k=4, median=2, expected (0, 3)"
        )
        self.assertEqual(
            find_subarray_with_k_median([-1, 0, 1, 2], 3, 0), (0, 2),
            msg="Failed for [-1, 0, 1, 2] with k=3, median=0, expected (0, 2)"
        )

    def test_count_subarrays_with_sum_and_product(self):
        """Test count_subarrays_with_sum_and_product function."""
        self.assertEqual(
            count_subarrays_with_sum_and_product([1, 2, 3, 2], 5, 6), 2,
            msg="Failed for [1, 2, 3, 2] with target_sum=5, target_product=6, expected 2"
        )
        self.assertEqual(
            count_subarrays_with_sum_and_product([1, 2], 3, 10), 0,
            msg="Failed for [1, 2] with target_sum=3, target_product=10, expected 0"
        )
        self.assertEqual(
            count_subarrays_with_sum_and_product([], 0, 1), 0,
            msg="Failed for empty array with target_sum=0, target_product=1, expected 0"
        )
        self.assertEqual(
            count_subarrays_with_sum_and_product([-1, 1, 0], 0, 0), 1,
            msg="Failed for [-1, 1, 0] with target_sum=0, target_product=0, expected 1"
        )
        self.assertEqual(
            count_subarrays_with_sum_and_product([2, 2], 4, 4), 1,
            msg="Failed for [2, 2] with target_sum=4, target_product=4, expected 1"
        )

    def test_find_max_sum_in_windows_with_k_distinct(self):
        """Test find_max_sum_in_windows_with_k_distinct function."""
        self.assertEqual(
            find_max_sum_in_windows_with_k_distinct([1, 2, 1, 3, 4], 2, 3), [4, 6, 8],
            msg="Failed for [1, 2, 1, 3, 4] with k=2, window_size=3, expected [4, 6, 8]"
        )
        self.assertEqual(
            find_max_sum_in_windows_with_k_distinct([1, 1], 2, 2), [2],
            msg="Failed for [1, 1] with k=2, window_size=2, expected [2]"
        )
        self.assertEqual(
            find_max_sum_in_windows_with_k_distinct([], 1, 1), [],
            msg="Failed for empty array with k=1, window_size=1, expected []"
        )
        self.assertEqual(
            find_max_sum_in_windows_with_k_distinct([-1, -1, -2], 2, 2), [-2, -3],
            msg="Failed for [-1, -1, -2] with k=2, window_size=2, expected [-2, -3]"
        )
        self.assertEqual(
            find_max_sum_in_windows_with_k_distinct([1, 2, 3], 1, 3), [],
            msg="Failed for [1, 2, 3] with k=1, window_size=3, expected []"
        )

    def test_find_subarrays_with_k_triplets(self):
        """Test find_subarrays_with_k_triplets function."""
        self.assertEqual(
            find_subarrays_with_k_triplets([1, 2, 3, 4, 2, 3, 5], 2, 12), [(0, 5)],
            msg="Failed for [1, 2, 3, 4, 2, 3, 5] with k=2, target_sum=12, expected [(0, 5)]"
        )
        self.assertEqual(
            find_subarrays_with_k_triplets([1, 2, 3], 1, 20), [],
            msg="Failed for [1, 2, 3] with k=1, target_sum=20, expected []"
        )
        self.assertEqual(
            find_subarrays_with_k_triplets([], 1, 1), [],
            msg="Failed for empty array with k=1, target_sum=1, expected []"
        )
        self.assertEqual(
            find_subarrays_with_k_triplets([-1, 1, -1, 1, 0], 2, 0), [(0, 4)],
            msg="Failed for [-1, 1, -1, 1, 0] with k=2, target_sum=0, expected [(0, 4)]"
        )
        self.assertEqual(
            find_subarrays_with_k_triplets([2, 2, 2, 2], 1, 6), [(0, 2), (1, 3)],
            msg="Failed for [2, 2, 2, 2] with k=1, target_sum=6, expected [(0, 2), (1, 3)]"
        )

    def test_interleave_arrays_with_diff(self):
        """Test interleave_arrays_with_diff function."""
        self.assertEqual(
            interleave_arrays_with_diff([1, 2, 3], [4, 5, 6], 3), [1, 4, 2, 5, 3, 6],
            msg="Failed for [1, 2, 3], [4, 5, 6] with diff=3, expected [1, 4, 2, 5, 3, 6]"
        )
        self.assertEqual(
            interleave_arrays_with_diff([1, 2], [3, 4], 1), [],
            msg="Failed for [1, 2], [3, 4] with diff=1, expected []"
        )
        self.assertEqual(
            interleave_arrays_with_diff([], [1, 2], 1), [],
            msg="Failed for [], [1, 2] with diff=1, expected []"
        )
        self.assertEqual(
            interleave_arrays_with_diff([-1, 0], [2, 3], 3), [-1, 2, 0, 3],
            msg="Failed for [-1, 0], [2, 3] with diff=3, expected [-1, 2, 0, 3]"
        )
        self.assertEqual(
            interleave_arrays_with_diff([1, 1], [1, 1], 0), [1, 1, 1, 1],
            msg="Failed for [1, 1], [1, 1] with diff=0, expected [1, 1, 1, 1]"
        )

    def test_max_product_subarray_with_min_k(self):
        """Test max_product_subarray_with_min_k function."""
        self.assertEqual(
            max_product_subarray_with_min_k([1, 2, 3, -1, 4], 3), 24,
            msg="Failed for [1, 2, 3, -1, 4] with k=3, expected 24"
        )
        self.assertEqual(
            max_product_subarray_with_min_k([1, 2], 3), None,
            msg="Failed for [1, 2] with k=3, expected None"
        )
        self.assertEqual(
            max_product_subarray_with_min_k([], 1), None,
            msg="Failed for empty array with k=1, expected None"
        )
        self.assertEqual(
            max_product_subarray_with_min_k([-2, -3, -4], 2), 12,
            msg="Failed for [-2, -3, -4] with k=2, expected 12"
        )
        self.assertEqual(
            max_product_subarray_with_min_k([0, 1, 0, 0], 2), 0,
            msg="Failed for [0, 1, 0, 0] with k=2, expected 0"
        )

    def test_find_pairs_with_sum_and_product(self):
        """Test find_pairs_with_sum_and_product function."""
        self.assertEqual(
            find_pairs_with_sum_and_product([1, 2, 3], [3, 2, 1], 4, 3), [(1, 3), (3, 1)],
            msg="Failed for [1, 2, 3], [3, 2, 1] with target_sum=4, target_product=3, expected [(1, 3), (3, 1)]"
        )
        self.assertEqual(
            find_pairs_with_sum_and_product([1, 2], [3, 4], 5, 10), [],
            msg="Failed for [1, 2], [3, 4] with target_sum=5, target_product=10, expected []"
        )
        self.assertEqual(
            find_pairs_with_sum_and_product([], [1, 2], 3, 2), [],
            msg="Failed for [], [1, 2] with target_sum=3, target_product=2, expected []"
        )
        self.assertEqual(
            find_pairs_with_sum_and_product([-1, 0], [1, 2], 1, 0), [(0, 1)],
            msg="Failed for [-1, 0], [1, 2] with target_sum=1, target_product=0, expected [(0, 1)]"
        )
        self.assertEqual(
            find_pairs_with_sum_and_product([2, 2], [2, 2], 4, 4), [(2, 2), (2, 2)],
            msg="Failed for [2, 2], [2, 2] with target_sum=4, target_product=4, expected [(2, 2), (2, 2)]"
        )

    def test_rearrange_by_value_and_frequency(self):
        """Test rearrange_by_value_and_frequency function."""
        self.assertEqual(
            rearrange_by_value_and_frequency([1, 2, 2, 1, 3, 3, 3]), [3, 3, 3, 2, 2, 1, 1],
            msg="Failed for [1, 2, 2, 1, 3, 3, 3], expected [3, 3, 3, 2, 2, 1, 1]"
        )
        self.assertEqual(
            rearrange_by_value_and_frequency([1, 1, 1]), [1, 1, 1],
            msg="Failed for [1, 1, 1], expected [1, 1, 1]"
        )
        self.assertEqual(
            rearrange_by_value_and_frequency([]), [],
            msg="Failed for empty array, expected []"
        )
        self.assertEqual(
            rearrange_by_value_and_frequency([-1, -1, 0, 0, 0, -2]), [0, 0, 0, -1, -1, -2],
            msg="Failed for [-1, -1, 0, 0, 0, -2], expected [0, 0, 0, -1, -1, -2]"
        )
        self.assertEqual(
            rearrange_by_value_and_frequency([1, 2, 3]), [3, 2, 1],
            msg="Failed for [1, 2, 3], expected [3, 2, 1]"
        )


    def test_replace_with_furthest_larger(self):
        """Test replace_with_furthest_larger function."""
        self.assertEqual(
            replace_with_furthest_larger([1, 3, 2, 4, 1]), [4, 4, 4, -1, -1],
            msg="Failed for [1, 3, 2, 4, 1], expected [4, 4, 4, -1, -1]"
        )
        self.assertEqual(
            replace_with_furthest_larger([5, 4, 3]), [-1, -1, -1],
            msg="Failed for [5, 4, 3], expected [-1, -1, -1]"
        )
        self.assertEqual(
            replace_with_furthest_larger([]), [],
            msg="Failed for empty array, expected []"
        )
        self.assertEqual(
            replace_with_furthest_larger([1]), [-1],
            msg="Failed for [1], expected [-1]"
        )
        self.assertEqual(
            replace_with_furthest_larger([2, 2, 2]), [-1, -1, -1],
            msg="Failed for [2, 2, 2], expected [-1, -1, -1]"
        )

    def test_find_subarray_with_k_sum_range(self):
        """Test find_subarray_with_k_sum_range function."""
        self.assertEqual(
            find_subarray_with_k_sum_range([1, 2, 3, 4, 5], 3, 6, 8), (0, 2),
            msg="Failed for [1, 2, 3, 4, 5] with k=3, min_sum=6, max_sum=8, expected (0, 2)"
        )
        self.assertEqual(
            find_subarray_with_k_sum_range([1, 2], 3, 1, 2), (-1, -1),
            msg="Failed for [1, 2] with k=3, min_sum=1, max_sum=2, expected (-1, -1)"
        )
        self.assertEqual(
            find_subarray_with_k_sum_range([], 1, 0, 1), (-1, -1),
            msg="Failed for empty array with k=1, min_sum=0, max_sum=1, expected (-1, -1)"
        )
        self.assertEqual(
            find_subarray_with_k_sum_range([-1, 0, 1, 2], 2, 0, 1), (1, 2),
            msg="Failed for [-1, 0, 1, 2] with k=2, min_sum=0, max_sum=1, expected (1, 2)"
        )
        self.assertEqual(
            find_subarray_with_k_sum_range([2, 2, 2], 2, 4, 4), (0, 1),
            msg="Failed for [2, 2, 2] with k=2, min_sum=4, max_sum=4, expected (0, 1)"
        )

    def test_count_subarrays_with_median_and_sum(self):
        """Test count_subarrays_with_median_and_sum function."""
        self.assertEqual(
            count_subarrays_with_median_and_sum([1, 2, 3, 2], 2, 5), 2,
            msg="Failed for [1, 2, 3, 2] with target_median=2, target_sum=5, expected 2"
        )
        self.assertEqual(
            count_subarrays_with_median_and_sum([1, 2], 1, 3), 0,
            msg="Failed for [1, 2] with target_median=1, target_sum=3, expected 0"
        )
        self.assertEqual(
            count_subarrays_with_median_and_sum([], 0, 0), 0,
            msg="Failed for empty array with target_median=0, target_sum=0, expected 0"
        )
        self.assertEqual(
            count_subarrays_with_median_and_sum([-1, 0, 1], 0, 0), 1,
            msg="Failed for [-1, 0, 1] with target_median=0, target_sum=0, expected 1"
        )
        self.assertEqual(
            count_subarrays_with_median_and_sum([2, 2], 2, 4), 1,
            msg="Failed for [2, 2] with target_median=2, target_sum=4, expected 1"
        )

if __name__ == '__main__':
    unittest.main()
