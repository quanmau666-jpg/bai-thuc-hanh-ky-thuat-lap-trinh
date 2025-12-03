
source_file = "students.txt"

destination_file = "students_copy.txt"


with open(source_file, "r", encoding="utf-8") as src, open(destination_file, "w", encoding="utf-8") as dest:
   
    content = src.read()
    
    dest.write(content)

print(f"Đã sao chép nội dung từ '{source_file}' sang '{destination_file}' thành công!\n")


print("Nội dung trong tệp sao chép:")
with open(destination_file, "r", encoding="utf-8") as f:
    print(f.read())
