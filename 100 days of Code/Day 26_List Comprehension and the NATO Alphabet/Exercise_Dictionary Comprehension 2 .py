student_dict = {
    "student":["angela","james","lily"],
    "score": [56,76,98]
}

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# for (key, value) in student_data_frame.items():
#     print(value)


for (index, row) in student_data_frame.iterrows():
    # print(index)
    # print(row.student)
    # print(row.score)
    if row.student == "angela":
        print(row.score)
