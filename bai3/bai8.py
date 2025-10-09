import math

x, y = 0, 0  # Tọa độ ban đầu của robot

while True:
    move = input("Nhập hướng và số bước (hoặc nhấn Enter để dừng): ")
    if not move:  # Nếu người dùng nhấn Enter trống thì dừng
        break
    try:
        direction, steps = move.split()
        steps = int(steps)
    except ValueError:
        print("Sai định dạng! Hãy nhập theo mẫu: UP 5 hoặc LEFT 3.")
        continue

    direction = direction.upper()
    if direction == "UP":
        y += steps
    elif direction == "DOWN":
        y -= steps
    elif direction == "LEFT":
        x -= steps
    elif direction == "RIGHT":
        x += steps
    else:
        print("Hướng không hợp lệ! (chỉ dùng UP, DOWN, LEFT, RIGHT)")

distance = math.sqrt(x**2 + y**2)
print("Khoảng cách từ vị trí hiện tại đến điểm đầu tiên là:", round(distance))
