import sheety

first_name = input(
    "Welcome to Ryan's Flight Club.\nWe find the best flight deals and email you.\nWhat is your first name? ")
last_name = input("And what is your last name, please? ")

email = input("Finally, what is your email? ")
email_confirmation = input("Please type your email a second time for confirmation: ")

email = "email"
email_confirmation = "email_confirmation"

while email != email_confirmation:
    email = input("Finally, what is your email? ")
    if email.lower() == "quit" \
            or email.lower() == "exit":
        exit()
    email_confirmation = input("Please type your email a second time for confirmation: ")
    if email_confirmation.lower() == "quit" \
            or email.lower() == "exit":
        exit()

print("Brilliant! You made the cut. You're in the Flight Club!")

sheety.post_new_row(first_name, last_name, email)

"""MY FIRST ATTEMPT -> WHICH DID WORK . . . MOSTLY ;)"""
# import requests

# # Sheety API constant
# SHEETY_USERS_ENDPOINT = "https://api.sheety.co/b456eca6f5cc1f2313ff597eca22ef30/flightDeals/users"

# first_name = input("Welcome to Ryan's Flight Club.\nWe find the best flight deals and email you.\nWhat is your first name? ")
# last_name = input("And what is your last name, please? ")

# email = ""
# email_confirmation = ""

# def get_email():
# email = input("Finally, what is your email? ")
# email_confirmation = input("Please type your email a second time for confirmation: ")
#   return email, email_confirmation

# get_email()
# email_confirmed = False
# while email_confirmed:
#   if email == email_confirmation:
#     print("Brilliant! You made the cut. You're in the Flight Club!")
#     email_confirmed = True
#   else:
#     get_email()


# new_data = {
#   "user": {
#     "firstName": first_name,
#     "lastName": last_name,
#     "email": email
#   }
# }
# response = requests.post(
#   url=SHEETY_USERS_ENDPOINT,
#   json=new_data
# )
# data = response.json()
# print(data["user"])
