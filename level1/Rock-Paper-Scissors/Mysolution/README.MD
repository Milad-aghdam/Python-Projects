# Rock Paper Scissors Game
This is a simple Python script that allows you to play the classic game of rock, paper or scissors against the computer. The game rules are as follows:

- Rock beats scissors
- Scissors beats paper
- Paper beats rock
If both players have the same choice, it is a tie

## How to run the script
To run the script, you need to have Python 3 installed on your system. You also need to have the random module, which is a built-in module in Python.

To run the script, open a terminal or command prompt and navigate to the folder where the script is located. Then type the following command:

```{bash}
python game.py
```

The script will prompt you to enter your choice of rock, paper or scissors. You can type any of these words in any case (upper or lower). The script will then display the computer’s choice and the winner of the game. You can play as many times as you want. To quit the game, type ‘q’ when asked to play again.

## How the script works
The script uses a class called RockPaperScissors to implement the game logic. The class has the following attributes and methods:

- choices: A list of strings that contains the possible choices of rock, paper or scissors.
- get_user_choice: A method that prompts the user to enter their choice and returns it as a lowercase string. It also validates the input and asks the user to enter again if the input is invalid.
- get_computer_choice: A method that returns a random choice of rock, paper or scissors for the computer using the random module.
- decide_winner: A method that compares the user’s choice and the computer’s choice and returns a string that indicates the winner of the game.
- play: A method that initiates a game of rock, paper or scissors between the user and the computer. It calls the get_user_choice and get_computer_choice methods to obtain the choices of both players, and prints them on the screen. It then calls the decide_winner method to determine and print the winner of the game.

The script also has a main block that creates an instance of the RockPaperScissors class and calls the play method in a loop. The loop breaks when the user types ‘q’ to quit the game.