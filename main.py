
# -------- Global variables ----------

# Game board

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
# If game is still going

game_still_going = True

# Who won? or Tie?
winner = None

# Who's turn is it
current_player = "X"


# The cmd for the display board
def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


# The function to play the game
def play_game():
    global winner
    global board
    # display the board
    display_board()
    # While the same is still going
    while game_still_going:
        # handle a single turn of an arbitrary player
        handle_turn(current_player)
        # check if game has ended
        check_if_game_over()
        # change between X and O
        flip_player()
    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")


# Prompts each player to take a turn
def handle_turn(player):
    print(player + "'s turn.")
    # A while loop to see if the square selected has already been used
    valid = False
    while not valid:
        # Listen out for string or char inputs into the prompt
        try:
            # prompt the user for a position and subtract 1 to get correct position numbers
            position = int(input("Choose a position from 1-9: "))
            position = position - 1
            # Check if the current square is occupied
            if board[position] == "-":
                valid = True
            # Display an error if the player uses an occupied square
            else:
                print("You can't go there")
        # Print an error if the value is not an integer input
        except ValueError:
            print("Enter a integer please")
    # Cast a X or a O to the board
    board[position] = player
    display_board()


# runs the commands for the win or draw conditions
def check_if_game_over():
    check_if_winner()
    check_if_tie()


# Sees if either player has won the game
def check_if_winner():

    global winner
    # Player won on rows
    row_winner = check_rows()
    # Player won on columns
    column_winner = check_columns()
    # Player won on diagonal
    diagonal_winner = check_diagonals()
    # A list of outputs for each win type
    if row_winner:
        winner = row_winner
        print("Good row win!")
    elif column_winner:
        winner = column_winner
        print("good Column win!")
    elif diagonal_winner:
        winner = diagonal_winner
        print("Cheeky Diagonal Win!")
    # The default value
    else:
        winner = None


# Conditions for row wins
def check_rows():
    # Function will only run if game_still_going == True
    global game_still_going
    # Each potential win state
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # Instigate the end of the game
    if row_1 or row_2 or row_3:
        game_still_going = False
    # Return the first row number value for each row win
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


# Conditions for column wins
def check_columns():
    # Function will only run if game still going == True
    global game_still_going
    # Each potential win state
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # Instigate the end of the game
    if column_1 or column_2 or column_3:
        game_still_going = False
    # Return the first column number value for each column win
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


# Conditions for column wins
def check_diagonals():
    # Function will only run if game still going == True
    global game_still_going
    # Each potential win state
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    # Instigate the end of the game
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # Return the first diagonal number value for each column win
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return


# Conditions for a tie
def check_if_tie():
    # Function will only run if game still going == True
    global game_still_going
    # Conditions to instigate end game as a tie
    if "-" not in board:
        game_still_going = False
    return


# Alternates which player it is (each go)
def flip_player():
    # Takes the initial current player value and changes the value output into the game
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"


# Run the game
play_game()