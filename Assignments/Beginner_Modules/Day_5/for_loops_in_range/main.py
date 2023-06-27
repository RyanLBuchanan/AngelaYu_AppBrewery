# For loop with range
# for number in range(1, 11, 3):
#     print("Number", number)
from openpyxl.styles.builtins import total

# Add number from 1 to 100 -> from Gauss' childhood with Bad Teacher
total = 0
for number in range(1, 101):
    total += number
print(total)