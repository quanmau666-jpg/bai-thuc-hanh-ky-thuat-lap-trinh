def count_lines_in_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
            print(f"Số dòng trong tệp {filename}: {len(lines)}")
    except FileNotFoundError:
        print(f"Không tìm thấy tệp: {filename}")
    except Exception as e:
        print("Lỗi khác:", e)


count_lines_in_file("test.txt")
