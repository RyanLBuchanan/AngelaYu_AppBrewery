with open("file1.txt") as numbers_1:
    n1 = numbers_1.readlines()
with open("file2.txt") as numbers_2:
    n2 = numbers_2.readlines()

# n1 = [int(num.rstrip('\n')) for num in n1]
# n2 = [int(num.rstrip('\n')) for num in n2]
# print(n1)
# print(n2)

result = [int(n) for n in n1 if n in n2]
# result = [n for n in number if n in pd.read()]
# Write your code above 👆

print(result)

