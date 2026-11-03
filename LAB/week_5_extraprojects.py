import random

class Hand:
    def __init__(self):
        self.cards = []
    def add_card(self):
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.cards.append(random.choice(cards))
    def score(self):
        if sum(self.cards) == 21 and len(self.cards) == 2:
            return 0
        if 11 in self.cards and sum(self.cards) > 21:
            self.cards.remove(11)
            self.cards.append(1)
        return sum(self.cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif user_score == 0:
        return "Win with a Blackjack!"
    elif computer_score == 0:
        return "Lose, dealer has Blackjack."
    elif user_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "Dealer went over. You win."
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose."
    
print("=== Blackjack (Object-Oriented Version) ===")
user_hand = Hand()
computer_hand = Hand()
for _ in range(2):
    user_hand.add_card()
    computer_hand.add_card()

game_over = False

while not game_over:
    user_score = user_hand.score()
    computer_score = computer_hand.score()
    print(f"\nYour cards: {user_hand.cards}")
    print(f"Current score: {user_score}")
    print(f"Dealer's first card: {computer_hand.cards[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
        game_over = True
    else:
        choice = input("Type 'y' to hit or 'n' to stand: ")

        if choice.lower() == "y":
            user_hand.add_card()
        else:
            game_over = True

while computer_hand.score() != 0 and computer_hand.score() < 17:
    computer_hand.add_card()

print("\n===== FINAL RESULTS =====")
print(f"Your cards: {user_hand.cards}")
print(f"Your final score: {user_hand.score()}")
print(f"\nDealer cards: {computer_hand.cards}")
print(f"Dealer final score: {computer_hand.score()}")
print("\n" + compare(user_hand.score(), computer_hand.score()))
