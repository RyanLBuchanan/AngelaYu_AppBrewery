# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
# Initialize the highest_score variable with the first score in the list
highest_score = student_scores[0]

# Iterate over each score in the list starting from the second score
for score in student_scores:
    # Compare the current score to the highest_score
    if score > highest_score:
        highest_score = score

# Print the highest score
print(f"The highest score in the class is: {highest_score}")