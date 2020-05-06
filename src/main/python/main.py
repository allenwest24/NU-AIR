# Imports required for this PyQt app.
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# Classes needed in main.
from UI import UI

# General basic imports.
import sys
import os

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = UI()              # 1. Instantiate UI
    sys.exit(app.exec())   # 2. Invoke appctxt.app.exec_()
