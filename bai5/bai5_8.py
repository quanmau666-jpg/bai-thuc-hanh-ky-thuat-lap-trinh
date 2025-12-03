# Tìm kiếm tuyến tính trong danh sách
def Sequential_Search(dlist, item):
    for i, val in enumerate(dlist):  # duyệt từng phần tử
        if val == item:              # nếu tìm thấy
            return True, i           # trả về True và chỉ số
    return False, -1                  # nếu không tìm thấy
