print("Chao mung den voi may tinh tien!")
total_bill = float(input("Tong tien hoa don la: $"))
tip = int(input("Ban muon tip cho nhan vien bao nhieu % ? 10, 12 or 15? "))
people = int(input("Nhom co bao nhieu nguoi: "))

print(f"Moi nguoi can tra {round((total_bill+total_bill * tip/100)/people,2)} dollars.")


