import random

def rock_paper_scissors():
    print("===================")
    print("Rock Paper Scissors")
    print("===================")
    print("1) ✊ Rock")
    print("2) ✋ Paper")
    print("3) ✌️ Scissors")

def rock_paper_scissors_lizard_spock():
    print("================================")
    print("Rock Paper Scissors Lizard Spock")
    print("================================")
    print("1) ✊ Rock")
    print("2) ✋ Paper")
    print("3) ✌️ Scissors")
    print("4) 🦎 Lizard")
    print("5) 🖖 Spock")  
    
def get_user_choice(max_choice):
    while True:
        try:
            choice = int(input("Pick a number: "))
            if 1 <= choice <= max_choice:
                return choice
            else:
                print(f"Please enter a number between 1 and {max_choice}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_computer_choice(max_choice):
    return random.randint(1, max_choice)

def determine_winner(user, cpu, rules):
    if user == cpu:
        return "It's a tie!"
    elif cpu in rules[user]:
        return "You won!"
    else:
        return "The CPU won!"
    
def main():
    print("Choose your game mode:")
    print("1) Rock Paper Scissors")
    print("2) Rock Paper Scissors Lizard Spock")

    game_mode = input("Select a game mode (1 or 2): ")

    if game_mode == "1":
        rock_paper_scissors()
        max_choice = 3
        rules = {
            1 : [3], #Rock beats Scissors
            2 : [1], #Paper beats Rock
            3 : [2], #Scissors beats Paper
        }
        choices = ["✊","✋","✌️"]

    elif game_mode == "2":
        rock_paper_scissors_lizard_spock()
        max_choice = 5
        rules = {
            1: [3, 4], # Rock beats Scissors and Lizard
            2: [1, 5], # Paper beats Rock and Spock
            3: [2, 4], #Scissors beaat Paper and Lizard
            4: [2, 5], #Lizard beats Paper and Spock
            5: [1, 3], #Spock beats Rock and Scissors
        }
        choices = ["✊","✋","✌️","🦎","🖖"]

    else:
        print("Invalid game mode.")
        return
    
    user_choice = get_user_choice(max_choice)
    cpu_choice = get_computer_choice(max_choice)

    print(f"\nYou chose: {choices[user_choice - 1]}")
    print(f"CPU chose: {choices[cpu_choice - 1]}")

    result = determine_winner(user_choice, cpu_choice, rules)
    print(result)



main()

