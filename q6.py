# q6.py - First negative number with WHILE loop
# Author: ph wong
# Date: March 2026

def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    # Check if lst is a list
    if not isinstance(lst, list):
        return "No negatives"
    
    i = 0  # Index counter
    while i < len(lst):  # While we haven't reached end of list
        if lst[i] < 0:   # Found negative number!
            return lst[i]
        i = i + 1        # Move to next number
    
    return "No negatives"  # No negatives found


# Task 2
# Test case 1: [3, 5, -1, 7, -2, 8] → -1
result1 = find_first_negative([3, 5, -1, 7, -2, 8])
print("Result 1:", result1)

# Test case 2: [2, 10, 7, 0] → "No negatives"
result2 = find_first_negative([2, 10, 7, 0])
print("Result 2:", result2)