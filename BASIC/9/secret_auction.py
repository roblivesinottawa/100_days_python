import os

bids = {}
bidding_finished = False

def find_highest_bidder(bids):
    highest_bid = 0
    winner = ""

    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"the winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("enter youur name: >>> ")
    price = int(input("what's your bid? >>> $ "))
    bids[name] = price
    should_continue = input("are there any other bidders? type 'yes' or 'no'. ")
    if should_continue == 'no':
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        os.system('cls')