# Tic Tac Toe Game
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([s == letter for s in row]):
            return True

        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([s == letter for s in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal2]):
                return True

        return False
    
def play(game, x_player, o_player):
    game.print_board()
    letter = 'X'
    while game.available_moves():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            print(f"{letter} makes a move to square {square}")
            game.print_board()

            if game.current_winner:
                print(f"{letter} wins!")
                return letter

            letter = 'O' if letter == 'X' else 'X'

    print("It's a tie!")

def get_move(self, game):
    square = input("Input move (0-8): ")
    valid_square = False
    val = None
    while not valid_square:
        try:
            val = int(square)
            if val not in game.available_moves():
                raise ValueError
            valid_square = True
        except ValueError:
            square = input("Invalid move. Input move (0-8): ")
    return val

def human_move(self, game):
    return self.get_move(game)

def random_move(self, game):
    square = r.choice(game.available_moves())
    return square

play(TicTacToe(), HumanPlayer('X'), RandomComputerPlayer('O'))