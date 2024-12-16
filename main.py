from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import load_ui
from PyQt6.QtGui import QPixmap, QIcon
import sys


class TikTacToeBoard(QMainWindow):
    def __init__(self):
        super().__init__()
        
    def new_game(self):
        """New game"""
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
    
    def check_field(self):
        pass
    
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
                self.output.setText(f'Игрок \"{self.player}\" походил на {row + 1} ряд {col + 1} колонки')
                self.player = '0'
            elif self.player == '0':
                self.field[row][col] = '0'
                self.output.setText(f'Игрок \"{self.player}\" походил на {row + 1} ряд {col + 1} колонки')
                self.player = 'X'
        else:
            self.output.setText(f'Ход невозможен, т.к ход уже был сделан игроком \"{button.text()}\"')
        self.check_field()
        
                
        
    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TikTacToeBoard()
    ex.show()
    app.exec()