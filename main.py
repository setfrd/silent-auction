from turtle import clear
from art import logo

print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if int(bid_amount) > highest_bid:  # Convert bid_amount to integer
            highest_bid = int(bid_amount)  # Convert bid_amount to integer
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name?: ")
    price = input("What is your bid?:  $")
    bids[name] = price  # No conversion to int here
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()
