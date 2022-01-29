from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


def bordure_case(painter, option, ligne):
    """ permet de mettre en gras la bordure d'une case """
    r = option.rect
    x, y, w, h = r.x(), r.y(), r.width(), r.height()
    if ligne=='h':
        x1, y1, x2, y2 = x, y, x+w, y
    elif ligne=='d':
        x1, y1, x2, y2 = x+w, y, x+w, y+h
    elif ligne=='b':
        x1, y1, x2, y2 = x+w, y+h, x, y+h
    elif ligne=='g':
        x1, y1, x2, y2 = x, y+h, x, y
    else:
        return
    pen = QPen()
    pen.setWidth(2)
    painter.setPen(pen)
    painter.drawLine(x1, y1, x2, y2)


class Delegate(QItemDelegate):

    def __init__(self, parent: None):
        super(Delegate, self).__init__(parent)

    def grille_init(self, g):
        self.g0 = g

    def paint(self, painter, option, index):
        """ appelé case par case pour en dessiner le contenu"""
        
        row, col = index.row(), index.column()
        if row == 0 or row == 3 or row == 6:
            if col in[0, 3, 6]:
                bordure_case(painter, option, 'g')
                bordure_case(painter, option, 'h')
            elif col == 8:
                bordure_case(painter, option, 'd')
                bordure_case(painter, option, 'h')
            else:
                bordure_case(painter, option, 'h')
        elif row in [1, 2, 4, 5, 7]:
            if col in [0,3,6]:
                bordure_case(painter, option, 'g')
            elif col == 8:
                bordure_case(painter, option, 'd')
        elif row == 8:
            if col in [0, 3, 6]:
                bordure_case(painter, option, 'g')
                bordure_case(painter, option, 'b')
            elif col == 8:
                bordure_case(painter, option, 'd')
                bordure_case(painter, option, 'b')
            else:
                bordure_case(painter, option, 'b')

        
        QItemDelegate.paint(self, painter, option, index)


