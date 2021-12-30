print("Welcome to the Love Calculator!")
name1 = input("Your name: ")
name2 = input("Her name: ")

name = name1 + name2

low_case_name = name.lower()

s1 = 0
for i in "true":
    print(f"{i} occurs {low_case_name.count(i)} times.")
    s1+=low_case_name.count(i)
print(f"Total: {s1}")

s2 = 0
for i in "love":
    print(f"{i} occurs {low_case_name.count(i)} times.")
    s2+=low_case_name.count(i)
print(f"Total: {s2}")

print(f"Score: {str(s1) + str(s2)}")

