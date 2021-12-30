#Tim so chan
# numbers = [1,1,2,3,5,8,13,21,34,55]

# result = [num for num in numbers if not num%2] 

# print(result)


#Tim so co trong ca 2 file
import os
os.chdir("C:/Users/Admin/Desktop/100 days of Code/Day 26_List Comprehension and the NATO Alphabet")

with open("text1.txt") as txt1:
    nums1 = txt1.readlines()


with open("text2.txt") as txt2:
    nums2 = txt2.readlines()

number = [int(num) for num in nums1 if num in nums2]
print(number)
