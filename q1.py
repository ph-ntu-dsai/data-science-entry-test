def swap(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return -1
    return y, x


result1 = swap("Apple", 10)
print("Scene 1 result:", result1)

result2 = swap(9, 17)
print("Scene 2 result:", result2)
