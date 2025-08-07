def permute(s: str) -> list[str]:
    """
    Generate all possible permutations of the input string.

    @param s: The input string to permute.
    @return: A list of strings representing all permutations.
    @example:
        >>> permute("abc")
        ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
        >>> permute("a")
        ['a']
    """
    # Reference: https://llego.dev/posts/how-generate-all-possible-permutations-string-python/

    if len(s) == 0:
        return []
    if len(s) == 1:
        return [s]

    permutations = []

    for i, char in enumerate(s):
        remaining_chars = s[:i] + s[i+1:]
        permutated = permute(remaining_chars)
        for string in permutated:
            permutations.append(char + string)

    return permutations


def count_permutations(n: int, items: list) -> int:
    """
    Count the number of permutations of n items from the given list.

    @param n: Number of items to select.
    @param items: List of items to permute.
    @return: Integer count of possible permutations.
    @example:
        >>> count_permutations(2, [1, 2, 3])
        6
        >>> count_permutations(1, [1])
        1
    """
    pass


def combinations(items: list, k: int) -> list[list]:
    """
    Generate all possible combinations of k items from the input list.

    @param items: List of items to choose from.
    @param k: Number of items to select in each combination.
    @return: List of lists, each containing a combination.
    @example:
        >>> combinations([1, 2, 3], 2)
        [[1, 2], [1, 3], [2, 3]]
        >>> combinations([1, 2], 1)
        [[1], [2]]
    """
    pass


def count_combinations(n: int, k: int) -> int:
    """
    Count the number of ways to choose k items from n items without repetition.

    @param n: Total number of items.
    @param k: Number of items to choose.
    @return: Integer count of combinations.
    @example:
        >>> count_combinations(5, 2)
        10
        >>> count_combinations(3, 3)
        1
    """
    pass


def permute_with_repetition(items: list, k: int) -> list[list]:
    """
    Generate all permutations of k items from the list, allowing repetition.

    @param items: List of items to choose from.
    @param k: Number of items in each permutation.
    @return: List of lists, each containing a permutation.
    @example:
        >>> permute_with_repetition([1, 2], 2)
        [[1, 1], [1, 2], [2, 1], [2, 2]]
        >>> permute_with_repetition([1], 1)
        [[1]]
    """
    pass


def subsets(items: list) -> list[list]:
    """
    Generate all possible subsets (combinations of any size) of the input list.

    @param items: List of items to generate subsets from.
    @return: List of lists, each containing a subset.
    @example:
        >>> subsets([1, 2])
        [[], [1], [2], [1, 2]]
        >>> subsets([1])
        [[], [1]]
    """
    pass


def permute_multiset(items: list) -> list[list]:
    """
    Generate all unique permutations of a list that may contain duplicates.

    @param items: List of items, possibly with duplicates.
    @return: List of lists, each containing a unique permutation.
    @example:
        >>> permute_multiset([1, 1, 2])
        [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
        >>> permute_multiset([1, 2])
        [[1, 2], [2, 1]]
    """
    pass


def combinations_with_repetition(items: list, k: int) -> list[list]:
    """
    Generate all combinations of k items from the list, allowing repetition.

    @param items: List of items to choose from.
    @param k: Number of items in each combination.
    @return: List of lists, each containing a combination.
    @example:
        >>> combinations_with_repetition([1, 2], 2)
        [[1, 1], [1, 2], [2, 2]]
        >>> combinations_with_repetition([1], 1)
        [[1]]
    """
    pass


def permute_fixed_length(items: list, k: int) -> list[list]:
    """
    Generate all permutations of k items from the input list without repetition.

    @param items: List of items to choose from.
    @param k: Length of each permutation.
    @return: List of lists, each containing a permutation.
    @example:
        >>> permute_fixed_length([1, 2, 3], 2)
        [[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]
        >>> permute_fixed_length([1], 1)
        [[1]]
    """
    pass


def count_subsets_with_sum(nums: list, target: int) -> int:
    """
    Count the number of subsets of the list that sum to the target value.

    @param nums: List of integers.
    @param target: Target sum.
    @return: Integer count of subsets with the target sum.
    @example:
        >>> count_subsets_with_sum([1, 2, 3], 3)
        2
        >>> count_subsets_with_sum([1, 1], 2)
        1
    """
    pass


