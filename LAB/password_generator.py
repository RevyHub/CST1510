# This is the second project for extra projects week 4
# Week - 4, Password Generator
import random
letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
num_letters = int(input("How many letters would you like? "))
num_symbols = int(input("How many symbols would you like? "))
num_numbers = int(input("How many numbers would you like? "))
password_list = []
for _ in range(num_letters):
    password_list.append(random.choice(letters))
for _ in range(num_symbols):
    password_list.append(random.choice(symbols))
for _ in range(num_numbers):
    password_list.append(random.choice(numbers))
random.shuffle(password_list)
password = "".join(password_list)
print(f"Your password is: {password}")