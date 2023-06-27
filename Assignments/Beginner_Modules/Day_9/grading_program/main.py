student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# Create an empty dictionary called student_grades.
student_grades = {}

# Write your code below to add the grades to student_grades.👇
for key, value in student_scores.items():
    if value >= 91:
        student_grades[key] = "Outstanding"
    elif value >= 81:
        student_grades[key] = "Exceeds Expectations"
    elif value >= 71:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

# 🚨 Don't change the code below 👇
print(f"Student Grades dictionary: {student_grades}")