# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import os
import pandas

os.chdir('C:/Users/Admin/Desktop/100 days of Code/Day 26_List Comprehension and the NATO Alphabet/NATO alphabet')

data = pandas.read_csv("nato_phonetic_alphabet.csv")
print(data)