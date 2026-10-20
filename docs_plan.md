# Additional Documentation Plan

## Purpose

Expand the README with separate guides for installation, gameplay, troubleshooting, and testing.

The files below are planned documents. This plan does not imply that they have already been created.

## Planned Documents

| File | Purpose | Planned contents |
|---|---|---|
| `docs/installation.md` | Help a new user install and launch the game | Python requirements, version check, ZIP download, Git cloning, opening the project folder, and launch commands |
| `docs/gameplay.md` | Explain how to play | Choosing X or O, cell numbering, alternating turns, occupied cells, winning combinations, draws, restarting, and exiting |
| `docs/troubleshooting.md` | Explain common problems and solutions | Python command not found, incorrect working directory, incorrect script name, entering answers in PowerShell instead of the game, and unsaved changes |
| `docs/testing.md` | Describe repeatable manual checks | Test environment, input sequences, expected results, actual results, and screenshot references |

## Testing Guide Outline

The planned testing guide should cover:

1. Starting the game using the documented command.
2. Selecting X and O.
3. Entering an invalid symbol.
4. Placing a symbol in a free cell.
5. Attempting to use an occupied cell.
6. Entering an out-of-range number or non-numeric move.
7. Checking that players alternate correctly.
8. Winning through a row, column, and diagonal.
9. Completing a game in a draw.
10. Starting a new game with a reset board.
11. Exiting after a completed game.

Each test should record its inputs, expected behavior, actual behavior, and pass or fail result.

## Implementation Order

1. Write the installation guide and check its commands.
2. Write the gameplay guide using the corrected game.
3. Add troubleshooting advice based on observed problems.
4. Write and perform the manual tests.
5. Add links to the completed guides in the README.

## Completion Criteria

The documentation should allow another student to download, launch, play, and test the game without reading its source code.

Instructions must match the submitted version. Test results must distinguish completed checks from planned checks.
