# Recursion Repository

This repository contains Python files with moderate-level recursion problems that avoid specialized algorithms (e.g., dynamic programming, backtracking). The problems focus on recursive logic, state management, and data structures like nested lists and strings.

This repository contains two Python files:
- `recursion.py`: This file contains recursion problems
- `recursion_unittest.py`: This file contains unittest of problems in `recursion.py`.

Each problem includes a function signature and epytext docstring with examples.

## Table of Contents
- [Why Recursion?](#why-recursion)
- [Getting Started](#getting-started)
- [Testing the Solutions](#testing-the-solutions)
- [Guidelines](#Guidelines)

## Why Recursion?
Recursion is a powerful programming technique where a function calls itself to solve smaller instances of the same problem. It’s particularly useful for problems involving:
- Hierarchical or nested structures (e.g., lists within lists).
- Divide-and-conquer strategies.
- Combinatorial tasks (e.g., counting paths or substrings).

These problems build on basic recursion concepts:
- Multiple recursive calls (e.g., climbing stairs with 1 or 2 steps).
- State tracking (e.g., tracking alternating signs or parentheses balance).
- Complex data structures (e.g., nested lists).
- String and list manipulation (e.g., merging lists, finding substrings).

## Getting Started
Follow these steps to use the repository:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/paras-a/Recursion.git
   cd recursion
   ```

2. **Requirements**:
   - Python 3.6 or higher.
   - No external libraries are required, as the problems use standard Python.

3. **File Structure**:
   - `recursion.py`: recursion problems.
   - `recursion_unittest.py` (optional): Unit tests for the problems.
   - `README.md`: This file.

4. **Implementing Solutions**:
   - Open the Python files in your editor.
   - Each function is solved with a workable solution. You can replace the solution with `pass` and implement your own solution.
   - Use the docstring examples to guide your solution and verify correctness.

5. **Running the Code**:
   - Test individual functions in a Python interpreter:
     ```python
        from recursion import climb_stairs
        print(climb_stairs(3))  # Should print 3
     ```
   - Or create a script to test multiple cases:
     ```python 
        from recursion import count_nested_depth
        print(count_nested_depth([1, [2, 3], [4, [5]]]))  # Should print 3
     ```

## Testing the Solutions
To ensure that the implementations are correct, I did the following:

1. **Use Docstring Examples**:
   - Each function’s docstring includes example inputs and expected outputs (e.g., `climb_stairs(3)` → `3`).
   - Manually test these in a Python interpreter or script.

2. **Create Unit Tests**:
   - `recursion_unittest.py` contains all the test cases that I ran to ensure functionality.
   - Run tests using:
     ```bash
     python -m unittest recursion_unittest.py
     ```
   - Create test files using the `unittest` framework. Example:
     ```python
     import unittest
     from recursion_unittest import count_nested_depth

     class TestMoreModerateRecursion(unittest.TestCase):
         def test_count_nested_depth(self):
             self.assertEqual(count_nested_depth([1, [2, 3], [4, [5]]]), 3)
             self.assertEqual(count_nested_depth([]), 0)
             self.assertEqual(count_nested_depth([1, 2, 3]), 1)

     if __name__ == '__main__':
         unittest.main()
     ```

3. **Edge Cases**:
   - Test edge cases like empty inputs, single elements, or invalid inputs (e.g., negative numbers for some functions).
   - Example edge cases:
     - `contains_string("", "a")` → `False`
     - `count_nested_depth([[]])` → `2`
     - `count_paths(1, 1)` → `1`

## Guidelines
- Use Python 3 and maintain consistent formatting (e.g., PEP 8).
- Include docstrings with `@param`, `@return`, `@rtype`, and examples.
- Test your code thoroughly.

## License
This repository is licensed under the MIT License.

---

Happy coding, and enjoy mastering recursion!