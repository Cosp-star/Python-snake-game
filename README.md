# Python-snake-game
A simple implementation of the classic Snake game using Python.

## Features
- Basic movement through user input.
- collision detection to the snake's body and to the food pellet.
- Scoreboard to keep track of how many pellets have been consumed.

### main game

![image](https://github.com/user-attachments/assets/e113c7b2-f2ec-4ed3-a0d0-2e5b594d5573)

### Game over screen

![image](https://github.com/user-attachments/assets/96fe0180-2bb6-4da8-975d-f4e4973d1ee1)


## Known issues
- when pressing left and down or right and down at the same time, it will cause the snake to move in the other direction, causing a game over screen.
- the checkhit() method in the Snake class always outputs true when the snake moves for the first time.
