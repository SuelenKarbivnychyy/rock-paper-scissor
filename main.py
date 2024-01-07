import random

def Play_game():
    """
    Ask the user to choose one hand to play the game and based on the rules
    the program should display who is the winning!

    Rules: Rock crushes scissors, scissors cut paper, and paper covers rock. 
    """

    hands = ["Rock", "Paper", "Scissors"]

    game_on = True
    user_score = 0
    computer_score = 0

    while game_on:

        computer_hand = random.choice(hands)
        users_hand = input("\n                   Please enter your hand to play: \n-Rock \n-Paper \n-Scissors\nOr enter 'No' to exit:\n\n").title()
                

        if users_hand == "No":
            game_on = False                
            
            if user_score == computer_score:
                print("\nIs a draw!")
            elif user_score > computer_score:
                print("\nUser is the winning!!!")
            else:
                print("\nThe computer won!")
            print(f"User Score: {user_score} X Computer Score: {computer_score}") 

        else:         
            print(f"\nUser's hand: {users_hand}\nComputer's hand: {computer_hand}\n")
            if users_hand == computer_hand:
                print("It's a draw.\n")            
            elif users_hand == hands[0] and computer_hand == hands[2]:
                user_score +=1
                print("Rock crushes Scissors!\n\nPoint for the User")            
            elif users_hand == hands[2] and computer_hand == hands[1]:
                user_score +=1
                print("Scissors cut Paper!\n\nPoint for the User")
            elif users_hand == hands[1] and computer_hand == hands[0]:
                user_score +=1
                print("Paper covers Rock!\n\nPoint for the User")
            else:
                print("Computer Score this time.\n")
                computer_score +=1              


ask_users_hand()    