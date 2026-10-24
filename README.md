# Escape Room

A simple text-based escape room game written in Python. Made as a CBSE Class 12 Computer Science practical project.

## About

You are locked in a room. Find the key and the secret 3-digit code, then open the door before you run out of moves. Every search needs a correct riddle answer.

The key, the code note, and the riddles are random each game, so every round is different.

## Requirements

- Python 3.6 or higher
- No external libraries (only the built-in `random` module)

## How to Run

```
python escape_room.py
```

## How to Play

1. You start with 8 moves.
2. Choose a menu option:
   - 1: Search a spot (desk, shelf, drawer, painting, box, carpet)
   - 2: Try the door
   - 3: Check inventory
   - 4: Quit
3. Searching a spot costs 1 move. You must answer a riddle correctly to search it. A wrong answer still costs the move.
4. One spot hides the key. Another hides a note with the code.
5. Trying the door costs 1 move. You need the key and the correct code to escape.
6. If your moves reach 0, you lose.

## Concepts Used

- Functions
- Lists and tuples
- Loops (`while`, `for`)
- Conditional statements (`if`, `elif`, `else`)
- String methods (`strip`, `lower`, `isdigit`)
- The `random` module (`randint`, `sample`, `choice`)
- Return values

## Project Structure

```
escape_room.py
README.md
```
