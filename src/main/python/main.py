# Imports required for any PyQt app.
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# Assorted basic imports.
import sys
import os

SIZE_UNIT = 500

class AppContext(ApplicationContext):

    def run(self):
        self.window = QWidget()
        self.window.setGeometry(0, 0, SIZE_UNIT, SIZE_UNIT)
        self.window.setWindowTitle("NU-AIR: (NU And Improved Registration)")
        self.label = QLabel(self.window)
        self.label.setText("Welcome to the app")
        self.label.move(SIZE_UNIT / 2 - 45, SIZE_UNIT / 4)
        self.start_button = QPushButton("Start!", self.window)
        self.start_button.resize(100, 25)
        self.start_button.move(SIZE_UNIT / 2 - 50, SIZE_UNIT / 2)
        self.start_button.clicked.connect(self.clickMethod)
        self.window.show()
        self.start_button.show()

        # TODO: Allen setup work
        return self.app.exec_()

    def clickMethod(self):
        print('Clicked Start.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    appctxt = AppContext()       # 1. Instantiate ApplicationContext
    exit_code = appctxt.run()    # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
