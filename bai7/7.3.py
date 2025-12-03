


ten_tap_tin = input("Nhập tên tệp văn bản (ví dụ: vanban.txt): ")

try:
    
    with open(ten_tap_tin, 'r', encoding='utf-8') as f:
        noi_dung = f.read()  
    
    print("\n--- Nội dung của tệp ---")
    print(noi_dung)

except FileNotFoundError:
    print("❌ Không tìm thấy tệp. Vui lòng kiểm tra lại tên tệp!")
except Exception as e:
    print("⚠️ Lỗi:", e)
