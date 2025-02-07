import random
print("Welcome to Rock, Paper, Scissors Game!")
def get_user_choice():
    user_choice = input("Enter your choice: rock, paper, or scissors (or 'quit' to exit): ").strip().lower()

    return user_choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    
    return computer_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == 'rock' and computer_choice == 'scissors':
        return "You win!"
    elif user_choice == 'paper' and computer_choice == 'rock':
        return "You win!"
    elif user_choice == 'scissors' and computer_choice == 'paper':
        return "You win!"
    elif user_choice == 'rock' and computer_choice == 'paper':
        return "Computer wins!"
    elif user_choice == 'paper' and computer_choice == 'scissors': 
        return "Computer wins!"
    elif user_choice == 'scissors' and computer_choice == 'rock':
        return "Computer wins!"
    else:
        return "Invalid input. Please enter rock, paper, or scissors."    

def main():
    while True:
        user_choice = get_user_choice()
        if user_choice == 'quit':
                print("Qutting the game...")
                break
        elif user_choice in ['rock', 'paper', 'scissors']:
            computer_choice = get_computer_choice()
            print(f"Computer chose {computer_choice}")
            print(f"You chose {user_choice}")
            result = determine_winner(user_choice, computer_choice)
            print(result)
        else:
            print("Invalid input. Please enter rock, paper, or scissors.")
    
    

if __name__ == "__main__":
    main()