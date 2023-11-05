import random
from typing import List


class RockPaperScissors:
    """Main class for rock paper scissors game."""
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors'] 

    def get_user_choice(self):
        """This method prompts the user to enter their choice of rock, paper or scissors and returns it as a lowercase string.

        Parameters: self: The instance of the class that contains this method.

        Returns: user_choice: A string that represents the user’s choice of rock, paper or scissors.

        Raises: None

        Examples: >>> game = RockPaperScissors() >>> game.get_user_choice() Enter your choice (rock/paper/scissors): Rock ‘rock’>>> game.get_user_choice() Enter your choice (rock/paper/scissors): lizard Invalid choice. 
        Please make sure your choice is in ‘rock’, ‘paper’ or ‘scissors’. Enter your choice (rock/paper/scissors): scissors ‘scissors’ 
        """
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        
        if user_choice in self.choices:
            return user_choice
        else:
            print("Invalid choice. Please make sure your choice is in 'rock', 'paper' or 'scissors'.")
            return self.get_user_choice()
        
    def get_computer_choice(self):
        """ This method returns a random choice of rock, paper or scissors for the computer.

        Parameters: self: The instance of the class that contains this method.

        Returns: computer_choice: A string that represents the computer’s choice of rock, paper or scissors.

        Raises: None

        Examples: >>> game = RockPaperScissors() >>> game.get_computer_choice() ‘paper’ >>> game.get_computer_choice() ‘rock’ 
        """
        return random.choice(self.choices)
    
    def decide_winner(self, user_choice, computer_choice):
        """This method compares the user’s choice and the computer’s choice of rock, paper or scissors and returns a string that indicates the winner.

        Parameters: self: The instance of the class that contains this method. user_choice: A string that represents the user’s choice of rock, paper or scissors. computer_choice: A string that represents the computer’s choice of rock, paper or scissors.

        Returns: winner: A string that announces the winner of the game. It can be one of the following values: - “It is a Tie!” if the user and the computer have the same choice. - “Congratulations, you won!” if the user’s choice beats the computer’s choice according to the game rules. - “Oh no, the computer won!” if the computer’s choice beats the user’s choice according to the game rules.

        Raises: None

        Examples: >>> game = RockPaperScissors() >>>
        game.decide_winner(‘rock’, ‘scissors’) ‘Congratulations, you won!’ >>> 
        game.decide_winner(‘paper’, ‘paper’) ‘It is a Tie!’ >>>
        game.decide_winner(‘scissors’, ‘rock’) ‘Oh no, the computer won!
        """
        
        if user_choice == computer_choice:
            return ("It is a Tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            return "Congratulations, you won!"
        else:
            return "Oh no, the computer won!"


    def play(self):
        """This method initiates a game of rock, paper or scissors between the user and the computer. It calls the get_user_choice and get_computer_choice methods to obtain the choices of both players, and prints them on the screen. It then calls the decide_winner method to determine and print the winner of the game.

        Parameters: self: The instance of the class that contains this method.

        Returns: None

        Raises: None

        Examples: >>> game = RockPaperScissors() >>>
        game.play() Enter your choice (rock/paper/scissors): paper User choice this paper and computer choice this rock Congratulations, you won!
        """
        user_choice = self.get_user_choice()
        computer_choice = self.get_computer_choice()
        print(f"User choice this {user_choice} and computer choice this {computer_choice}")
        print(self.decide_winner(user_choice, computer_choice))

if __name__ == "__main__" :
    game = RockPaperScissors()
    while True:
        game.play()
        continue_game = input("Do you want to play again? (Enter any key to continue or 'q' to quit): ")
        if continue_game.lower() == 'q':
            break
