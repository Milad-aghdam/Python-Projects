import random

import random

class TicTacToe:

    def __init__(self):
        self.board = [''] * 10
        self.player_turn = "X"

    def get_random_first_player(self):
        return random.choice(["O", "X"])

    def show_board(self):
        print("\n")
        print(self.board[1], "|", self.board[2], "|", self.board[3])
        print("------")
        print(self.board[4], "|", self.board[5], "|", self.board[6])
        print("------")
        print(self.board[7], "|", self.board[8], "|", self.board[9])
        print("\n")

    def swap_player_turn(self):
        self.player_turn = "X" if self.player_turn == "O" else "O"
        return self.player_turn
    
    def has_player_won(self, player):
        won = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
            [1, 4, 7], [2, 5, 8], [3, 6, 9],  # columns
            [1, 5, 9], [3, 5, 7]  # diagonals
        ]
        for combination in won:
            if all(self.board[i] == player for i in combination):
                return True
        return False

    def fix_spot(self, position):
        if 1 <= position <= 9 and self.board[position] == "":
            self.board[position] = self.player_turn
            return True
        else:
            print("Invalid move. Try again.")
            return False
        
    def is_board_full(self):
        return "" not in self.board[1:]
    
    def start(self):
        print("Welcome to Tic Tac Toe game")
        first_player = self.get_random_first_player()
        self.player_turn = first_player  # Update the starting player
        print(f"The first player is: {first_player}")

        while True:
            self.show_board()

            try:
                position = int(input(f"Player {self.player_turn}, enter your move (1-9): "))

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
    game = TicTacToe()
    game.start()
    