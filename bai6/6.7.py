import math

class Circle:
    def __init__(self, radius):
        self.radius = radius  # khởi tạo bán kính

    def area(self):
        # Diện tích hình tròn: π * r^2
        return math.pi * (self.radius ** 2)

    def circumference(self):
        # Chu vi hình tròn: 2 * π * r
        return 2 * math.pi * self.radius


# --- Ví dụ chạy thử ---
r = float(input("Nhập bán kính hình tròn: "))
c = Circle(r)

print("Diện tích hình tròn là:", c.area())
print("Chu vi hình tròn là:", c.circumference())
