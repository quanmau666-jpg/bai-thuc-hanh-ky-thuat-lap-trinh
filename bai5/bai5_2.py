import datetime as dt  # Import thư viện datetime

# Định dạng chuỗi ngày giờ
format = '%Y-%m-%dT%H:%M:%S'

# Chuyển chuỗi thành đối tượng datetime
t1 = dt.datetime.strptime('2008-10-12T14:45:52', format)

# In ra các thông tin riêng lẻ
print("Day", t1.day)        # Ngày
print("Month", t1.month)    # Tháng
print("Minute", t1.minute)  # Phút
print("Second", t1.second)  # Giây

# Lấy thời gian hiện tại
t2 = dt.datetime.now()

# Tính hiệu giữa hai thời điểm
diff = t2 - t1
print("How many days difference?", diff.days)  # Số ngày chênh lệch
