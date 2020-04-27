# Imports required for any PyQt app.
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# Assorted basic imports.
import sys
import os

class AppContext(ApplicationContext):

    def run(self):
        window = QMainWindow()
        window.resize(500, 500)
        window.setWindowTitle("NU-AIR: (NU And Improved Registration)")
        label = QLabel("Welcome Screen:")
        label.setAlignment(Qt.AlignCenter)
        window.setCentralWidget(label)
        window.show()
        # TODO: Allen setup work
        return self.app.exec_()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    appctxt = AppContext()       # 1. Instantiate ApplicationContext
    exit_code = appctxt.run()    # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
