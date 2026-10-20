# This is the Third project for extra projects week 4
# Week - 4, Blind Auction
bids = {}
keep_bidding = True
while keep_bidding:
    name = input("Name: ")
    bid = int(input("Bid (£): "))
    bids[name] = bid
    if input("Another bidder? (yes/no): ").lower() == "no":
        keep_bidding = False
highest_bid = 0
winner = ""
for name, bid in bids.items():
    if bid > highest_bid:
        highest_bid = bid
        winner = name
print(f"{winner} wins with a bid of £{highest_bid}.")