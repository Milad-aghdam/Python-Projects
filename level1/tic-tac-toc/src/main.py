import random

class TicTacToe:
    """A class that represents a tic tac toe game."""

    def __init__(self):
        """Initialize the board and the player turn."""
        self.board: list[str] = [''] * 10  # A list of 10 strings representing the board
        self.player_turn: str = "X"  # A string indicating the current player's turn

    def get_random_first_player(self) -> str:
        """Return a random player to start the game."""
        return random.choice(["O", "X"])

    def show_board(self) -> None:
        """Print the board to the console."""
        print("\n")
        print(self.board[1], "|", self.board[2], "|", self.board[3])
        print("------")
        print(self.board[4], "|", self.board[5], "|", self.board[6])
        print("------")
        print(self.board[7], "|", self.board[8], "|", self.board[9])
        print("\n")

    def swap_player_turn(self) -> str:
        """Swap the player turn and return the new player."""
        self.player_turn = "X" if self.player_turn == "O" else "O"
        return self.player_turn
    
    def has_player_won(self, player: str) -> bool:
        """Return True if the given player has won the game, False otherwise."""
        won: list[list[int]] = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
            [1, 4, 7], [2, 5, 8], [3, 6, 9],  # columns
            [1, 5, 9], [3, 5, 7]  # diagonals
        ]
        for combination in won:
            if all(self.board[i] == player for i in combination):
                return True
        return False

    def fix_spot(self, position: int) -> bool:
        """Fix the player's move on the board and return True if successful, False otherwise."""
        if 1 <= position <= 9 and self.board[position] == "":
            self.board[position] = self.player_turn
            return True
        else:
            print("Invalid move. Try again.")
            return False
        
    def is_board_full(self) -> bool:
        """Return True if the board is full, False otherwise."""
        return "" not in self.board[1:]
    
    def start(self) -> None:
        """Start the game and handle the user input."""
        print("Welcome to Tic Tac Toe game")
        first_player: str = self.get_random_first_player()
        self.player_turn = first_player  # Update the starting player
        print(f"The first player is: {first_player}")

        while True:
            self.show_board()

            try:
                position: int = int(input(f"Player {self.player_turn}, enter your move (1-9): "))

                if 1 <= position <= 9:
                    if self.fix_spot(position):
                        if self.has_player_won(self.player_turn):
                            print(f"Player {self.player_turn} wins!")
                            break

                        if "" not in self.board[1:]:
                            print("It's a tie!")
                            break

                        self.swap_player_turn()
                    else:
                        print("Invalid move. Try again.")
                else:
                    print("Invalid input. Please enter a number between 1 and 9.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    game: TicTacToe = TicTacToe()
    game.start()
