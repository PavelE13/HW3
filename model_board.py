class Board:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # создаем пустую доску с пробелами вместо пустых строк

    def get_board(self):
        return self.board  # возвращаем текущее состояние доски

    def set_position(self, position, player):
        self.board[position] = player  # ставим фишку игрока на заданную позицию

    def is_position_empty(self, position):
        return self.board[position] == ' '  # проверяем, свободна ли заданная позиция

    def check_win(self, player):
        # проверяем, выиграл ли заданный игрок
        return ((self.board[0] == player and self.board[1] == player and self.board[2] == player) or
                (self.board[3] == player and self.board[4] == player and self.board[5] == player) or
                (self.board[6] == player and self.board[7] == player and self.board[8] == player) or
                (self.board[0] == player and self.board[3] == player and self.board[6] == player) or
                (self.board[1] == player and self.board[4] == player and self.board[7] == player) or
                (self.board[2] == player and self.board[5] == player and self.board[8] == player) or
                (self.board[0] == player and self.board[4] == player and self.board[8] == player) or
                (self.board[2] == player and self.board[4] == player and self.board[6] == player))