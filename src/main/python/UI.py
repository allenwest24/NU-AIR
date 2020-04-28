from PyQt5 import QtGui
from PyQt5.QtWidgets import *
import sys

class UI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "NU-AIR"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        # TODO: Allen - Find and set the icon for top left corner next to title.
        #self.setWindowIcon(QtGui.QIcon(""))
        self.InitButtons()
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def InitButtons(self):
        # Add all widgets
        self.home = QPushButton("Home", self)
        self.priority = QPushButton('By Priority', self)
        self.upload = QPushButton('Upload Mock Schedule', self)
        self.create = QPushButton('Make Schedule', self)
        self.credits = QPushButton('Credits', self)

        self.home.clicked.connect(self.button1)
        self.priority.clicked.connect(self.button2)
        self.upload.clicked.connect(self.button3)
        self.create.clicked.connect(self.button4)
        self.credits.clicked.connect(self.button5)

        # Add tabs
        self.tab1 = self.ui1()
        self.tab2 = self.ui2()
        self.tab3 = self.ui3()
        self.tab4 = self.ui4()
        self.tab5 = self.ui5()

        self.initUI()

    def initUI(self):
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.home)
        left_layout.addWidget(self.priority)
        left_layout.addWidget(self.upload)
        left_layout.addWidget(self.create)
        left_layout.addWidget(self.credits)
        left_layout.addStretch(5)
        left_layout.setSpacing(20)
        left_widget = QWidget()
        left_widget.setLayout(left_layout)

        self.right_widget = QTabWidget()
        self.right_widget.tabBar().setObjectName("mainTab")

        self.right_widget.addTab(self.tab1, '')
        self.right_widget.addTab(self.tab2, '')
        self.right_widget.addTab(self.tab3, '')
        self.right_widget.addTab(self.tab4, '')
        self.right_widget.addTab(self.tab5, '')

        self.right_widget.setCurrentIndex(0)
        self.right_widget.setStyleSheet('''QTabBar::tab{width: 0; \
            height: 0; margin: 0; padding: 0; border: none;}''')

        main_layout = QHBoxLayout()
        main_layout.addWidget(left_widget)
        main_layout.addWidget(self.right_widget)
        main_layout.setStretch(0, 40)
        main_layout.setStretch(1, 200)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    # Set buttons
    def button1(self):
        self.right_widget.setCurrentIndex(0)

    def button2(self):
        self.right_widget.setCurrentIndex(1)

    def button3(self):
        self.right_widget.setCurrentIndex(2)

    def button4(self):
        self.right_widget.setCurrentIndex(3)

    def button5(self):
        self.right_widget.setCurrentIndex(4)

    # Set pages
    def ui1(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('Home'))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def ui2(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('By Priority'))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def ui3(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('Upload Mock Schedule'))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def ui4(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('Make Schedule'))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def ui5(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('Credits'))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main
