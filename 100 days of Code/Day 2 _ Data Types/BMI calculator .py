w  = float(input("Nhap can nang (kg): "))
h = float(input("Nhap chieu cao (m): "))

# ham round lam tron den so nguyen gan nhat
# ham int lam tron xuong
# ham ceil lam tron len, nhung muon dung phai import math
print(f"Chi so BMI cua ban la: {round(w/(h*h),3)}")
# so 3 la do dai phan sau dau "."