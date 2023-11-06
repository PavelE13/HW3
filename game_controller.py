
from game_view import GameView
from model_board import Board


class GameController:
    def __init__(self):
        self.view = GameView()
        self.model = Board()

    def play_game(self):
        self.view.print_start_mes()  # выводим приветственное сообщение
        self.view.print_board(self.model.get_board())   # выводим текущее состояние доски
        while True:
            # ход первого игрока
            x_choice = int(input("Игрок X, выберите свой ход (1-9): "))  # запрашиваем ход первого игрока
            if not self.model.is_position_empty(x_choice - 1):  # проверяем, свободна ли выбранная позиция
                self.view.print_position_already_taken()  # выводим сообщение об ошибке, если позиция занята
                continue
            self.model.set_position(x_choice - 1, 'X')  # ставим фишку игрока на выбранную позицию
            self.view.print_board(self.model.get_board())   # выводим обновленное состояние доски
            if self.model.check_win('X'):   # проверяем, выиграл ли первый игрок
                self.view.print_winner('X')  # выводим сообщение о победе первого игрока
                break
            if ' ' not in self.model.get_board():  # проверяем, закончилась ли игра в ничью
                self.view.print_tie()  # выводим сообщение о ничьей
                break
            # ход второго игрока
            while True:
                o_choice = int(input("Игрок 0, выберите свой ход (1-9): "))  # запрашиваем ход второго игрока
                if not self.model.is_position_empty(o_choice - 1):  # проверяем, свободна ли выбранная позиция
                    self.view.print_position_already_taken()  # выводим сообщение об ошибке, если позиция занята
                    continue
                self.model.set_position(o_choice - 1, 'O')  # ставим фишку игрока на выбранную позицию
                break
            self.view.print_board(self.model.get_board())  # выводим обновленное состояние доски
            if self.model.check_win('O'):  # проверяем, выиграл ли второй игрок
                self.view.print_winner('O')  # выводим сообщение о победе второго игрока
                break