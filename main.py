import sys
import random
from PyQt6 import QtWidgets
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Кружочки')
        self.setGeometry(100, 100, 1920, 1080)
        self.button = QtWidgets.QPushButton('Нарисовать кружочек', self)
        self.button.setGeometry(10, 10, 100, 30)
        self.button.clicked.connect(self.add_circle)
        self.circles = []

    def add_circle(self):
        x = random.randint(50, self.width() - 50)
        y = random.randint(50, self.height() - 50)
        diameter = random.randint(10, 100)
        color = QColor(random.randint(0, 228), random.randint(0, 228), random.randint(0, 228))
        self.circles.append((x, y, diameter, color))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        for x, y, diameter, color in self.circles:
            painter.setBrush(color)
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(x, y, diameter, diameter)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
