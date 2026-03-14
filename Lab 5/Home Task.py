# Tic Tac Toe Game
class TicTacToe:
    def __init__(self):
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def display_board(self):
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("--+---+--")
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("--+---+--")
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")

    def player_move(self, position):
        if self.board[position] == " ":
            self.board[position] = "X"
            return True
        return False
    def ai_move(self):
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = "O"
                if self.check_winner("O"):
                    return
                self.board[i] = " "
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = "X"
                if self.check_winner("X"):
                    self.board[i] = "O"
                    return
                self.board[i] = " "
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = "O"
                return
    def check_winner(self, mark):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for condition in win_conditions:
            if all(self.board[i] == mark for i in condition):
                return True
        return False
    def is_draw(self):
        return all(space != " " for space in self.board)
    
def play_game():
    game = TicTacToe()
    while True:
        game.display_board()
        try:
            position = int(input("Enter your move (0-8): "))
            if position < 0 or position > 8:
                print("Invalid position. Try again.")
                continue
            if not game.player_move(position):
                print("Position already taken. Try again.")
                continue
        except ValueError:
            print("Invalid input. Enter a number between 0 and 8.")
            continue
        if game.check_winner("X"):
            game.display_board()
            print("Congratulations! You win!")
            break
        if game.is_draw():
            game.display_board()
            print("It's a draw!")
            break
        game.ai_move()
        if game.check_winner("O"):
            game.display_board()
            print("AI wins! Better luck next time.")
            break

play_game()