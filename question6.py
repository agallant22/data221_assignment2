import pandas

dataFrame = pandas.read_csv("crime.csv")

dataFrame["risk"] = dataFrame["ViolentCrimesPerPop"].apply(
    lambda x: "HighCrime" if x >= 0.50 else "LowCrime"
)

average_employment = dataFrame.groupby("risk")["PctUnemployed"].mean()

print("Average Unemployment Rate by Crime Risk Level:")
print(f"High Crime: {average_employment["HighCrime"]:.2f}")
print(f"Low Crime: {average_employment["LowCrime"]:.2f}")