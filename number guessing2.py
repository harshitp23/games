import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

logo = r"""
                  __                                            _            
   ____  __  ______ ___  / /_  ___  _____   ____ ___  _____  __________(_)___  ____ _
  / __ \/ / / / __ `__ \/ __ \/ _ \/ ___/  / __ `/ / / / _ \/ ___/ ___/ / __ \/ __ `/
/ / / / /_/ / / / / / / /_/ /  __/ /     / /_/ / /_/ /  __(__  |__  ) / / / / /_/ / 
/_/ /_/\__,_/_/ /_/ /_/_.___/\___/_/      \__, /\__,_/\___/____/____/_/_/ /_/\__, /  
                                         /____/                             /____/ 
"""

def play_game():
    clear_screen()
    print(logo)
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number = random.randint(1, 100)

    while True:
        level = input("Choose difficulty - easy or hard: ").lower()
        if level == "hard":
            attempts = 5
            break
        elif level == "easy":
            attempts = 10
            break
        else:
            print("Invalid choice. Please type 'easy' or 'hard'.")

    print(f"You have {attempts} attempts to guess the number.")

    while attempts > 0:
        try:
            user_number = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if user_number == number:
            print(f"🎉 Correct! The number was {number}. You win!")
            return True
        elif user_number < number:
            print("Higher!")
        else:
            print("Lower!")

        # Give a "closeness" hint
        if abs(user_number - number) <= 5 and user_number != number:
            print("You're very close!")

        attempts -= 1
        print(f"You have {attempts} attempts remaining.\n")

    print(f"💀 You ran out of attempts. The number was {number}. Better luck next time!")
    return False

def main():
    gameover = False
    wins, losses = 0, 0

    while not gameover:
        result = play_game()
        if result:
            wins += 1
        else:
            losses += 1

        print(f"Scoreboard → Wins: {wins}, Losses: {losses}")
        more = input("Would you like to play again? (y/n): ").lower()
        if more != "y":
            print("Thank you for playing! Goodbye.")
            gameover = True

if __name__ == "__main__":
    main()
