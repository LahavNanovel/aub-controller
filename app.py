import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton)
from PyQt5.QtCore import pyqtSlot
from communicator import Communicator

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.communicator = Communicator()
        self.communicator.turn_off()
        self.state = "off"
        self.initUI()

    def initUI(self):
        self.setFixedWidth(300)
        self.setFixedHeight(200)
        self.button = QPushButton('Turn on', self)
        self.button.clicked.connect(self.on_click)
        self.button.move(100, 70)
        self.show()

    def on_click(self):
        if self.state == "off":
            self.communicator.turn_on()
            self.state = "on"
            self.button.setText("Turn Off")
        else:
            self.communicator.turn_off()
            self.state = "off"
            self.button.setText("Turn On")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
