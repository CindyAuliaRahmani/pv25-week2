import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton,
    QRadioButton, QComboBox, QGroupBox
)

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Week 2 : Layout - User Registration Form')

        # Identitas
        identitas_box = QGroupBox('Identitas (vertical box layout)')
        identitas_layout = QVBoxLayout()
        identitas_layout.addWidget(QLabel('Nama : nama_anda'))
        identitas_layout.addWidget(QLabel('Nim : nim_anda'))
        identitas_layout.addWidget(QLabel('Kelas : kelas_anda'))
        identitas_box.setLayout(identitas_layout)

        # Navigation
        nav_box = QGroupBox('Navigation (horizontal box layout)')
        nav_layout = QHBoxLayout()
        nav_layout.addWidget(QPushButton('Home'))
        nav_layout.addWidget(QPushButton('About'))
        nav_layout.addWidget(QPushButton('Contact'))
        nav_box.setLayout(nav_layout)

        # User Registration Form
        form_box = QGroupBox('User Registration (form layout)')
        form_layout = QVBoxLayout()
        
        form_layout.addWidget(QLabel('Full Name:'))
        self.full_name = QLineEdit()
        form_layout.addWidget(self.full_name)
        
        form_layout.addWidget(QLabel('Email:'))
        self.email = QLineEdit()
        form_layout.addWidget(self.email)
        
        form_layout.addWidget(QLabel('Phone:'))
        self.phone = QLineEdit()
        form_layout.addWidget(self.phone)
        
        form_layout.addWidget(QLabel('Gender:'))
        gender_layout = QHBoxLayout()
        self.male_radio = QRadioButton('Male')
        self.female_radio = QRadioButton('Female')
        gender_layout.addWidget(self.male_radio)
        gender_layout.addWidget(self.female_radio)
        form_layout.addLayout(gender_layout)
        
        form_layout.addWidget(QLabel('Country:'))
        self.country_combo = QComboBox()
        self.country_combo.addItems(['Select', 'USA', 'UK', 'Indonesia', 'India'])
        form_layout.addWidget(self.country_combo)
        
        form_box.setLayout(form_layout)

        # Actions
        action_box = QGroupBox('Actions (horizontal box layout)')
        action_layout = QHBoxLayout()
        action_layout.addWidget(QPushButton('Submit'))
        action_layout.addWidget(QPushButton('Cancel'))
        action_box.setLayout(action_layout)

        # Main Layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(identitas_box)
        main_layout.addWidget(nav_box)
        main_layout.addWidget(form_box)
        main_layout.addWidget(action_box)

        self.setLayout(main_layout)
        self.resize(400, 350)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RegistrationForm()
    window.show()
    sys.exit(app.exec())