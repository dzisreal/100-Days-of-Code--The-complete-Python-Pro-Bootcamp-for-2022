import random

simple_character = ["A","B","C","D","F",'G','H','I','K','L','M']

special_character = ["!","@","#","$","%",'^','*','(',')']

number_character = ['1','2','3','4','5','6','7','8','9']

pw = int(input("Nhap so ki tu trong password ban muon tao: "))

simple = int(input("Nhap so ki tu thuong: "))
special = int(input("Nhap so ki tu dac biet: "))
number = pw - simple - special

n=5
while n>0:
    pwl = []

    for i in range(simple):
        pwl += random.choice(simple_character)

    for i in range(special):
        pwl += random.choice(special_character)

    for i in range(number):
        pwl += random.choice(number_character)

    print(pwl)
    random.shuffle(pwl)
    print(pwl)

    password = ""
    for i in pwl:
        password+=i

    print(password)
    print(len(password))
    print("\n")
    n-=1
