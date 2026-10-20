# Tic Tac Toe — Python CLI Game

A two-player Tic Tac Toe game played in the terminal. Players share one computer, choose X or O, and take turns placing their symbols on a 3 × 3 board.

This version was prepared as a coursework project involving testing, bug fixing, and documentation improvements.

Original project: https://github.com/ERYXGF/tictactoe_python

## Requirements

- Python 3 installed on your computer.
- A terminal for running the game and entering moves.
- Optional: Visual Studio Code for editing and running the project.

The coursework version was tested on Windows using Python 3.15 and Visual Studio Code.

## Installation

### Download as ZIP

1. Open https://github.com/geraldmudryj/tictactoe_python.
2. Click Code → Download ZIP.
3. Extract the downloaded archive.
4. In Visual Studio Code, select File → Open Folder and open the extracted project folder.
5. Select Terminal → New Terminal.

Make sure the terminal is opened in the folder containing `tictactoe.py`.

### Clone with Git

If Git is installed, you can download the project using:

```bash
git clone https://github.com/geraldmudryj/tictactoe_python.git
cd tictactoe_python
```

## Running the Game

Check your Python version:

```bash
python --version
```

Run the corrected game:

```bash
python tictactoe.py
```

On Windows, if the `python` command is unavailable and Python Launcher is installed, try:

```bash
py tictactoe.py
```

On macOS or Linux, you may need:

```bash
python3 tictactoe.py
```

The game will ask Player 1 to choose X or O.

## How to Play

1. Player 1 chooses the English letter X or O. Player 2 receives the other symbol.
2. Player 1 makes the first move.
3. Enter the number of an available cell from 1 to 9 and press Enter.
4. Cells 1–3 form the top row, 4–6 the middle row, and 7–9 the bottom row.
5. Players take turns. A cell that already contains a symbol cannot be used again.
6. The first player to place three matching symbols in a row, column, or diagonal wins.
7. If all cells are occupied and neither player has won, the game ends in a draw.

After a game ends, enter:

- Y to start a new game.
- N to exit.

When choosing a symbol, use the English letter O, not the digit 0.

## Project Structure

| File | Description |
|---|---|
| `tictactoe.py` | Corrected game covered by the instructions above |
| `main.py` | Original game script; startup checked successfully without modifications |
| `README.md` | Project description, setup instructions, and game rules |
| `LICENSE` | Original project license |
| `.gitignore` | Rules for excluding temporary and local files from Git |

The coursework documentation is organized into:

- `docs_audit.md` — audit of the original documentation.
- `fix_report.md` — initial execution results, identified bugs, fixes, and verification results.
- `docs_plan.md` — plan for additional documentation.

## Troubleshooting

### Python command is not recognized

Check that Python is installed. On Windows, try `py` instead of `python`. If Python was installed recently, close and reopen the terminal.

### Cannot open file

Make sure the archive has been extracted and the terminal is opened in the folder containing `tictactoe.py`.

### X or O is treated as a PowerShell command

Start the game first. Enter your symbol only after the game asks you to choose X or O.

A prompt beginning with `PS` means PowerShell is waiting for a command.

### Changes do not appear when running the game

Save the file with Ctrl + S, stop the previous run, and start the game again. Check that you are editing and running the file from the same project folder.

### Stopping the game early

Press Ctrl + C in the terminal to interrupt the program.

## License

The original project is distributed under the MIT License. The original license text and copyright notice are retained in `LICENSE`.
