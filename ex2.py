from PySide2.QtWidgets import *

class IHM(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("IHM")

        self.layout = QGridLayout()

        self.label = QLabel("Laisser un commentaire")
        self.button1 = QPushButton("Success")
        self.button2 = QPushButton("Cancel")
        self.textEdit = QTextEdit()

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.textEdit)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)


        self.setLayout(self.layout)

if __name__ == "__main__":
   app = QApplication([])
   ihm = IHM()
   ihm.show()
   app.exec_()
