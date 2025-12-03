s = input("Nhập câu: ")

upper = lower = 0

for c in s:
    if c.isupper():
        upper += 1
    elif c.islower():
        lower += 1

print("Chữ hoa:", upper)
print("Chữ thường:", lower)
