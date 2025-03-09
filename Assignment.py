import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QLineEdit, 
    QRadioButton, QComboBox, QVBoxLayout, QHBoxLayout, QFormLayout, QGroupBox
)

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Week 2 : Layout - User Registration Form")
        self.setGeometry(100, 100, 400, 500)

        mainLayout = QVBoxLayout()

        labelIdentitas = QLabel("Identitas (vertical box layout)")
        mainLayout.addWidget(labelIdentitas)

        groupIdentitas = QGroupBox()
        layoutIdentitas = QVBoxLayout()
        layoutIdentitas.addWidget(QLabel("Nama  : Cindy Aulia Rahmani"))
        layoutIdentitas.addWidget(QLabel("Nim   : F1D022116"))
        layoutIdentitas.addWidget(QLabel("Kelas : C"))
        groupIdentitas.setLayout(layoutIdentitas)

        mainLayout.addWidget(groupIdentitas)

        labelNavigation = QLabel("Navigation (horizontal box layout)")
        mainLayout.addWidget(labelNavigation)

        groupNavigation = QGroupBox()
        layoutNavigation = QHBoxLayout()
        layoutNavigation.addWidget(QPushButton("Home"))
        layoutNavigation.addWidget(QPushButton("About"))
        layoutNavigation.addWidget(QPushButton("Contact"))
        groupNavigation.setLayout(layoutNavigation)

        mainLayout.addWidget(groupNavigation)

        labelReg = QLabel("User Registration (form layout)")
        mainLayout.addWidget(labelReg)

        groupReg = QGroupBox()
        layoutReg = QFormLayout()
        layoutReg.addRow("Full Name:", QLineEdit())
        layoutReg.addRow("Email:", QLineEdit())
        layoutReg.addRow("Phone:", QLineEdit())

        layoutGender = QHBoxLayout()
        layoutGender.addWidget(QRadioButton("Male"))
        layoutGender.addWidget(QRadioButton("Female"))
        layoutReg.addRow("Gender:", layoutGender)

        self.country = QComboBox()
        self.country.addItems(["Select", "Indonesia", "Singapura", "Malaysia", "Thailand", "Vietnam"])
        layoutReg.addRow("Country:", self.country)

        groupReg.setLayout(layoutReg)

        mainLayout.addWidget(groupReg)

        actionLabel = QLabel("Actions (horizontal box layout)")
        mainLayout.addWidget(actionLabel)

        actionGroup = QGroupBox()
        actionLayout = QHBoxLayout()
        actionLayout.addWidget(QPushButton("Submit"))
        actionLayout.addWidget(QPushButton("Cancel"))
        actionGroup.setLayout(actionLayout)

        mainLayout.addWidget(actionGroup)

        self.setLayout(mainLayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegistrationForm()
    window.show()
    sys.exit(app.exec())
