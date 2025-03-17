import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QGroupBox,QHBoxLayout, QPushButton, QFormLayout, QLineEdit, QRadioButton, QComboBox
)

class MainWindow(QWidget):  
    def __init__(self):  
        super().__init__()  

        # Set window properties  
        self.setWindowTitle("Week 2 : Layout - User Registration Form")  
        self.setGeometry(100, 100, 500, 700)  

        # Buat GroupBox untuk Identitas  
        layout_grup = QGroupBox("Identitas (vertical box layout)")  
        layout_atas = QVBoxLayout() 
        
        
        # Tambahkan label ke dalam layout  
        layout_atas.addWidget(QLabel("Nama  : Agus"))  
        layout_atas.addWidget(QLabel("NIM   : 124"))  
        layout_atas.addWidget(QLabel("Kelas : c"))  
        
        self.setFixedSize(500,200)
        
        layout_grup.setLayout(layout_atas)  # Set layout ke GroupBox 

        layout_grupdua = QGroupBox("Navigation (horizontal box layout)")
        layout_tengah = QHBoxLayout()
        layout_tengah.addWidget(QPushButton("Home"))
        layout_tengah.addWidget(QPushButton("About"))
        layout_tengah.addWidget(QPushButton("Contact"))
        
        self.setFixedSize(500,200)
        
        layout_grupdua.setLayout(layout_tengah)
        
        layout_gruptiga = QGroupBox("User Registration (Form Layout)")
        layout_tiga = QFormLayout()
        
        self.nama_input = QLineEdit()
        self.email_input = QLineEdit()
        self.telp_input = QLineEdit()
        
        layout_gender = QHBoxLayout()
        self.cw = QRadioButton("Male")
        self.cwk = QRadioButton("Female")
        layout_gender.addWidget(self.cw)
        layout_gender.addWidget(self.cwk)
        
        self.country = QComboBox()
        self.country.addItems(["Select", "Indonesia", "Malaysia", "Thailand", "Korea", "Brunei"])
        
        layout_tiga.addRow("Full Name :", self.nama_input)
        layout_tiga.addRow("Email :", self.email_input)
        layout_tiga.addRow("Phone :", self.telp_input)
        layout_tiga.addRow("Gender :", layout_gender)
        layout_tiga.addRow("Country :", self.country)
        layout_gruptiga.setLayout(layout_tiga)
        
        self.setFixedSize(500,200)
        

        layout_grupempat = QGroupBox("Actions(horizontal box layout)")
        layout_akhir = QHBoxLayout()
        layout_akhir.addWidget(QPushButton("Submit"))
        layout_akhir.addWidget(QPushButton("Cancel"))
        
        
        self.setFixedSize(500,400)
        
        layout_grupempat.setLayout(layout_akhir)
        

        # Buat layout utama  
        
        main_layout = QVBoxLayout()  
        main_layout.addWidget(layout_grup)# Tambahkan GroupBox ke layout utama  
        main_layout.addWidget(layout_grupdua)
        main_layout.addWidget(layout_gruptiga)
        main_layout.addWidget(layout_grupempat)
        

        self.setLayout(main_layout)  # Set layout utama ke window  

if __name__ == "__main__":  
    app = QApplication(sys.argv)  
    window = MainWindow()  
    window.show()  
    sys.exit(app.exec())  