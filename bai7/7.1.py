
file_path = 'D:/a.txt'  

content = """Hello
Python
GPT
   trailing space   
"""


with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Đã tạo file ví dụ tại:", file_path)
print("Nội dung file:")
print(content)
print("="*40)



print("Cách 1: Phiên bản sửa lỗi (giữ khoảng trắng đầu/cuối)")
with open(file_path, 'r', encoding='utf-8') as input_file:
    for line in input_file:
        line_no_newline = line.rstrip('\n')  # chỉ bỏ newline
        s = ''
        l = len(line_no_newline)
        while l > 0:
            s = s + line_no_newline[l - 1]
            l -= 1
        print(s)
print("="*40)


