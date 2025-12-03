class Hinhchunhat(object):
   
    def __init__(self, dai, rong):
        self.chieu_dai = dai
        self.chieu_rong = rong

    
    def dientich(self):
        return self.chieu_dai * self.chieu_rong



hcn1 = Hinhchunhat(5, 3)
hcn2 = Hinhchunhat(10, 4)
hcn3 = Hinhchunhat(7, 2)


print("Hình chữ nhật 1:")
print("  Chiều dài:", hcn1.chieu_dai)
print("  Chiều rộng:", hcn1.chieu_rong)
print("  Diện tích:", hcn1.dientich())

print("\nHình chữ nhật 2:")
print("  Chiều dài:", hcn2.chieu_dai)
print("  Chiều rộng:", hcn2.chieu_rong)
print("  Diện tích:", hcn2.dientich())

print("\nHình chữ nhật 3:")
print("  Chiều dài:", hcn3.chieu_dai)
print("  Chiều rộng:", hcn3.chieu_rong)
print("  Diện tích:", hcn3.dientich())
