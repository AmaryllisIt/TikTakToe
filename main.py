from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import load_ui
from PyQt6.QtGui import QPixmap, QIcon
import sys
from ui_ui import Ui_MainWindow


class TikTacToeBoard(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Крестики-Нолики')
        self.setFixedSize(600, 600)

        self.btns = [[self.btn_1, self.btn_2, self.btn_3],
                     [self.btn_4, self.btn_5, self.btn_6],
                     [self.btn_7, self.btn_8, self.btn_9]
                     ]

        for row in self.btns:
            for col in row:
                col.clicked.connect(self.make_move)
                col.setDisabled(True)
        self.btnStart.clicked.connect(self.new_game)
        self.output.setDisabled(True)

    def new_game(self):
        """New game"""
        self.player = 'X'
        self.winner = False
        self.output.setText('')
        self.field = [["?" for _ in range(3)] for _ in range(3)]
        for i in range(len(self.btns)):
            for j in range(len(self.btns[i])):
                self.btns[i][j].setText('?')
        self.btnStart.setDisabled(True)
        self.btnStart.setText('Начать новую игру')
        for row in self.btns:
            for button in row:
                button.setDisabled(False)

    def config(self):
        pass

    def block_buttons(self):
        for row in self.btns:
            for col in row:
                col.setDisabled(True)

    def check_field(self):
        diags = [[self.field[i][i] for i in range(len(self.field[0]))],
                 [self.field[i][len(self.field[0]) - 1 - i] for i in range(len(self.field[0]))]]
        rows = [[self.field[i][j] for i in range(
            len(self.field[0]))] for j in range(len(self.field[0]))]
        cols = self.field[:]

        # Checking...
        for i in range(len(diags)):
            if (diags[i].count(diags[i][0]) == len(diags[i])) and diags[i][0] != '?':
                self.winner = 'X' if self.player == '0' else '0'
                self.block_buttons()
                self.output.setText(f'Игра завершена!\nПобедил игрок "{self.winner}"')
                self.btnStart.setDisabled(False)

        for i in range(len(rows)):
            if (rows[i].count(rows[i][0]) == len(rows[i])) and rows[i][0] != '?':
                self.winner = 'X' if self.player == '0' else '0'
                self.block_buttons()
                self.output.setText(f'Игра завершена!\nПобедил игрок "{self.winner}"')
                self.btnStart.setDisabled(False)

        for i in range(len(cols)):
            if (cols[i].count(cols[i][0]) == len(cols[i])) and cols[i][0] != '?':
                self.winner = 'X' if self.player == '0' else '0'
                self.block_buttons()
                self.output.setText(f'Игра завершена!\nПобедил игрок "{self.winner}"')
                self.btnStart.setDisabled(False)

        if '?' not in str(self.field) and not self.winner:
            self.winner = None
            self.output.setText(f'Игра завершена!\nНичья')
            self.block_buttons()
            self.btnStart.setDisabled(False)

    def make_move(self):
        """make move in field"""
        row, col = 0, 0
        button = self.sender()

        if int(button.objectName()[-1]) <= 3:
            col = int(button.objectName()[-1]) - 1
        elif 3 < int(button.objectName()[-1]) <= 6:
            row = 1
            col = int(button.objectName()[-1]) - 4
        elif 6 < int(button.objectName()[-1]) <= 9:
            row = 2
            col = int(button.objectName()[-1]) - 7

        if self.field[row][col] == '?':
            if self.player == 'X':
                self.field[row][col] = 'X'
                button.setText('X')
                self.output.setText(f'Игрок \"{self.player}\" походил на {
                                    row + 1} ряд {col + 1} колонки')
                self.player = '0'
            elif self.player == '0':
                self.field[row][col] = '0'
                button.setText('0')
                self.output.setText(f'Игрок \"{self.player}\" походил на {
                                    row + 1} ряд {col + 1} колонки')
                self.player = 'X'
        else:
            self.output.setText(
                f'Ход невозможен, т.к ход уже был сделан игроком \"{button.text()}\"')
        self.check_field()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TikTacToeBoard()
    ex.show()
    app.exec()
