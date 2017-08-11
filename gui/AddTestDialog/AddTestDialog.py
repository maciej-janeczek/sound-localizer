from PyQt5 import QtWidgets
from core.user import Gender, User
from core.test import ProcedureType


class AddTestDialog(QtWidgets.QDialog):
    NumGridRows = 3
    NumButtons = 4
    name = ''
    age = '25'
    gender = Gender.MALE
    procedure = ProcedureType.BASIC
    iterations = 20

    def __init__(self):
            super().__init__()
            self.createFormGroupBox()

            buttonBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
            buttonBox.accepted.connect(self.accept)
            buttonBox.rejected.connect(self.reject)

            mainLayout = QtWidgets.QVBoxLayout()
            mainLayout.addWidget(self.formGroupBox)
            mainLayout.addWidget(buttonBox)
            self.setLayout(mainLayout)

            self.setWindowTitle("Add User")

    def createFormGroupBox(self):
        self.formGroupBox = QtWidgets.QGroupBox("Test settings")
        layout = QtWidgets.QFormLayout()
        self.name_line = QtWidgets.QLineEdit()
        layout.addRow(QtWidgets.QLabel("Name:"), self.name_line)

        self.age_box = QtWidgets.QSpinBox()
        self.age_box.setValue(25)
        layout.addRow(QtWidgets.QLabel("Age:"), self.age_box)

        self.gender_box = QtWidgets.QComboBox()
        self.gender_box.addItem("N/A")
        self.gender_box.addItem("Male")
        self.gender_box.addItem("Female")
        layout.addRow(QtWidgets.QLabel("Gender:"), self.gender_box)

        self.procedure_box = QtWidgets.QComboBox()
        self.procedure_box.addItem("Basic")
        layout.addRow(QtWidgets.QLabel("Procedure:"), self.procedure_box)
        self.formGroupBox.setLayout(layout)

    def accept(self):
        self.name = self.name_line.text()
        self.age = self.age_box.value()
        self.gender = Gender(self.gender_box.currentText())
        self.procedure = ProcedureType(self.procedure_box.currentText())
        super().accept()
