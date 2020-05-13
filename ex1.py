from PySide2.QtWidgets import  *

app = QApplication([])
mainWidget = QWidget()

layout = QVBoxLayout()

label = QLabel("Ceci est un QLabel")
button = QPushButton("Ceci est un QPushButton")
progressBar = QProgressBar()
scrollBar = QScrollBar()

layout.addWidget(label)
layout.addWidget(button)
layout.addWidget(progressBar)
layout.addWidget(scrollBar)
mainWidget.setLayout(layout)
mainWidget.setLayout(layout)

mainWidget.show()
app.exec_()