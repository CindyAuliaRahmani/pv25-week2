import sys
from PyQt6.QtWidgets import *

def window():
    app = QApplication(sys.argv)

    w = QWidget()
    b = QLabel(w)

    w.setGeometry(100, 100, 200, 50)

    b.setText("Hello world!")
    b.move(50, 20)

    w.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    window()
