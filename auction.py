import os
import random


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                       .-------------.
                      /_______________\
'''

# Auction items
auction_items = [
    "Vintage Painting",
    "Signed Football Jersey",
    "Luxury Watch",
    "Mountain Bike",
    "Concert VIP Tickets",
    "Gaming Laptop",
    "Mystery Box"
]


def get_bid(min_bid):
    name = input("Enter your name: ").strip().title()

    while True:
        try:
            price = int(input(f"Enter your bid (minimum ${min_bid}): $"))
            if price < min_bid:
                print(f"Bid must be at least ${min_bid}.")
            else:
                return name, price
        except ValueError:
            print("Invalid input. Please enter a positive number.")


def highest_bidder(bidding_record, item, reserve_price):
    if not bidding_record:
        print(f"\nNo bids were placed for {item}.")
        return None, None

    winner, highest_bid = max(bidding_record.items(), key=lambda x: x[1])

    if highest_bid < reserve_price:
        print(f"\nReserve price of ${reserve_price} not met. No winner for {item}.")
        return None, None

    print(f"\nThe winner of the {item} is {winner} with a bid of ${highest_bid}!\n")

    print("Bidding History:")
    for bidder, bid in sorted(bidding_record.items(), key=lambda x: x[1], reverse=True):
        print(f"- {bidder}: ${bid}")

    return winner, highest_bid


def start_auction(item):
    clear_screen()
    print(logo)
    print(f"\nAuction begins for: {item}\n")

    reserve_price = int(input("Set the reserve price ($): "))
    min_increment = int(input("Set the minimum increment ($): "))

    bids = {}
    highest = reserve_price

    while True:
        name, price = get_bid(highest + min_increment - 1)
        bids[name] = price
        highest = max(highest, price)

        more_bidders = input("Are there any other bidders? (yes/no): ").strip().lower()
        while more_bidders not in ["yes", "no"]:
            more_bidders = input("Please enter yes or no: ").strip().lower()

        if more_bidders == "no":
            return highest_bidder(bids, item, reserve_price)
        else:
            clear_screen()
            print(logo)
            print(f"\nBidding continues for: {item}\n")


# --- Main Program ---
def main():
    clear_screen()
    print(logo)
    print("🎉 Welcome to the Ultimate Silent Auction! 🎉\n")

    items_to_auction = auction_items.copy()

    while items_to_auction:
        print("\nItems available for auction:")
        for i, item in enumerate(items_to_auction, start=1):
            print(f"{i}. {item}")

        try:
            choice = int(input("\nChoose an item by number (or 0 for random Mystery Box): "))
            if choice == 0:
                item = random.choice(items_to_auction)
            elif 1 <= choice <= len(items_to_auction):
                item = items_to_auction[choice - 1]
            else:
                raise ValueError
        except ValueError:
            print("Invalid choice. Try again.")
            continue

        start_auction(item)
        items_to_auction.remove(item)

        more_items = input("\nDo you want to auction another item? (yes/no): ").strip().lower()
        if more_items != "yes":
            break

    print("\n🎉 Auction event has ended. Thank you for participating!")


if __name__ == "__main__":
    main()
