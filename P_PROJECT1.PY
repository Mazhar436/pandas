# ****************** Student Result Analysis ********************

import pandas as pd

data = {
    "Roll_No": [1, 2, 3, 4, 5],
    "Name": ["Ali", "Mazhar", "Azhar", "Iqra", "Saba"],
    "Math": [80, 92, None, 65, 72],
    "Physics": [86, 96, 78, 67, None],
    "Chemistry": [63, 75, 69, 84, 91],
    "English": [82, 87, 75, 68, None],
    "Computer": [65, 79, None, 94, 87]
}

df = pd.DataFrame(data)
print("Original Data:\n", df)

# Handle Missing Value
df = df.fillna(df.mean(numeric_only=True))
print("\nAfter Handling Missing Values:\n", df)

# Add new columns: Total and Percentage
df["Total"] = df[["Math", "Physics", "Chemistry", "English", "Computer"]].sum(axis=1)
df["Percentage"] = df["Total"] / 5

# Grade Assignment
bins = [0, 50, 60, 70, 80, 90, 100]
labels = ["F", "D", "C", "B", "A", "A+"]
df["Grade"] = pd.cut(df["Percentage"], bins=bins, labels=labels, right=False)

print("\nStudent Results with Grade:\n", df)

# Descriptive Statistics
print("\nDescriptive Statistics:\n", df.describe(include="all"))

# Sorting & Filtering 
top_students = df.sort_values(by="Total", ascending=False).head(3)
print("\nTOP 3 Students:\n", top_students)

high_score = df[df["Percentage"] > 80]
print("\nStudents with >80%:\n", high_score)

# Groupby & Aggregation
grade_group = df.groupby("Grade")[["Math", "Physics", "Chemistry", "English", "Computer"]].mean()
print("\nAverage Marks per Grade:\n", grade_group)

# Value counts
print("\nGrade Distribution:\n", df["Grade"].value_counts())

# Pivot Table
pivot = df.pivot_table(values="Total", index="Grade", aggfunc=["mean", "max", "min"])
print("\nPivot Table (Total per Grade):\n", pivot)

# Correlation 
print("\nCorrelation between Subjects:\n", df.corr(numeric_only=True))

# Conditional Selection 
fails = df[df["Percentage"] < 50]
print("\nStudents who failed:\n", fails)
