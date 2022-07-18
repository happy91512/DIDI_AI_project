import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

def window():
    app = QApplication(sys.argv)
    widget = QWidget()
    textLabel = QLabel(widget)
    textLabel.setText("Hello World!")
    textLabel.move(110,85)
    TimeEdit.setFont(font)
    TimeEdit.setStyleSheet("background-color:rgb(170, 170, 255);")
    TimeEdit.setFrame(False)
    TimeEdit.setAlignment(QtCore.Qt.AlignCenter)
    TimeEdit.setMinimumDate(QtCore.QDate(2022, 7, 18))
    TimeEdit.setObjectName("TimeEdit")
    widget.setGeometry(50,50,320,200)
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()