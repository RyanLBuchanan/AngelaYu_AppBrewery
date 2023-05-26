
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
#
#
#
# print(weight/height**2)

h, w = map(float, input("Enter your height in m: "), input("Enter your weight in kg: "))
bmi = w / (h ** 2)
print(bmi)