def k_length_substrings(s: str, k: int) -> list[str]:
    """
    Generate all k-length substrings of the input string using combinations.

    @param s: Input string.
    @param k: Length of each substring.
    @return: List of k-length substrings.
    @example:
        >>> k_length_substrings("abc", 2)
        ['ab', 'ac', 'bc']
        >>> k_length_substrings("a", 1)
        ['a']
    """
    pass


def permute_with_constraints(items: list, forbidden: set[tuple]) -> list[list]:
    """
    Generate permutations of items excluding those with forbidden adjacent pairs.

    @param items: List of items to permute.
    @param forbidden: Set of tuples representing forbidden adjacent pairs.
    @return: List of valid permutations.
    @example:
        >>> permute_with_constraints([1, 2, 3], {(1, 2)})
        [[1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        >>> permute_with_constraints([1, 2], set())
        [[1, 2], [2, 1]]
    """
    pass


def combinations_sum(nums: list, target: int) -> list[list]:
    """
    Generate all combinations of numbers that sum to the target value.

    @param nums: List of integers.
    @param target: Target sum.
    @return: List of lists, each containing a combination that sums to target.
    @example:
        >>> combinations_sum([1, 2, 3], 3)
        [[1, 2], [3]]
        >>> combinations_sum([1, 1], 2)
        [[1, 1]]
    """
    pass


def circular_permutations(items: list) -> list[list]:
    """
    Generate all unique circular permutations of the input list.

    @param items: List of items to permute.
    @return: List of lists, each representing a unique circular permutation.
    @example:
        >>> circular_permutations([1, 2, 3])
        [[1, 2, 3], [1, 3, 2]]
        >>> circular_permutations([1, 2])
        [[1, 2]]
    """
    pass


def k_subsets_lexico(items: list, k: int) -> list[list]:
    """
    Generate all k-subsets of the input list in lexicographic order.

    @param items: List of items to choose from.
    @param k: Size of each subset.
    @return: List of lists, each containing a k-subset.
    @example:
        >>> k_subsets_lexico([1, 2, 3], 2)
        [[1, 2], [1, 3], [2, 3]]
        >>> k_subsets_lexico([1, 2], 1)
        [[1], [2]]
    """
    pass


def permute_with_prefix(items: list, prefix: list) -> list[list]:
    """
    Generate all permutations of items that start with the given prefix.

    @param items: List of items to permute.
    @param prefix: List representing the required prefix.
    @return: List of permutations starting with the prefix.
    @example:
        >>> permute_with_prefix([1, 2, 3], [1])
        [[1, 2, 3], [1, 3, 2]]
        >>> permute_with_prefix([1, 2], [2])
        [[2, 1]]
    """
    pass


def combinations_min_value(items: list, k: int, min_val: int) -> list[list]:
    """
    Generate all k-combinations where each item is at least min_val.

    @param items: List of integers.
    @param k: Number of items in each combination.
    @param min_val: Minimum value for items in the combination.
    @return: List of valid k-combinations.
    @example:
        >>> combinations_min_value([1, 2, 3, 4], 2, 2)
        [[2, 3], [2, 4], [3, 4]]
        >>> combinations_min_value([1, 2], 1, 2)
        [[2]]
    """
    pass


def count_permutations_fixed(items: list, fixed: dict) -> int:
    """
    Count permutations where certain items are fixed at specific positions.

    @param items: List of items to permute.
    @param fixed: Dictionary mapping positions (0-based) to required items.
    @return: Integer count of valid permutations.
    @example:
        >>> count_permutations_fixed([1, 2, 3], {0: 1})
        2
        >>> count_permutations_fixed([1, 2], {})
        2
    """
    pass


def derangements(n: int) -> list[list]:
    """
    Generate all derangements (permutations where no element is in its original position).

    @param n: Number of items (1 to n).
    @return: List of lists, each representing a derangement.
    @example:
        >>> derangements(3)
        [[2, 3, 1], [3, 1, 2]]
        >>> derangements(2)
        [[2, 1]]
    """
    pass


def combinations_constrained(items: list, k: int, forbidden: set) -> list[list]:
    """
    Generate k-combinations excluding those containing forbidden items.

    @param items: List of items to choose from.
    @param k: Number of items in each combination.
    @param forbidden: Set of items that cannot be included.
    @return: List of valid k-combinations.
    @example:
        >>> combinations_constrained([1, 2, 3, 4], 2, {3})
        [[1, 2], [1, 4], [2, 4]]
        >>> combinations_constrained([1, 2], 1, set())
        [[1], [2]]
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
