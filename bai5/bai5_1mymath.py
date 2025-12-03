# Định nghĩa module toán học mymath

# Hàm tính bình phương
def square(n):
    return n * n

# Hàm tính lập phương
def cube(n):
    return n * n * n

# Hàm tính trung bình cộng của danh sách
def average(values):
    nvals = len(values)          # Số lượng phần tử
    total = sum(values)          # Tổng các phần tử
    return total / nvals         # Trả về trung bình
