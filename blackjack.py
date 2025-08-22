import random

# Logo for display
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ / 
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

# Card deck
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    """Returns a random card from the deck."""
    return random.choice(cards)


def calculate_score(cards_list):
    """Calculates the score of the given hand."""
    # Blackjack (Ace + 10)
    if sum(cards_list) == 21 and len(cards_list) == 2:
        return 0
    # Adjust Ace from 11 to 1 if score > 21
    if 11 in cards_list and sum(cards_list) > 21:
        cards_list.remove(11)
        cards_list.append(1)
    return sum(cards_list)


def compare(user_score, computer_score):
    """Compares the scores and returns the result message."""
    if user_score == computer_score:
        return "🤝 It's a draw!"
    elif computer_score == 0:
        return "💀 You lose! The computer has a Blackjack!"
    elif user_score == 0:
        return "🎉 You win with a Blackjack!"
    elif user_score > 21:
        return "😢 You went over. You lose!"
    elif computer_score > 21:
        return "🔥 Computer went over. You win!"
    elif user_score > computer_score:
        return "✅ You win!"
    else:
        return "❌ You lose!"


def play_game():
    print(logo)
    print("🎲 Welcome to Blackjack! Try to beat the dealer without going over 21.")
    print("-" * 60)

    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]

    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            draw_card = input("👉 Type 'y' to draw another card or 'n' to pass: ").lower()
            if draw_card == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print("-" * 60)
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
    print("-" * 60)


while input("🎮 Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    print("\n" + "=" * 70 + "\n")
    play_game()
