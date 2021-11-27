from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
import random
import sys


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Ui.ui", self)
        self.pushButton.clicked.connect(self.draw_)
        self.DRAW = False

    def paintEvent(self, event):
        if self.DRAW:
            p = QPainter()
            p.begin(self)
            self.draw(p)
            p.end()

    def draw_(self):
        self.DRAW = True
        self.repaint()

    def draw(self, p):
        p.setBrush(QColor(255, 255, 0))
        for i in range(random.randint(1, 100)):
            r = random.randint(1, 500)
            p.drawEllipse(random.randint(1, 800), random.randint(1, 600), r, r)


app = QApplication(sys.argv)
main = Main()
main.show()
sys.exit(app.exec())
