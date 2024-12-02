from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QRect
import sys
import random


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        # Найти кнопку из UI и подключить событие
        self.drawButton = self.findChild(QPushButton, 'drawButton')
        self.drawButton.clicked.connect(self.add_circle)

        # Список кругов
        self.circles = []

    def add_circle(self):
        # Добавляем рандомные круги
        x = random.randint(50, self.width() - 50)
        y = random.randint(50, self.height() - 50)
        radius = random.randint(10, 100)
        self.circles.append((x, y, radius))
        self.update()  # Перерисовать форму

    def paintEvent(self, event):
        # Рисуем круги
        painter = QPainter(self)
        painter.setBrush(QColor('yellow'))
        for x, y, radius in self.circles:
            painter.drawEllipse(QRect(x, y, radius, radius))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
