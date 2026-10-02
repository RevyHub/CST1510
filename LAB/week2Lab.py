# Week 2 - Extra Practice Projects
print("WEEK 2 PROJECTS")
print("1. Python Pizza")
print("2. Treasure Island")
print("3. Higher or Lower")
print("4. Number Guessing Game")
project = input("Choose a project (1 - 4): ")
if project == "1":
    print("PYTHON PIZZA")
    print("Sizes: S = $15, M = $20, L = $25")
    size = input("What size pizza? (S/M/L): ")
    if size == "S":
        bill = 15
    elif size == "M":
        bill = 20
    elif size == "L":
        bill = 25
    else:
        bill = 0
        print("That is not a valid size.")
    if bill > 0:
        pepperoni = input("Add pepperoni? (Y/N): ")
        if pepperoni == "Y" and size == "S":
            bill = bill + 2
        elif pepperoni == "Y":
            bill = bill + 3
        cheese = input("Add extra cheese? (Y/N): ")
        if cheese == "Y":
            bill = bill + 1
        print("Your final bill is: $" + str(bill) + ".")

elif project == "2":
    print("TREASURE ISLAND")
    print("You are on an island looking for treasure.")
    direction = input("Do you go left or right? ")
    if direction == "left":
        action = input("You reach a lake. Swim or wait? ")
        if action == "wait":
            door = input("Three doors appear: red, blue, or yellow. Which do you choose? ")
            if door == "yellow":
                print("You found the treasure!")
            elif door == "red":
                print("A dragon guards this room. Game over.")
            elif door == "blue":
                print("The room fills with water. Game over.")
            else:
                print("That door is not here. Game over.")
        else:
            print("The lake is too deep. Game over.")
    else:
        print("You fall into a hidden hole. Game over.")

elif project == "3":
    print("HIGHER OR LOWER")
    account_a = "A"
    followers_a = 120
    account_b = "B"
    followers_b = 85
    guess = ""
    while guess != "quit":
        print("Account A has " + str(followers_a) + " followers.")
        print("Account B has " + str(followers_b) + " followers.")
        guess = input("Which has more followers, A or B? Type quit to stop: ")
        if guess == "quit":
            print("Thanks for playing.")
        elif guess == account_a:
            if followers_a > followers_b:
                print("Correct")
            else:
                print("Wrong")
        elif guess == account_b:
            if followers_b > followers_a:
                print("Correct")
            else:
                print("Wrong")
        else:
            print("Enter A, B, or quit.")
elif project == "4":
    print("NUMBER GUESSING GAME")
    secret_number = 7
    guess_count = 0
    guess = 0
    while guess != secret_number:
        guess = int(input("Guess the secret number (1-10): "))
        guess_count = guess_count + 1

        if guess > secret_number:
            print("Too high.")
        elif guess < secret_number:
            print("Too low.")
        else:
            print("Correct! You guessed it in " + str(guess_count) + " guesses.")
else:
    print("Choose a number from 1 to 4.")
