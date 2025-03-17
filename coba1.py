import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel

def window():
    app = QApplication(sys.argv)
    main_window = QWidget()
    text = QLabel(main_window)
    main_window.setWindowTitle("First Window")
    main_window.setGeometry(100, 100, 300, 200)
    text.setText("Belajar PyQt6")
    text.move(110, 85)
    main_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    window()