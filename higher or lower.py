import random

logo = r"""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = r"""
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

data = [
    {'name': 'Instagram', 'follower_count': 625, 'description': 'Social media platform', 'country': 'United States'},
    {'name': 'Cristiano Ronaldo', 'follower_count': 568, 'description': 'Footballer', 'country': 'Portugal'},
    {'name': 'Ariana Grande', 'follower_count': 363, 'description': 'Musician and actress', 'country': 'United States'},
    {'name': 'Dwayne Johnson', 'follower_count': 371, 'description': 'Actor and professional wrestler', 'country': 'United States'},
    {'name': 'Selena Gomez', 'follower_count': 406, 'description': 'Musician and actress', 'country': 'United States'},
    {'name': 'Kylie Jenner', 'follower_count': 384, 'description': 'Reality TV personality and businesswoman', 'country': 'United States'},
    {'name': 'Kim Kardashian', 'follower_count': 350, 'description': 'Reality TV personality and businesswoman', 'country': 'United States'},
    {'name': 'Lionel Messi', 'follower_count': 448, 'description': 'Footballer', 'country': 'Argentina'},
    {'name': 'Beyoncé', 'follower_count': 302, 'description': 'Musician', 'country': 'United States'},
    {'name': 'Neymar', 'follower_count': 207, 'description': 'Footballer', 'country': 'Brasil'},
    {'name': 'National Geographic', 'follower_count': 135, 'description': 'Magazine', 'country': 'United States'},
    {'name': 'Justin Bieber', 'follower_count': 283, 'description': 'Musician', 'country': 'Canada'},
    {'name': 'Taylor Swift', 'follower_count': 252, 'description': 'Musician', 'country': 'United States'},
    {'name': 'Kendall Jenner', 'follower_count': 281, 'description': 'Reality TV personality and Model', 'country': 'United States'},
    {'name': 'Jennifer Lopez', 'follower_count': 239, 'description': 'Musician and actress', 'country': 'United States'},
    {'name': 'Nicki Minaj', 'follower_count': 214, 'description': 'Musician', 'country': 'Trinidad and Tobago'},
    {'name': 'Nike', 'follower_count': 282, 'description': 'Sportswear multinational', 'country': 'United States'},
    {'name': 'Khloé Kardashian', 'follower_count': 300, 'description': 'Reality TV personality and businesswoman', 'country': 'United States'},
    {'name': 'Miley Cyrus', 'follower_count': 202, 'description': 'Musician and actress', 'country': 'United States'},
    {'name': 'Katy Perry', 'follower_count': 195, 'description': 'Musician', 'country': 'United States'},
    {'name': 'Kourtney Kardashian', 'follower_count': 216, 'description': 'Reality TV personality', 'country': 'United States'},
    {'name': 'Kevin Hart', 'follower_count': 170, 'description': 'Comedian and actor', 'country': 'United States'},
    {'name': 'Ellen DeGeneres', 'follower_count': 135, 'description': 'Comedian', 'country': 'United States'},
    {'name': 'Real Madrid CF', 'follower_count': 135, 'description': 'Football club', 'country': 'Spain'},
    {'name': 'FC Barcelona', 'follower_count': 119, 'description': 'Football club', 'country': 'Spain'},
    {'name': 'Rihanna', 'follower_count': 147, 'description': 'Musician and businesswoman', 'country': 'Barbados'},
    {'name': 'Demi Lovato', 'follower_count': 151, 'description': 'Musician and actress', 'country': 'United States'},
    {'name': "Victoria's Secret", 'follower_count': 75, 'description': 'Lingerie brand', 'country': 'United States'},
    {'name': 'Zendaya', 'follower_count': 173, 'description': 'Actress and musician', 'country': 'United States'},
    {'name': 'Shakira', 'follower_count': 85, 'description': 'Musician', 'country': 'Colombia'},
    {'name': 'Drake', 'follower_count': 134, 'description': 'Musician', 'country': 'Canada'},
    {'name': 'Chris Brown', 'follower_count': 135, 'description': 'Musician', 'country': 'United States'},
    {'name': 'LeBron James', 'follower_count': 150, 'description': 'Basketball player', 'country': 'United States'},
    {'name': 'Vin Diesel', 'follower_count': 91, 'description': 'Actor', 'country': 'United States'},
    {'name': 'Cardi B', 'follower_count': 158, 'description': 'Musician', 'country': 'United States'},
    {'name': 'David Beckham', 'follower_count': 78, 'description': 'Footballer', 'country': 'United Kingdom'},
    {'name': 'Billie Eilish', 'follower_count': 108, 'description': 'Musician', 'country': 'United States'},
    {'name': 'Justin Timberlake', 'follower_count': 69, 'description': 'Musician and actor', 'country': 'United States'},
    {'name': 'UEFA Champions League', 'follower_count': 104, 'description': 'Club football competition', 'country': 'Europe'},
    {'name': 'NASA', 'follower_count': 91, 'description': 'Space agency', 'country': 'United States'},
    {'name': 'Emma Watson', 'follower_count': 70, 'description': 'Actress', 'country': 'United Kingdom'},
    {'name': 'Shawn Mendes', 'follower_count': 72, 'description': 'Musician', 'country': 'Canada'},
    {'name': 'Virat Kohli', 'follower_count': 243, 'description': 'Cricketer', 'country': 'India'},
    {'name': 'Gigi Hadid', 'follower_count': 77, 'description': 'Model', 'country': 'United States'},
    {'name': 'Priyanka Chopra Jonas', 'follower_count': 86, 'description': 'Actress and musician', 'country': 'India'},
    {'name': '9GAG', 'follower_count': 58, 'description': 'Social media platform', 'country': 'China'},
    {'name': 'Ronaldinho', 'follower_count': 73, 'description': 'Footballer', 'country': 'Brasil'},
    {'name': 'Maluma', 'follower_count': 63, 'description': 'Musician', 'country': 'Colombia'},
    {'name': 'Camila Cabello', 'follower_count': 67, 'description': 'Musician', 'country': 'Cuba'},
    {'name': 'NBA', 'follower_count': 78, 'description': 'Club Basketball Competition', 'country': 'United States'}
]

def format_data(account):
    return f"{account['name']}, a {account['description']} from {account['country']}"

def check_answer(guess, a_followers, b_followers):
    return (guess == 'a' and a_followers > b_followers) or (guess == 'b' and b_followers > a_followers)

def get_random_account(exclude_account=None):
    account = random.choice(data)
    while account == exclude_account:
        account = random.choice(data)
    return account

def game():
    print(logo)
    print("🎮 Welcome to Higher or Lower: Instagram Followers Edition!")
    print("👉 Guess who has MORE Instagram followers.\n")
    score = 0
    game_should_continue = True

    account_a = get_random_account()
    account_b = get_random_account(exclude_account=account_a)

    while game_should_continue:
        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Against B: {format_data(account_b)}\n")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        while guess not in ['a', 'b']:
            guess = input("❌ Invalid input! Please type 'A' or 'B': ").lower()

        a_followers = account_a["follower_count"]
        b_followers = account_b["follower_count"]

        if check_answer(guess, a_followers, b_followers):
            score += 1
            print(f"✅ Correct! Your current score: {score}\n")
            account_a = account_b
            account_b = get_random_account(exclude_account=account_a)
        else:
            print(f"❌ Wrong! Final score: {score}")
            game_should_continue = False

while True:
    game()
    play_again = input("🔁 Do you want to play again? Type 'y' or 'n': ").lower()
    if play_again != 'y':
        print("👋 Thanks for playing! Goodbye!")
        break
    print("\n" + "=" * 60 + "\n")
