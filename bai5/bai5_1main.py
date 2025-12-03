# Sử dụng module mymath
import mymath as mt  # import module và đặt tên tắt là mt

values = [2, 4, 6, 8, 10]  # Danh sách ví dụ

print("Squares:")
for v in values:
    print(mt.square(v))  # Gọi hàm square từ module

print("Cubes:")
for v in values:
    print(mt.cube(v))    # Gọi hàm cube từ module

print("Average:", mt.average(values))  # Gọi hàm average từ module

