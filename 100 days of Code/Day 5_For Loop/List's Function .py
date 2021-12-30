lst = list(map(int, input("Nhap chieu cao moi nguoi: ").split()))
print(lst)
print(sum(lst))
print(max(lst))

s = 0
for i in range(2,101,2):
    s+=i
print(f"Tong so chan tu 1 den 100: {s}")

for i in range(100):
    if i%15==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)