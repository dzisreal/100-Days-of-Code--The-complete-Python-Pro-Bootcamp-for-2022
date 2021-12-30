import random

name_string = input()
name = name_string.split(",")

n=10

while n>0:
    print(random.choice(name)) # ham choice chon random cac phan tu trong list luon, neu khong dung choice thi phai random theo vi tri phan tu
    n-=1