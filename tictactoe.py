#FIRST MILESTONE PROJECT IN UDEMY: CREATING AN INTERACTIVE TICTACTOE GAME.
"""
Rules:
1) Two players should be able to play the game.
2) The board should be printed out after every move.
3) You should be able to accept the input of the player position and then place a symbol on the board.
4) The game can also finish in a draw.
"""

grid = [1,2,3,4,5,6,7,8,9]                                                               


def players():
    while True:
        result = input("Player 1: Do you want to be O or X? ").strip().upper()

        if result == "X":
            print("Player 1 is X and Player 2 is O")
            return "X", "O"
        elif result == "O":
            print("Player 1 is O and Player 2 is X")
            return "O", "X"
        else:
            print("Please choose either X or O")


def display(grid):
    print(grid[0:3])
    print(grid[3:6])
    print(grid[6:9])


def player_move(grid, symbol):
    while True:
        try:
            result = int(input(f"Player {symbol}, choose your next position (1-9):"))
            if result not in range(1,10):
                print("That number is not in the required range.")
                continue
            elif grid[result-1] in ["X","O"]:
                print("That position is already taken.")
                continue
            grid[result-1] = symbol
            break
        except ValueError:
            print("Please input a number.")


def finished(grid, symbol):
    winning_list = (
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
)
    for (a,b,c) in winning_list:
        if grid[a] == grid[b] == grid[c] == symbol:
            return True   
    return False


def draw(grid):
    return all(case in ("X","O") for case in grid)


def keep_playing():
    while True:
        answer = input("Do you want to keep playing (Y or N)? ")
        if answer in ("Y","y","yes"):
            return True
        if answer in ("N","n","no"):
            return False
        else:
            print("Please enter either yes or no. ")


def run_game():   
    play = True

    while play:
        grid = [1,2,3,4,5,6,7,8,9]
        player1_symbol, player2_symbol = players()
        current_symbol = player1_symbol

        while True:
            display(grid)
            player_move(grid, current_symbol)

            if finished(grid, current_symbol):
                display(grid)
                print(f"Congratulations ! Player {current_symbol} has won !")
                break

            if draw(grid):
                display(grid)
                print("This game has ended in a draw.")
                break

            current_symbol = player2_symbol if current_symbol == player1_symbol else player1_symbol
        
        play = keep_playing()

if __name__ == "__main__":
    run_game()
