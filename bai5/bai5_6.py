import numpy as np

# Tạo mảng mẫu
arr = np.array([1, 3, 5, 7, 9, 11])

# Nhập số từ bàn phím
x = int(input("Nhập số cần kiểm tra: "))

# Kiểm tra xem x có nằm trong arr hay không
if x in arr:
    print(x, "có trong mảng.")
else:
    print(x, "KHÔNG có trong mảng.")
