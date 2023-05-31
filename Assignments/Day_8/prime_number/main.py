def prime_checker(number):
    # Assume the number is prime initially
    is_prime = True

    # Check potential divisors from 2 to number - 1
    for divisor in range(2, number):
        # If the number is divisible by the divisor without leaving a remainder,
        # it is not prime
        if number % divisor == 0:
            is_prime = False

    # Check the value of is_prime after the loop
    if is_prime:
        # If is_prime is still True, the number is prime
        print("It's a prime number.")
    else:
        # If is_prime is False, the number is not prime
        print("It's not a prime number.")


# Ask the user to enter a number and call the prime_checker function
n = int(input("Check this number: "))
prime_checker(number=n)

while True:
    n = int(input("Check this number (enter 0 to exit): "))

    if n == 0:
        break

    prime_checker(number=n)

# def is_prime(n):
#     if n <= 1:
#         print(f"{n} is not a prime number.")
#         return False
#
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             print(f"{n} is not a prime number.")
#             return False
#
#     print(f"{n} is a prime number.")
#     return True
#
# while True:
#     n = int(input("Check this number (enter 0 to exit): "))
#
#     if n == 0:
#         break
#
#     is_prime(n)