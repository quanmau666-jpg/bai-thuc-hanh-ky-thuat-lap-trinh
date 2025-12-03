s = input("Nhập câu: ")

letters = digits = 0

for c in s:
    if c.isalpha():
        letters += 1
    elif c.isdigit():
        digits += 1

print("Số chữ cái là:", letters)
print("Số chữ số là:", digits)
