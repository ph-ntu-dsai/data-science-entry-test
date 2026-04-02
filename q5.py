def check_divisibility(num, divisor):
    if not isinstance(num, (int, float)) or not isinstance(divisor, (int, float)):
        return -1
    if divisor == 0:
        return -1
    return num % divisor == 0


x = check_divisibility(10, 2)
print("Scene 1 result:", x)

y = check_divisibility(7, 3)
print("Scene 2 result:", y)

z = check_divisibility("ten", 2)
print("Scene 3 result:", z)
