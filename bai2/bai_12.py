import re

value = []

items = [x for x in input("Nhập mật khẩu (cách nhau bằng dấu phẩy): ").split(',')]

for p in items:
    if len(p) < 6 or len(p) > 12:
        continue
    if not re.search("[a-z]", p):
        continue
    if not re.search("[0-9]", p):
        continue
    if not re.search("[A-Z]", p):
        continue
    if not re.search("[$#@]", p):
        continue
    if re.search("\s", p):
        continue
    value.append(p)

print("Mật khẩu hợp lệ:", ",".join(value))
