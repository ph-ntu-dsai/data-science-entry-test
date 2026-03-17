# q5.py - Divisibility check (math + conditions!)
# Author: ph wong
# Date: March 2026


def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    # Check if both are numbers (int or float)
    if not isinstance(num, (int, float)) or not isinstance(divisor, (int, float)):
        return False
    
    # Check if divisor is zero (can't divide by zero)
    if divisor == 0:
        return False
    
    # Check divisibility: remainder must be 0
    return num % divisor == 0


# Task 2
# Test case 1: 10, 2 → 10 % 2 = 0 → True
result1 = check_divisibility(10, 2)
print("Result 1 (10, 2):", result1)

# Test case 2: 7, 3 → 7 % 3 = 1 → False
result2 = check_divisibility(7, 3)
print("Result 2 (7, 3):", result2)