# Bug Fix Report

## Environment

- Operating system: Windows.
- Python version: 3.15.
- Editor: Visual Studio Code.
- Tested script: `tictactoe.py`.
- Initial launch method: Visual Studio Code debugger, started with F5.

The equivalent command for running the script directly from its folder is:

```bash
python tictactoe.py
```

The assignment also specifies `python3 main.py`. The results below concern `tictactoe.py`; they must not be treated as execution results for `main.py`.

## Initial Execution

The first recorded run stopped before symbol selection.

File: `tictactoe.py`  
Function: `run_game()`  
Line: 79 in the initial version.

Error:

```text
TypeError: cannot unpack non-iterable function object
```

The program attempted to unpack the function object `players` instead of calling the function and receiving its result.

## Fix 1 — Missing Function Call

### Original code

```python
player1_symbol, player2_symbol = players
```

### Corrected code

```python
player1_symbol, player2_symbol = players()
```

### Explanation

Parentheses call the function. Its returned pair of symbols can then be assigned to the two player variables.

After this change, execution reached the symbol selection prompt.

## Fix 2 — Converting a Symbol to an Integer

Location: `players()`, line 15 at the time of discovery.

### Original code

```python
result = int(input("Player 1: Do you want to be O or X"))
```

Entering the letter O caused:

```text
ValueError: invalid literal for int() with base 10: 'O'
```

### Corrected code

```python
result = input("Player 1: Do you want to be O or X? ").strip().upper()
```

### Explanation

X and O are text values, so integer conversion is inappropriate. The corrected code keeps the answer as a string.

The added `strip()` removes surrounding spaces, and `upper()` allows lowercase answers.

## Fix 3 — Missing Return Values

Location: `players()`.

Code inspection showed that the original function printed the assigned symbols but did not return them or finish the selection loop after a valid answer.

### Corrected function

```python
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
```

### Explanation

Each valid choice now returns two symbols and exits the function. An invalid answer produces a message and repeats the prompt.

This supplies the values required by the assignment in `run_game()`.

## Fix 4 — Boolean Value Instead of a Player Symbol

Location: the turn-switching statement in `run_game()`, line 98 at the time of correction.

### Original code

```python
current_symbol = player2_symbol if current_symbol == player1_symbol else current_symbol == player1_symbol
```

During a game, the prompt displayed `Player False`, and `False` was placed on the board.

### Corrected code

```python
current_symbol = player2_symbol if current_symbol == player1_symbol else player1_symbol
```

### Explanation

The original expression after `else` performed a comparison and returned a Boolean value.

The corrected expression returns the first player's symbol. Turns therefore alternate between the two selected symbols.

## Verification After Corrections

The recorded successful game used X as the first player's symbol and the following moves:

```text
1, 4, 2, 5, 3
```

| Check | Recorded result |
|---|---|
| Game startup | Reached the symbol selection prompt |
| Selection of X | Assigned X to Player 1 and O to Player 2 |
| Move entry | Accepted cell numbers and updated the board |
| Alternating turns | Used X and O without Boolean values |
| Horizontal victory | Detected the winning X combination in cells 1, 2, and 3 |
| End of a winning game | Displayed the victory message and replay prompt |

Successful output included:

```text
Congratulations ! Player X has won !
Do you want to keep playing (Y or N)?
```

Additional manual checks confirmed the following results:

| Check | Result |
|---|---|
| Selection of O | Player 1 received O and could make the first move |
| New game | Entering Y started another round with a reset board |
| Draw detection | A full board without a winner produced the draw message |
| Exit | Entering N ended the program and returned control to PowerShell |
### Selection of O and a new game

After the previous game, entering Y starts a new round. Selecting O assigns it to Player 1, and the board resets to cells 1–9.

![Selection of O and a new game](screenshots/04_o_and_new_game.png)

### Draw detection

The move sequence 1, 2, 3, 5, 4, 6, 8, 7, 9 fills the board without a winning combination. The game announces a draw.

![Draw detection](screenshots/05_draw.png)

### Exiting the game

Entering N at the replay prompt ends the program and returns control to PowerShell.

![Exiting the game](screenshots/06_exit.png)

## Separate Startup Check of main.py

The original `main.py` was also launched through the Visual Studio Code debugger using F5.

Result: the game started and displayed its interactive prompt. No startup error was observed, and no changes to `main.py` were required.

This check confirms startup only. It does not establish that every gameplay scenario in `main.py` has been tested.

The errors and corrections described earlier in this report apply to `tictactoe.py`.
