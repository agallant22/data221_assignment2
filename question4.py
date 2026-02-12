import pandas

dataFrame = pandas.read_csv("student.csv")

filtered_dataFrame = dataFrame[
    (dataFrame["studytime"] >= 3) &
    (dataFrame["internet"] == 1) &
    (dataFrame["absences"] <= 5)
]

# print(filtered_dataFrame)

filtered_dataFrame.to_csv("high_engagement.csv", index = False)

print("Students Saved: ", len(filtered_dataFrame))
print("Average Grade: ", filtered_dataFrame["grade"].mean())