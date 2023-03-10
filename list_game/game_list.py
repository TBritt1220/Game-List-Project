"""
Author: Taiwan Britt
"""
# Establish the initial values in the list to start the game
my_games = [0, 1, 2]
other_games = [3, 4, 5]


def replacement_choice(games):
    """
    Gives the user the option to replace current values in their list with new values
    """
    print(f"Here is the current list: {games}")
    # New value will automatically become a string without using "" in the input bar
    location = input("What location would you like to update? ")
    user_choice = input("Type a string to place at position: ")
    games[int(location)] = user_choice
    print(f'Updated: {games}')


# Replaced the current value of 1 in my list with Tai
replacement_choice(my_games)


def game_on_choice():
    """
    Creating an interactive menu to give the user an option to continue playing the game or end it
    """
    while True:
        choice = input("keep playing (Y or N): ")
        if choice.upper() == 'Y':
            return True
        elif choice.upper() == 'N':
            print("game has ended")
            return False
        else:
            continue


# User feedback established by the While If loop if user makes invalid & valid input
game_on_choice()

# Establish the interactive feedback the user receives for as long as they continue to play
game_on = True

# Creates updates on the game in response to the user interaction & choices
while game_on:
    # Input new value to replace the current selected value 
    replacement_choice(my_games)
    # Does the user want to continue playing the game?
    game_on = game_on_choice()
    if not game_on:
        break
