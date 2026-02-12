import pandas

dataFrame = pandas.read_csv("student.csv")

dataFrame.loc[dataFrame["grade"] <= 9, "grade_band"] = "Low"
dataFrame.loc[(dataFrame["grade"] >= 10) & (dataFrame["grade"] <= 14), "grade_band"] = "Medium"
dataFrame.loc[dataFrame["grade"] >= 15, "grade_band"] = "High"

summary = dataFrame.groupby(["grade_band"]).agg(
    number_of_students = ("grade", "count"),
    average_absences = ("absences", "mean"),
    internet_percentage = ("internet", "mean")
)

summary["internet_percentage"] = summary["internet_percentage"] * 100

summary.to_csv("student_bands.csv")