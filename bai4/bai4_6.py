ten_day_du = input("Nhập họ và tên: ").strip()

# Tách thành danh sách các từ
tu = ten_day_du.split()

if len(tu) == 2:
    ho = tu[0]
    ten = tu[1]
    print("Họ:", ho)
    print("Tên riêng:", ten)
else:
    print("Vui lòng nhập đúng định dạng: chỉ gồm họ và tên riêng (2 từ).")
