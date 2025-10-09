import math

def Tinh(R):
    
    if not isinstance(R, (int, float)):
        print("Lỗi: Bán kính phải là số (int hoặc float)!")
        return None
    if R <= 0:
        print("Bán kính phải lớn hơn 0. Hãy thử lại!")
        return None
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R ** 2

    print("KẾT QUẢ TÍNH TOÁN HÌNH TRÒN ")
    print(f"Bán kính: {R}")
    print(f"Chu vi: {chu_vi:.3f}")
    print(f"Diện tích: {dien_tich:.3f}")
    print("Hoàn tất tính toán!")

if __name__ == "__main__":
    try:
        R = float(input("Nhập bán kính hình tròn: "))
        ket_qua = Tinh(R)
        if ket_qua:
            print("\nDữ liệu trả về:", ket_qua)
    except ValueError:
        print("Lỗi: Bạn phải nhập một giá trị số!")
