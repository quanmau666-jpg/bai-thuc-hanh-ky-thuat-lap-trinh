def benefit(t, n, k):
    # t: lãi suất %/tháng
    # n: vốn ban đầu
    # k: số tháng gửi
    final_money = n * (1 + t/100)**k
    return final_money

# Chương trình chính 
t = float(input("Nhập lãi suất t (%/tháng): "))
n = float(input("Nhập số vốn ban đầu n: "))
k = int(input("Nhập số tháng gửi k: "))

result = benefit(t, n, k)
print("Số tiền nhận được sau", k, "tháng là:", result)
