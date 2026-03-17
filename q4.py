# q4.py - String reversing
# Author: ph wong
# Date: March 2026

def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    # Check if s is a string
    if not isinstance(s, str):
        return ""  # Return empty string if not string
    
    # Reverse using slicing: s[start:end:step]
    # s[::-1] means "whole string, step -1 (backwards)"
    return s[::-1]


# Task 2
# Test case 1
result1 = string_reverse("Hello World")
print("Result 1:", result1)  # dlroW olleH

# Test case 2
result2 = string_reverse("Python")
print("Result 2:", result2)  # nohtyP