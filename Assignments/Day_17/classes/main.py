# class Car:
#     # Initialize and add constructor
#     def __init__(self, seats):
#         self.seats = seats
#
#     def enter_race_mode(self):
#         self.seats = 2
#
#
# car = Car(5)
# print(f"Number of seats: {car.seat}")

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("007", "James Bond")
user_2 = User("001", "Jack")

# print(f"Username: {user_1.username}")

user_1.follow(user_2)
print(f"{user_1.username}'s followers: {user_1.followers}\n{user_1.username} is following: {user_1.following}\n")
print(f"{user_2.username}'s followers: {user_2.followers}\n{user_2.username} is following: {user_2.following}\n")
