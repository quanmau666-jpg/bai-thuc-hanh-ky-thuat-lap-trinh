import turtle

# Tạo cửa sổ vẽ
window = turtle.Screen()
window.bgcolor("lightgreen")   # Đổi màu nền

# Tạo "bút vẽ"
painter = turtle.Turtle()
painter.fillcolor('blue')      # Màu tô
painter.pencolor('blue')       # Màu viền
painter.pensize(3)             # Độ dày nét vẽ


# Hàm vẽ hình vuông cạnh s
def drawsq(t, s):
    for i in range(4):
        t.forward(s)   # Vẽ một cạnh
        t.left(90)     # Quay trái 90 độ để tạo góc vuông

# Lặp nhiều lần: mỗi lần xoay nhẹ rồi vẽ 1 hình vuông
for i in range(1, 180):
    painter.left(18)          # Xoay 18 độ
    drawsq(painter, 200)      # Vẽ hình vuông cạnh 200

# Giữ cửa sổ vẽ khi chạy xong
turtle.done()
