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

if __name__ == '__main__':
    unittest.main()