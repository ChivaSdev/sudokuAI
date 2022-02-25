from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

import sys


class AideMiniBouton(QtWidgets.QPushButton):

    def __init__(self, content, x, y, selected, label):
        super().__init__()
        self.content = content
        self.label = label
        self.x = x
        self.y = y
        self.selected = selected
        self.button = QtWidgets.QPushButton(self.content, self)
        
        self.button.setStyleSheet(
            "border-style: solid; background: #87CEFA; color: white; padding: 0px; padding-bottom: 1px;  ")
        self.button.setGeometry(QtCore.QRect(1, 0, 17, 13))
        if self.selected:
            self.button.pressed.connect(self.change_Content)
            self.button.setStyleSheet("background:white; border-style: solid;padding-bottom: 1px;") 

    # Logique Pricipale du bouton
    def change_Content(self):
        print("click on " +  self.content + " at " + str(self.x) + str(self.y))
        self.label.setText("click on " + self.content + " at [" + str(self.x)+","+ str(self.y)+ "]")
        
