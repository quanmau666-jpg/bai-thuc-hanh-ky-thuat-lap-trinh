import numpy as np  # Import thư viện NumPy

# Tạo mảng gồm các số từ 2 đến 10
x = np.arange(2, 11)

# Chuyển mảng 1 chiều thành ma trận 3x3
x = x.reshape(3, 3)

print("Ma trận 3x3 từ 2 đến 10:")
print(x)
