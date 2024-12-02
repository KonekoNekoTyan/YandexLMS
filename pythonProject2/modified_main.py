from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QRect
import sys
import random
from PyQt6.QtWidgets import QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Случайные окружности")

        # Виджет
        self.central_widget = QWidget()
        self.layout = QVBoxLayout(self.central_widget)

        # Кнопка
        self.draw_button = QPushButton("Нарисовать окружности")
        self.layout.addWidget(self.draw_button)

        # Основное окно
        self.setCentralWidget(self.central_widget)

        # Список кругов
        self.circles = []

        # Сигнал-слот
        self.draw_button.clicked.connect(self.add_circle)

    def add_circle(self):
        # Добавляем рандомные круги с цветом
        x = random.randint(50, self.width() - 50)
        y = random.randint(50, self.height() - 50)
        radius = random.randint(10, 100)
        color = QColor(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        self.circles.append((x, y, radius, color))
        self.update()  # Перерисовать форму

    def paintEvent(self, event):
        # Рисуем круги
        painter = QPainter(self)
        for x, y, radius, color in self.circles:
            painter.setBrush(color)
            painter.drawEllipse(QRect(x, y, radius, radius))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
