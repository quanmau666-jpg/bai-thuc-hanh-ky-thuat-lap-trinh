
text = input("Nhập văn bản: ")


words = text.split()


max_length = max(len(word) for word in words)


longest_words = [word for word in words if len(word) == max_length]


print("Các từ dài nhất là:", longest_words)
print("Độ dài của từ dài nhất là:", max_length)
