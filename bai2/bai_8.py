# In dãy Fibonacci < 4,000,000 và tính tổng các số chẵn

fib = [0, 1]   # Khởi tạo 2 số đầu tiên
while fib[-1] < 4000000:
    fib.append(fib[-1] + fib[-2])

# Bỏ số cuối nếu nó >= 4 triệu
if fib[-1] >= 4000000:
    fib.pop()

print("Dãy Fibonacci nhỏ hơn 4.000.000:")
print(fib)

tong_chan = sum(x for x in fib if x % 2 == 0)
print("Tổng các số chẵn trong dãy:", tong_chan)
