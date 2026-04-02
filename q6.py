def find_first_negative(lst):
    i = 0
    while i < len(lst):
        if lst[i] < 0:
            return lst[i]
        i += 1
    return "No negatives"


x = find_first_negative([3, 5, -1, 7, -2, 8])
print("Scene 1 result:", x)

y = find_first_negative([2, 10, 7, 0])
print("Scene 2 result:", y)
