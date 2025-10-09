import tkinter as tk
from tkinter import ttk, messagebox


def benefit(t, n, k):
    """Hàm tính lãi kép và trả về danh sách giá trị từng tháng"""
    values = [n]
    for _ in range(k):
        n *= (1 + t / 100)
        values.append(n)
    return values


def calculate():
    try:
        t = float(entry_t.get())
        n = float(entry_n.get())
        k = int(entry_k.get())

        if t <= 0 or n <= 0 or k <= 0:
            messagebox.showerror("Lỗi", "Các giá trị phải lớn hơn 0!")
            return

        values = benefit(t, n, k)
        final_amount = values[-1]
        profit = final_amount - values[0]

        # Hiển thị kết quả
        result_text.set(
            f"Tổng tiền sau {k} tháng: {final_amount:,.2f} VND\n"
            f"Tiền lãi tích lũy: {profit:,.2f} VND"
        )

        # Vẽ biểu đồ ASCII
        chart_display.delete("1.0", tk.END)
        max_len = 40
        max_val = max(values)
        for i, val in enumerate(values[1:], start=1):
            bar_len = int((val / max_val) * max_len)
            bar = "█" * bar_len
            chart_display.insert(tk.END, f"Tháng {i:>2}: {bar} {val:,.0f}\n")

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập đúng định dạng số.")


# --- Giao diện chính ---
app = tk.Tk()
app.title("💰 ỨNG DỤNG TÍNH LÃI TIẾT KIỆM 💰")
app.geometry("600x500")
app.resizable(False, False)
app.configure(bg="#f5f7fa")

# --- Tiêu đề ---
title = tk.Label(
    app,
    text="📈 ỨNG DỤNG TÍNH LÃI TIẾT KIỆM",
    font=("Consolas", 18, "bold"),
    bg="#f5f7fa",
    fg="#2c3e50",
)
title.pack(pady=10)

# --- Khung nhập liệu ---
frame_input = ttk.Frame(app)
frame_input.pack(pady=10)

ttk.Label(frame_input, text="Lãi suất (%/tháng):", font=("Consolas", 12)).grid(row=0, column=0, padx=10, pady=5)
entry_t = ttk.Entry(frame_input, width=20)
entry_t.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(frame_input, text="Vốn ban đầu (VND):", font=("Consolas", 12)).grid(row=1, column=0, padx=10, pady=5)
entry_n = ttk.Entry(frame_input, width=20)
entry_n.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(frame_input, text="Số tháng gửi:", font=("Consolas", 12)).grid(row=2, column=0, padx=10, pady=5)
entry_k = ttk.Entry(frame_input, width=20)
entry_k.grid(row=2, column=1, padx=10, pady=5)

# --- Nút tính toán ---
btn_calc = ttk.Button(app, text="Tính Toán 💡", command=calculate)
btn_calc.pack(pady=10)

# --- Kết quả ---
result_text = tk.StringVar()
result_label = tk.Label(
    app,
    textvariable=result_text,
    font=("Consolas", 12),
    bg="#f5f7fa",
    fg="#34495e",
)
result_label.pack(pady=5)

# --- Biểu đồ ---
chart_label = tk.Label(app, text="Biểu đồ tăng trưởng:", font=("Consolas", 13, "bold"), bg="#f5f7fa", fg="#2c3e50")
chart_label.pack()

chart_display = tk.Text(app, width=70, height=12, font=("Consolas", 10), bg="#ecf0f1", fg="#2c3e50")
chart_display.pack(pady=5)

# --- Ghi chú ---
footer = tk.Label(
    app,
    text="(C) 2025 - Sáng tạo bởi ChatGPT x Mau Quan 🌿",
    font=("Consolas", 9),
    bg="#f5f7fa",
    fg="#95a5a6",
)
footer.pack(side=tk.BOTTOM, pady=5)

app.mainloop()
