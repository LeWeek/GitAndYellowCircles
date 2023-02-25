from __future__ import annotations

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
import sys
import random
from UI_MainWindow import Ui_MainWindow

SCREEN_SIZE = [500, 500]


class YellowCircles(QMainWindow, Ui_MainWindow):

    def __init__(self: YellowCircles) -> None:

        super().__init__()

        self.setupUi(self)
        self.flag = False
        self.setWindowTitle('Git и желтые окружности')
        self.pushButton.clicked.connect(self.draw)
        self.coords = []

    def draw(self: YellowCircles) -> None:
        self.figure = 'circle'
        self.size = random.randint(10, 100)
        self.color = (255, 255, 0)
        self.flag = True
        self.update()

    def paintEvent(self: YellowCircles, event) -> None:
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(*self.color))
            qp.setBrush(QColor(*self.color))
            self.x, self.y = random.randint(100, SCREEN_SIZE[0] - 100),\
                             random.randint(100, SCREEN_SIZE[1] - 100)
            if self.figure == 'circle':
                qp.drawEllipse(self.x, self.y, self.size, self.size)
            qp.end()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = YellowCircles()
    ex.show()
    sys.exit(app.exec_())
