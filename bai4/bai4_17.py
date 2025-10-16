n = int(input("Nhập n: "))
for i in range(1, n):
    tong = sum(j for j in range(1, i) if i % j == 0)
    if tong > i:
        print(i, end=" ")
