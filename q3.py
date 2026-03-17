def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    
    # Check if key already exists
    if key in dct:
        print("Original value for", key, "was:", dct[key])
        dct[key] = value  # Update existing value
    else:
        dct[key] = value  # Add new key-value pair
    
    return dct


# Task 2
# Test case 1: {}, "name", "Alice"
result1 = update_dictionary({}, "name", "Alice")
print("Result 1:", result1)  # Should be: {'name': 'Alice'}

# Test case 2: {"age": 25}, "age", 26
result2 = update_dictionary({"age": 25}, "age", 26)
print("Result 2:", result2)  # Should print "25" first, then: {'age': 26}