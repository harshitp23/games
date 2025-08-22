import random

# Money ladder
MONEY_LADDER = [
    100, 200, 300, 500, 1000,
    2000, 4000, 8000, 16000, 32000,
    64000, 125000, 250000, 500000, 1000000
]
CHECKPOINTS = {4, 9}

# Questions
QUESTION_BANK = [
    {"question": "What does CPU stand for?",
     "options": ["Central Processing Unit", "Computer Personal Unit", "Central Peripheral Unit", "Core Processing Utility"],
     "answer": 0},
    {"question": "Which planet is known as the Red Planet?",
     "options": ["Venus", "Mars", "Jupiter", "Mercury"],
     "answer": 1},
    {"question": "In Python, what does len([1,2,3]) return?",
     "options": ["2", "3", "1", "Error"],
     "answer": 1},
    {"question": "Who wrote '1984'?",
     "options": ["George Orwell", "Aldous Huxley", "Ray Bradbury", "J.K. Rowling"],
     "answer": 0},
    {"question": "What is the capital of France?",
     "options": ["Paris", "Madrid", "Rome", "Berlin"],
     "answer": 0},
    {"question": "Which data structure uses FIFO order?",
     "options": ["Stack", "Queue", "Tree", "Graph"],
     "answer": 1},
    {"question": "Which language runs in a web browser?",
     "options": ["C", "Java", "Python", "JavaScript"],
     "answer": 3},
    {"question": "Which ocean is the largest?",
     "options": ["Atlantic", "Indian", "Pacific", "Arctic"],
     "answer": 2},
    {"question": "What gas do plants primarily absorb?",
     "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
     "answer": 2},
    {"question": "How many bits are in a byte?",
     "options": ["4", "8", "16", "32"],
     "answer": 1},
    {"question": "Which team sport uses the term 'offside'?",
     "options": ["Cricket", "Basketball", "Football (Soccer)", "Tennis"],
     "answer": 2},
    {"question": "Which library is standard for math in Python?",
     "options": ["numpy", "math", "pandas", "calc"],
     "answer": 1},
    {"question": "What is H2O commonly known as?",
     "options": ["Salt", "Hydrogen", "Water", "Oxygen"],
     "answer": 2},
    {"question": "Which country hosts the city of Barcelona?",
     "options": ["Italy", "France", "Portugal", "Spain"],
     "answer": 3},
    {"question": "Who painted the Mona Lisa?",
     "options": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet"],
     "answer": 1},
    {"question": "Which file extension is a Python file?",
     "options": [".js", ".py", ".java", ".txt"],
     "answer": 1},
    {"question": "What is the smallest prime number?",
     "options": ["0", "1", "2", "3"],
     "answer": 2},
    {"question": "Which is NOT an OOP principle?",
     "options": ["Encapsulation", "Polymorphism", "Inheritance", "Compilation"],
     "answer": 3},
    {"question": "Which metal is liquid at room temperature?",
     "options": ["Mercury", "Aluminum", "Iron", "Silver"],
     "answer": 0},
    {"question": "Which continent is the Sahara Desert in?",
     "options": ["Asia", "Africa", "Australia", "South America"],
     "answer": 1},
    {"question": "What does URL stand for?",
     "options": ["Uniform Resource Locator", "Universal Routing Link", "Unified Request Locator", "User Resource Link"],
     "answer": 0},
    {"question": "Which number system is binary?",
     "options": ["Base 10", "Base 2", "Base 8", "Base 16"],
     "answer": 1}
]

def use_lifeline(lifeline, options, correct_answer):
    if lifeline == "50-50":
        remaining = [correct_answer]
        while len(remaining) < 2:
            choice = random.choice(options)
            if choice != correct_answer and choice not in remaining:
                remaining.append(choice)
        random.shuffle(remaining)
        print("50-50 Lifeline Applied! Remaining options:")
        for idx, opt in enumerate(remaining):
            print(f"{idx+1}. {opt}")
        return remaining

    elif lifeline == "Hint":
        print(f"Hint: The correct answer starts with '{correct_answer[0]}'")
        return options

    elif lifeline == "Skip":
        print("Question skipped!")
        return None

def play_game():
    winnings = 0
    last_checkpoint = 0
    questions = random.sample(QUESTION_BANK, 15)
    lifelines = {"50-50": True, "Hint": True, "Skip": True}

    print("Welcome to Who Wants to Be a Millionaire!")

    for i in range(15):
        q = questions[i]
        correct_answer = q["options"][q["answer"]]

        while True:  # Keep asking until valid input
            print(f"\nQuestion {i+1} for ${MONEY_LADDER[i]:,}")
            print(q["question"])
            for idx, opt in enumerate(q["options"]):
                print(f"{chr(65+idx)}. {opt}")

            if any(lifelines.values()):
                print("Available Lifelines:", [name for name, available in lifelines.items() if available])

            answer = input("Your answer (A/B/C/D or lifeline name or 'quit'): ").strip()

            if answer.lower() == "quit":
                print(f"You walk away with ${winnings:,}.")
                return

            # Lifeline check (case-insensitive)
            if answer.title() in lifelines and lifelines[answer.title()]:
                lifelines[answer.title()] = False
                result = use_lifeline(answer.title(), q["options"], correct_answer)
                if answer.title() == "Skip":
                    break  # Move to next question
                answer = input("Now enter your answer (A/B/C/D): ").strip().upper()

            if answer.upper() not in ["A", "B", "C", "D"]:
                print("Invalid input. Try again.")
                continue  # Ask the same question again

            # Convert answer to index
            if ord(answer.upper()) - 65 == q["answer"]:
                winnings = MONEY_LADDER[i]
                print("✅ Correct!")
                if i in CHECKPOINTS:
                    last_checkpoint = winnings
                    print(f"Checkpoint reached: ${last_checkpoint:,}")
                if i == 14:
                    print("🏆 Congratulations! You won $1,000,000!")
                break  # Exit while loop for this question
            else:
                print(f"❌ Wrong! The correct answer was {chr(65+q['answer'])}. {correct_answer}")
                print(f"You leave with ${last_checkpoint:,}.")
                return  # Game over

    print(f"Game Over. You won ${winnings:,}.")


# Main loop to play again
while True:
    play_game()
    again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if again != "yes":
        print("Thanks for playing! Goodbye!")
        break
