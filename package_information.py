"""跑GUI需要安裝的套件:PyQt5

一樣打開之前建好的DIGI_AI環境
輸入pip install PyQt5
這樣就安裝好啦

怎麼看自己有沒有安裝成功?
創一個.py的python程式檔
內容如下:"""
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
    widget.setGeometry(50,50,320,200)
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()