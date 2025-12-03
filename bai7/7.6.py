def file_read_from_tail(fname, lines):
    try:
        with open(fname, "r", encoding="utf-8") as f:
            data = f.readlines()  
            if not data:
                print("Tệp rỗng.")
                return
            
            last_lines = data[-lines:]
            print("".join(last_lines))
    except FileNotFoundError:
        print(f"Không tìm thấy tệp: {fname}")
    except Exception as e:
        print("Lỗi khác:", e)


file_read_from_tail("test.txt", 2)
