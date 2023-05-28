# 🚨 Don't change the code below 👇
# Prompt the user to input a list of student heights, separated by spaces
student_heights = input("Input a list of student heights ").split()

# Convert the input heights from strings to integers
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

# Initialize variables to store the total heights and the number of students
total_heights = 0
num_students = 0

# Iterate over each student height in the list
for student in student_heights:
    # Add the current student's height to the total
    total_heights += student
    # Increment the number of students
    num_students += 1

# Calculate and print the average height rounded to the nearest whole number
print(round(total_heights / num_students))