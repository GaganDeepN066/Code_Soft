import random

def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and comp_choice == 'scissors') or \
         (user_choice == 'scissors' and comp_choice == 'paper') or \
         (user_choice == 'paper' and comp_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_score = 0
    comp_score = 0

    while True:
        user_input = input("Choose \n rock, paper, or scissors \n(or 'quit' to exit): ").lower()
        if user_input == 'quit':
            break
        elif user_input not in ['rock', 'paper', 'scissors']:
            print("Invalid input. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print(f"Your choice: {user_input}")
        print(f"Computer's choice: {computer_choice}")

        result = determine_winner(user_input, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            comp_score += 1

        print(f"Score - You: {user_score} Computer: {comp_score}")

    print("Thanks for playing!")

play_game()