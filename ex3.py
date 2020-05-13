from PySide2.QtWidgets import *
from PySide2.QtGui import *

class HelloWorld(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setFixedSize(400, 300)
        self.setWindowTitle("IHM")

        self.setWindowIcon(QIcon("fr-flag.png")) #chemin de l'image

        self.layout = QVBoxLayout()

        self.label = QLabel("Hello World")
        self.label.setAlignment(Qt.AlignCenter)

        self.progressBar = QProgressBar()
        self.progressBar.setValue(50)

        self.lineEdit = QLineEdit()
        self.button = QPushButton("Click me !")
        self.button.setToolTip("Hello World")

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.progressBar)
        self.layout.addWidget(self.lineEdit)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)



if __name__ == "__main__":
   app = QApplication([])
   ihm = HelloWorld()
   ihm.show()
   app.exec_()
