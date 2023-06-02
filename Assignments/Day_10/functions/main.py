# Functions with outputs

# def my_function(a, b):
#     result = a * b
#     return result
#
# output = my_function(3, 9)
#
# print(output)

def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    full_name = formatted_f_name + ' ' + formatted_l_name
    return f"{formatted_f_name} {formatted_l_name}"

f_name = input("What is your first name? ")
l_name = input("What is your last name? ")

formatted_string = format_name(f_name, l_name)
print(formatted_string)
