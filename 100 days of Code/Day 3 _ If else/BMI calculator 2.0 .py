h = float(input("Nhap chieu cao: "))
w = float(input("Nhap can nang: "))

BMI = round(w/(h*h),1)

print(f"BMI cua ban la: {BMI}")
if BMI < 18.5:
    print("Under weight")
elif 18.5 < BMI < 25:
    print("Normal weight")
elif 25 < BMI < 30:
    print("Over weight")
elif 30 < BMI < 35:
    print("Obese")
else:
    print("Clinically obese")