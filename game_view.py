class GameView:
    def print_start_mes(self):
        print("Добро пожаловать в игру - крестики-нолики!")  # выводим приветственное сообщение

    def print_board(self, board):
        print('-------------')
        for i in range(3):
            print('|', board[i * 3], '|', board[i * 3 + 1], '|', board[i * 3 + 2], '|')  # выводим состояние доски
            print('-------------')

    def print_winner(self, player):
        print(f"Поздравляем, Игрок {player} победил!")  # выводим сообщение о победе игрока

    def print_nobody_win(self):
        print("Ничья!")  # выводим сообщение о ничьей

    def print_position_bussy(self):
        print("Это место уже занято! Попробуйте еще раз.")  # выводим сообщение об ошибке, если позиция занята