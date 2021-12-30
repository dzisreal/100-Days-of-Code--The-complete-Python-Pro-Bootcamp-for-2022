PLACEHOLDER = "[name]"


with open("C:/Users/Admin/Desktop/100 days of Code/Day 24_Files, Directories and Paths/Mail Merge Project Completed/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("C:/Users/Admin/Desktop/100 days of Code/Day 24_Files, Directories and Paths/Mail Merge Project Completed/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"C:/Users/Admin/Desktop/100 days of Code/Day 24_Files, Directories and Paths/Mail Merge Project Completed/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

