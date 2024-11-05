import random
import time

# Game introduction
def intro():
    print("=====================")
    print("The Adventure Begins!")
    print("=====================")
    print("You find yourself in a dark forest, surrounded by towering trees and eerie silence.")
    print("Your goal is to survive and find your way out. Good luck!")
    print("\n")
    time.sleep(2)

# Function to make choices
def choose_path():
    print("Choose a path:")
    print("1) Take the winding path deeper into the forest.")
    print("2) Follow the narrow trail along the river.")
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        forest_path()
    elif choice == '2':
        river_path()
    else:
        print("Invalid choice! Try again.")
        choose_path()

# Forest path
def forest_path():
    print("\nYou wander down the winding path, when suddenly you hear rustling behind you.")
    print("A wild goblin appears! It snarls and gets ready to attack.")
    action = input("Do you want to (1) fight or (2) run? ")

    if action == '1':
        fight()
    elif action == '2':
        print("You quickly turn and run back to the beginning.")
        choose_path()
    else:
        print("Invalid choice! The goblin attacks you as you hesitate.")
        game_over()

# River path
def river_path():
    print("\nYou follow the river, enjoying the sound of water flowing peacefully.")
    print("After a while, you spot a boat tied to a tree.")
    action = input("Do you want to (1) take the boat or (2) keep walking along the river? ")

    if action == '1':
        print("You untie the boat and start paddling down the river...")
        print("A few miles down, you reach a small village. You've made it out of the forest safely!")
        print("Congratulations, you survived!")
    elif action == '2':
        print("You keep walking along the river and stumble upon a hidden treasure chest!")
        print("You open it and find a magic amulet. You've earned a bonus!")
    else:
        print("Invalid choice!")
        river_path()

# Fight function
def fight():
    player_hp = 10
    goblin_hp = 5
    print("\nBattle Start!")
    
    while player_hp > 0 and goblin_hp > 0:
        print("\n1) Attack")
        print("2) Defend")
        action = input("Choose your move: ")

        if action == '1':
            damage = random.randint(1, 5)
            goblin_hp -= damage
            print(f"You attack the goblin and deal {damage} damage! Goblin HP is now {goblin_hp}.")
        elif action == '2':
            print("You brace yourself and block the goblin's attack.")
            continue
        else:
            print("Invalid choice!")

        if goblin_hp <= 0:
            print("You defeated the goblin! You continue down the path.")
            return
        else:
            damage = random.randint(1, 3)
            player_hp -= damage
            print(f"The goblin attacks you and deals {damage} damage! Your HP is now {player_hp}.")

        if player_hp <= 0:
            game_over()

# Game over
def game_over():
    print("\nYou have been defeated. Game Over.")
    exit()

# Start game
intro()
choose_path()
