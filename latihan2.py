# import sys
# from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QLabel

# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.setGeometry(100, 100, 200, 150)
#         self.setWindowTitle("Signal & Slot (Button Clicked)")
#         layout = QVBoxLayout()
#         button = QPushButton("Cetak")
#         self.label= QLabel("")
#         layout.addWidget(self.label)
#         layout.addWidget(button)
        
#         self.setLayout(layout)
#         button.clicked.connect(self.proses_cetak)
        

#     def proses_cetak(self):
#         self.label.setText("Tombol cetak di klik!")

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())
import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QLabel

class ResultWindow(QWidget):
    def __init__(self, message):
        super().__init__()
        self.setWindowTitle("Hasil Cetak")
        self.setGeometry(150, 150, 200, 100)
        
        layout = QVBoxLayout()
        label = QLabel(message)
        layout.addWidget(label)
        self.setLayout(layout)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 200, 150)
        self.setWindowTitle("Signal & Slot (Button Clicked)")
        
        layout = QVBoxLayout()
        self.button = QPushButton("Cetak")
        layout.addWidget(self.button)
        self.setLayout(layout)
        
        self.button.clicked.connect(self.proses_cetak)

    def proses_cetak(self):
        self.result_window = ResultWindow("Tombol cetak diklik!")
        self.result_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
