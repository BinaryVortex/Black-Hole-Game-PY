import random
import time
from prettytable import PrettyTable

Retry="Yes"
while(Retry=="Yes"):
    
    #Enter name
    Name=str(input("Enter student name:"))
    print(" ")
    
    # Define the board
    board = [['-' for _ in range(20)] for _ in range(2)]

    # Define the player and computer pawns
    player = 0
    computer = 0
    s_player = False
    s_computer = False

    # Initialize the number of moves made by each player
    player_moves = 0
    computer_moves = 0
    player_black_holes = 0
    computer_black_holes = 0

    # Define the dice roll function
    def roll_dice():
        "This function will rolling a dice"
        return random.randint(1, 6)

    # Define a function to display the game board
    def display_board():
        "This function will create the board"
        x = PrettyTable()
        x = PrettyTable(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'])
        x.clear_rows()
        x.add_row(board[0][:6] + ['O'] + board[0][7:13] + ['O'] + board[0][14:])
        x.add_row(board[1][:6] + ['O'] + board[1][7:13] + ['O'] + board[1][14:])
        print(x)

    #------------------------------------------------------------main program------------------------------------------------------------
    # Define the function to move the pawn
    def move_pawn(pawn, steps):
        "This function will update the position on the board"
        pawn += steps
        if pawn == 7 or pawn == 14:
            pawn = 1
            print("Hit a black hole! Moving back to block 1.")
        elif pawn > 20:
            pawn = 20
        return pawn

    # Play the game
    while(Retry=="Yes"):

        # Player's turn
        input("Press enter to roll the dice...")
        roll = roll_dice()
        player_moves += 1
        print(f"Player dice roll is {roll}")
        is_first = False
        if s_player == False:
            if roll == 6:
                s_player = True
                is_first = True
                print("Player can now start moving.")
            else:
                print("Player need to roll a 6 to start the game.")
            
        if s_player == True  and is_first == False:
            if player == 0 and roll < 2:
                print("Cannot move.Player need to roll a 2 or greater.")
            else:
                if player +(roll // 2) == 7 or player +(roll // 2) == 14:
                    player_black_holes += 1

                player = move_pawn(player, roll // 2)
                
                print("Player moved to block", player)
                if board[player // 20][player % 20] == 'O':
                    
                    player = 0
                if player >= 20:
                    print("Player won!")
                    break
                
                board[0][player-1] = 'X'
                display_board()
                board[0][player-1] = '-'

        # Computer's turn

        time.sleep(1)  # Add delay to simulate the computer's "thinking" time
        roll = roll_dice()
        computer_moves += 1
        print(f"Computer dice roll is {roll}")
        is_first = False
        if s_computer == False:
            if roll == 6:
                s_computer = True
                is_first = True
                print("Computer can now start moving.")
            else:
                print("Computer need to roll a 6 to start the game.")

        if s_computer == True  and is_first == False:
            if computer == 0 and roll < 2:
                print("Cannot move.Computer need to roll a 2 or greater.")
            else:
                if computer +(roll // 2) == 7 or computer +(roll // 2) == 14:
                    computer_black_holes += 1

                computer = move_pawn(computer, roll // 2)

                print("Computer moved to block", computer)
                computer_moves += 1
                if board[computer // 20][computer % 20] == 'O':
                    computer_black_holes += 1

                    computer = 0
                if computer >= 20:
                    print("Computer won!")
                    break
                board[1][computer-1] = 'X'
                display_board()
                board[1][computer-1] = '-'

    # Save the game session to a text file
    timestamp = time.strftime("%Y_%m_%d_%H_%M")#  YYYY_M_D_H_M format

    # Open a new file in write mode
    filename = f"{timestamp}.txt"

    # Write some text to the file
    with open(filename, "w") as f:
        f.write(f"Player\n")
        if player >= 20:
            f.write("Player won!\n")
        elif player != 20:
            f.write("Player lost!\n")
        f.write(f"Player final block: {player}\n")
        f.write(f"Total player moves: {player_moves}\n")
        f.write(f"Total player black holes: {player_black_holes}\n")
        f.write(f"   \n")
        f.write(f"   \n")
        f.write(f"Computer\n")
        if computer >= 20:
            f.write("Computer won!\n")
        elif computer != 20:
            f.write("Computer lost!\n")
        f.write(f"Computer final block: {computer}\n")
        f.write(f"Total computer moves: {computer_moves}\n")
        f.write(f"Total computer black holes: {computer_black_holes}")

        Retry=str(input("Do you want to play another game(Yes/No)?"))
        if(Retry!="Yes"):
            print('Thank you')
                