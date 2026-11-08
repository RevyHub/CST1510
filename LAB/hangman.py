import random

word_list = ["apple", "python", "computer", "security", "network"]
chosen_word = random.choice(word_list)
display = []
for letter in chosen_word:
    display.append("_")
lives = 6
guessed_letters = []
while "_" in display and lives > 0:
    print("\nWord:", " ".join(display))
    print("Lives:", lives)
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    guessed_letters.append(guess)
    if guess in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess
        print("Correct!")
    else:
        lives -= 1
        print("Wrong guess.")
if "_" not in display:
    print("\nYou win!")
    print("Word was:", chosen_word)
else:
    print("\nYou lose!")
    print("Word was:", chosen_word)