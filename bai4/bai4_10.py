# Bai 9: 
ds = input("Nhập list (các phần tử cách nhau bởi dấu cách): ").split()
print("List vừa nhập:", ds)

# Bai 10: 
if len(ds) > 2:
    print("List sau khi cắt:", ds[1:-1])
else:
    print("List quá ngắn để cắt!")

# Bai 11: 
pt = input("Nhập phần tử muốn thêm: ")
ds.append(pt)
print("Sau khi thêm:", ds)

# Bai 12: 
x = input("Nhập phần tử muốn xóa: ")
if x in ds:
    ds.remove(x)
print("Sau khi xóa:", ds)

# Bai  13: 
t = input("Nhập phần tử cần tìm: ")
if t in ds:
    print(f"'{t}' ở vị trí:", ds.index(t))
else:
    print(f"'{t}' không có trong list")

# Bai  14:
ds.sort()
print("List sau khi sắp xếp:", ds)
