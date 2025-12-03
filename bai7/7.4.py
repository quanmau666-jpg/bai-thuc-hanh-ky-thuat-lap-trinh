

def file_read_from_head(fname, nlines):
    from itertools import islice 
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            print(f"\n--- {nlines} dòng đầu tiên của tệp {fname} ---")
            for line in islice(f, nlines):
                print(line.strip())  
    except FileNotFoundError:
        print("❌ Không tìm thấy tệp. Vui lòng kiểm tra lại tên tệp!")
    except Exception as e:
        print("⚠️ Lỗi:", e)



file_read_from_head('7.1','7.2')
