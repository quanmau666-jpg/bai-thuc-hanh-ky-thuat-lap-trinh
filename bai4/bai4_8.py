ds = input("Nhập dãy các từ: ").split()
max_len = max(len(tu) for tu in ds)
tu_dai_nhat = [tu for tu in ds if len(tu) == max_len]
print("Từ dài nhất có độ dài:", max_len)
print("Các từ dài nhất là:", ", ".join(tu_dai_nhat))
