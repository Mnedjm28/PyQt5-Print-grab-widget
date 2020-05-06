
import sys

from PyQt5 import QtGui, QtWidgets, QtPrintSupport

class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Create some widgets
        self.setGeometry(100, 100, 800, 650)
        self.button = QtWidgets.QPushButton(
            'Print QTextEdit widget (the one below)', self)
        self.button.setGeometry(20, 20, 260, 30)
        self.editor = QtWidgets.QTextEdit(
            'Wow such text why not change me?', self)
        self.editor.setGeometry(20, 60, 260, 200)

        self.editor2 = QtWidgets.QTextEdit(
            'hhhhhhhhhhhhhhhhhhhhW', self)
        self.editor2.setGeometry(20, 300, 260, 200)

        self.button.clicked.connect(self.print_widget)

    def print_widget(self):
        # Create printer
        printer = QtPrintSupport.QPrinter()
        # Create painter
        painter = QtGui.QPainter()
        # Start painter
        painter.begin(printer)
        # Grab a widget you want to print
        screen = self.grab()
        # Draw grabbed pixmap
        painter.drawPixmap(10, 10, screen)
        # End painting
        painter.end()




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = App()
    gui.show()
    app.exec_()