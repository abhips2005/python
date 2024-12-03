print("Welcome to stick game!")
print("Rules: \n -> Two players take turns to play the game. \n "
      "-> Each player picks one set of sticks (needn’t be adjacent) during his turn. \n"
      "-> A set contains 1, 2, or 3 sticks. The player who takes the last stick is the loser. \n"
      "-> The number of sticks in the set is to be input.")

player1=input("Enter the name of player 1: ")
player2=input("Enter the name of player 2: ")


def stick_game():
    sticks = 16
    while sticks>0:
        print(f"Total number of sticks remaining : {sticks}")
        player1_choice = int(input(f"Hey {player1} , choose the no of sticks (1,2,3): "))
        if player1_choice>3 or player1_choice>sticks:
            print("You break the rules! You are out.")
            break
        sticks=sticks-player1_choice
        if sticks==0:
            print(f"f{player1} lost!")
            break
            

        print(f"Remaining sticks: {sticks}")
        player2_choice= int(input(f"Hey {player2} , choose the no of sticks (1,2,3): "))
        if player2_choice > 3 or player1_choice > sticks:
            print("You break the rules! You are out.")
            break
        sticks=sticks-player2_choice
        if sticks==0:
            print(f"{player2} lost!")
print(stick_game())