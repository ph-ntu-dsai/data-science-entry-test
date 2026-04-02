def update_dct(dct, key, value):
    if key in dct:
        print("Original value:", dct[key])
        dct[key] = value
    else:
        dct[key] = value
    return dct


x = update_dct({}, "name", "Alice")
print("Scene 1 result:", x)

y = update_dct({"age": 25}, "age", 26)
print("Scene 2 result:", y)
