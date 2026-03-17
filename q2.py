def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    
    # Check if lst is actually a list
    if not isinstance(lst, list):
        return []  # Return empty list if input is not a list
    
    # Create new list with replacements
    new_list = []
    for item in lst:
        if item == find_val:
            new_list.append(replace_val)  # Replace this item
        else:
            new_list.append(item)         # Keep original item
    
    return new_list


# Task 2
# Test case 1: [1, 2, 3, 4, 2, 2], 2, 5
result1 = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
print("Result 1:", result1)  # Should be: [1, 5, 3, 4, 5, 5]

# Test case 2: ["apple", "banana", "apple"], "apple", "orange"
result2 = find_and_replace(["apple", "banana", "apple"], "apple", "orange")
print("Result 2:", result2)  # Should be: ['orange', 'banana', 'orange']