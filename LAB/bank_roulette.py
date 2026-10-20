# This is the first project for extra projects week 4
# Week - 4, Bank Roullette
import random
friends = ["Alice", "Bob", "Charlie", "Dana", "Ella"]
num_friends = len(friends)
index = random.randint(0, num_friends - 1)
payer = friends[index]
print(f"{payer} is paying the bill today!")