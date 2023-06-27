total = 0  # Variable to store the sum of numbers
for number in range(0, 101, 2):  # Loop through even numbers from 0 to 100
    total += number  # Add the current number to the total
    # print(f"{number} : {total}")  # Optional: Print the current number and total
print(total)  # Print the final sum of even numbers
