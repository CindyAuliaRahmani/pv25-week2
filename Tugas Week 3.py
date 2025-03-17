import sys
import random
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt6.QtGui import QMouseEvent

class MouseTracker(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Task Week 3 - (F1D022116 - Cindy Aulia Rahmani)")
        self.setGeometry(100, 100, 450, 400)

        self.label = QLabel(self)
        self.label.setText("x: 0, y: 0")
        self.label.setStyleSheet("font-size: 16px; color: white;")
        self.label.move(200, 150) 

        self.setMouseTracking(True)

    def mouseMoveEvent(self, event: QMouseEvent):
        x = int(event.position().x())
        y = int(event.position().y())

        xLabel = self.label.x()
        yLabel = self.label.y()
        widthLabel = self.label.width()
        heightLabel = self.label.height()

        if xLabel <= x <= xLabel + widthLabel and yLabel <= y <= yLabel + heightLabel:
            newX = random.randint(0, self.width() - widthLabel)
            newY = random.randint(0, self.height() - heightLabel)
            self.label.move(newX, newY)

        self.label.setText(f"x: {x}, y: {y}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MouseTracker()
    window.show()
    sys.exit(app.exec())
