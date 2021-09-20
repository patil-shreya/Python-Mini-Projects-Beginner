from replit import clear

import art

bids = {}

def highest_bid(bidding_record):
    highest_bid_amount = 0
    for bidder in bidding_record:
        bidding_amount = bidding_record[bidder]
        if bidding_amount > highest_bid_amount:
            highest_bid_amount = bidding_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid_amount}")
    
print(art.logo)

print("Welcome to the secret auction program!")

another_bidder = True
while another_bidder is True:
    name = input("What is your name?: ")
    bid_amount = int(input("What's your bid?: $"))
    bids[name] = bid_amount
    want_to_add = input("Are there any other bidders? Type 'Yes' or 'No' ").lower()
    if want_to_add == "no":
        another_bidder = False
        highest_bid(bids)
    elif want_to_add == "yes":
        clear()









    

    





