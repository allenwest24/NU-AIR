# PyQt5 imports.
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui

# Selenium imports
from selenium import webdriver

# Script imports.
from ScriptRunner import ScriptRunner

# General Python imports.
from functools import partial
import sys

# Runs the user interface for the entire application.
class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "NU-AIR (NU-And-Improved-Registration)"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.temp_type = ""

        # TODO: Allen - Find and set the icon for top left corner next to title.
        self.setWindowIcon(QtGui.QIcon('./logo.png'))
        self.InitButtons()
        self.InitWindow()

    # Initializes the main window to the desired parameters.
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    # Initializes the menu buttons to move around the tabs in the app.
    def InitButtons(self):
        # Add all widgets
        self.home = QPushButton("Home", self)
        self.priority = QPushButton('By Priority', self)
        self.upload = QPushButton('Upload Mock Schedule', self)
        self.create = QPushButton('Make Schedule', self)
        self.credits = QPushButton('Credits', self)

        # Connect the main buttons to their tabs.
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
        # Sets up the structure of the widgets that make up the main window.
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

        # Adds the tabs structurally.
        self.right_widget.addTab(self.tab1, '')
        self.right_widget.addTab(self.tab2, '')
        self.right_widget.addTab(self.tab3, '')
        self.right_widget.addTab(self.tab4, '')
        self.right_widget.addTab(self.tab5, '')

        # Style
        self.right_widget.setCurrentIndex(0)
        self.right_widget.setStyleSheet('''QTabBar::tab{width: 0; \
            height: 0; margin: 0; padding: 0; border: none;}''')

        # Puts the layout together.
        main_layout = QHBoxLayout()
        main_layout.addWidget(left_widget)
        main_layout.addWidget(self.right_widget)
        main_layout.setStretch(0, 40)
        main_layout.setStretch(1, 200)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    # Set buttons.
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

    # Set pages.
    def ui1(self):
        main_layout = QGridLayout()

        welcome_msg = QLabel("\n\n\n\n\n               Welcome!")
        welcome_msg.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))
        welcome_inst = QLabel("    Select a registration method on the\n"
        + "                  left to get started!\n\n\n\n\n\n\n")
        priority_header = QLabel("             By Priority")
        priority_header.setFont(QtGui.QFont("Arial", 10, QtGui.QFont.Bold))
        mock_sched_header = QLabel("     Upload Mock Schedule")
        mock_sched_header.setFont(QtGui.QFont("Arial", 10, QtGui.QFont.Bold))
        sched_header = QLabel("         Create Schedule")
        sched_header.setFont(QtGui.QFont("Arial", 10, QtGui.QFont.Bold))
        priority = QLabel("- List CRNS for classes you want\n"
        + "- Will log you in based on info you \n  provide\n"
        + "- Maneuvers to course registration\n"
        + "- Waits until your time card comes up\n"
        + "- Registers you for classes in order\n"
        + "- If any classes fail, will try again \n  with the next on the list!\n"
        + "- Repeats until credit limit is reached!")
        mock_sched = QLabel("- Login to grab a pre-made schedule\n"
        + "- Retrieve schedule to utilize here \n "
        + "- Set your desired schedules\n"
        + "- Select whether you want full schedule\n  priority or by class.\n"
        + "- Logs you in and maneuvers to\n  registration\n"
        + "- Will register by CRNs according to\n  specifications")
        sched = QLabel("- Make your ideal schedule/schedules\n"
        + "- Select whether you want full schedule\n  priority or by class.\n"
        + "- Logs you in according to your inputs\n"
        + "- Maneuvers you to registration\n"
        + "- Waits until your time card arrives \n "
        + "- Will register by CRNs according to\n  specifications\n")

        main_layout.addWidget(welcome_msg, 0, 1, 1, 1)
        main_layout.addWidget(welcome_inst, 1, 1, 1, 1)
        main_layout.addWidget(priority_header, 2, 0, 1, 1)
        main_layout.addWidget(mock_sched_header, 2, 1, 1, 1)
        main_layout.addWidget(sched_header, 2, 2, 1, 1)
        main_layout.addWidget(priority, 3, 0, 1, 1)
        main_layout.addWidget(mock_sched, 3, 1, 1, 1)
        main_layout.addWidget(sched, 3, 2, 1, 1)
        main = QWidget()
        main_layout.setAlignment(Qt.AlignTop)
        main.setLayout(main_layout)
        return main

    def ui2(self):
        # Need to do this in order to acces current states when we run.
        # Otherwise it will always be default values.
        global bigEditor
        global unameBox
        global passBox
        global termSelection
        global duoMethod

        # Initialize layout.
        main_layout = QGridLayout()

        # Initialize crn entry box.
        bigEditor = QTextEdit()

        # Initialize username and password boxes.
        unameBox = QLineEdit()
        passBox = QLineEdit()
        passBox.setEchoMode(QLineEdit.Password)

        # Initialize the buttons.
        runButton = QPushButton("Run")
        resetButton = QPushButton("Reset")
        scheduleButton = QPushButton("Schedule")

        # Initialize the selector boxes and set options.
        termSelection = QComboBox(self)
        termSelection.addItem("Fall 2020 Courses")
        termSelection.addItem("Spring 2021 Courses")
        termSelection.addItem("Summer 1, 2021 Courses")
        termSelection.addItem("Summer 2, 2021 Courses")
        duoMethod = QComboBox(self)
        duoMethod.addItem("Send me push notification")
        duoMethod.addItem("Call me")
        duoMethod.addItem("Enter Code")

        # Dump it all into layout.
        main_layout.addWidget(bigEditor, 0, 1, 6, 3)
        main_layout.addWidget(QLabel('Username:'), 0, 0, 1, 1)
        main_layout.addWidget(unameBox, 1, 0, 1, 1)
        main_layout.addWidget(QLabel('Password:'), 2, 0, 1, 1)
        main_layout.addWidget(passBox, 3, 0, 1, 1)
        main_layout.addWidget(termSelection, 4, 0, 1, 1)
        main_layout.addWidget(duoMethod, 5, 0, 1, 1)
        main_layout.addWidget(runButton, 6, 3, 1, 1)
        main_layout.addWidget(scheduleButton, 6, 2, 1, 1)
        main_layout.addWidget(resetButton, 6, 1, 1, 1)
        main_layout.addWidget(QLabel("This method allows you to register for "
        + "classes by listing the CRNs by priority. For the application to "
        + "read \neach CRN in order, please place one on each line like so:\n\n"
        + "8675309\n"
        + "1234567\n"
        + "1001010\n"
        + "5318008\n\n"
        + "and so on...\n\n"
        + "When you are finally ready to submit your list of courses, the app "
        + "you can press run!\n"
        + "If it is you first time running any of the methods since you opened "
        + "the application, it will prompt you to sign in.\n"
        + "The application will tell you if your time slot is up, or how much "
        + "time you have to wait. \n\nIf you keep the application running until "
        + "your time card is up, it will automatically enroll you as soon as "
        + "the website allows! :)"), 7, 0, 1, 4)

        # Set layout and alignment.
        main = QWidget()
        main_layout.setAlignment(Qt.AlignTop)
        main.setLayout(main_layout)
        self.temp_type = "priority"

        # Link buttons to functions.
        resetButton.clicked.connect(bigEditor.clear)
        runButton.clicked.connect(self.prompt_login)

        return main

    def ui3(self):
        main_layout = QGridLayout()
        main_layout.addWidget(QLabel('Feature not yet available!'))
        main = QWidget()
        main_layout.setAlignment(Qt.AlignCenter)
        main.setLayout(main_layout)
        return main

    def ui4(self):
        main_layout = QGridLayout()
        main_layout.addWidget(QLabel('Feature not yet available!'))
        main = QWidget()
        main_layout.setAlignment(Qt.AlignCenter)
        main.setLayout(main_layout)
        return main

    def ui5(self):
        main_layout = QGridLayout()

        credit_msg = QLabel("\n   Credits!\n")
        credit_msg.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Bold))
        credit_quote = QLabel("\nLife is soup, i am fork..\n"
        + "\n                              -some guy\n\n\n\n")
        allen = QLabel("        Allen West")
        allen.setFont(QtGui.QFont("Arial", 10, QtGui.QFont.Bold))
        luke = QLabel("        Luke Andrews")
        luke.setFont(QtGui.QFont("Arial", 10, QtGui.QFont.Bold))
        allen_deets = QLabel("- Github:\n  https://github.com/allenwest24\n\n"
        + "- LinkedIn:\n  https://www.linkedin.com/in/\n  allen-west-459031187/\n\n"
        + "- Email:\n  west.all@husky.neu.edu\n\n"
        + "- Current Position:\n  Cyber Security Coop, MIT Lincoln Laboratory")
        luke_deets = QLabel("- Github:\n  https://github.com/lukeandrews239\n\n"
        + "- LinkedIn:\n  https://www.linkedin.com/in/lukeandrews239/\n\n"
        + "- Email:\n  andrews.lu@husky.neu.edu\n\n"
        + "- Current Position:\n  Software Engineer Co-op, Apple")

        main_layout.addWidget(credit_msg, 0, 1, 1, 1)
        main_layout.addWidget(credit_quote, 1, 1, 1, 1)
        main_layout.addWidget(allen, 2, 0, 1, 1)
        main_layout.addWidget(luke, 2, 2, 1, 1)
        main_layout.addWidget(allen_deets, 3, 0, 1, 1)
        main_layout.addWidget(luke_deets, 3, 2, 1, 1)
        main = QWidget()
        main_layout.setAlignment(Qt.AlignTop)
        main.setLayout(main_layout)
        return main

    def prompt_login(self, crns):
        # Parse the user-given courses
        crns = bigEditor.toPlainText().split()
        username = unameBox.text()
        password = passBox.text()
        duo = str(duoMethod.currentText())
        term = str(termSelection.currentText())

        # Start doing some work son!
        popUpBox = QMessageBox()
        popUpBox.setIcon(QMessageBox.Information)
        popUpBox.setWindowTitle("Helpful Reminder")
        popUpBox.setGeometry(409, 343, 680, 500)
        popUpBox.setText("You're going to want to click stuff, DON'T.\n"
        + "The only thing you should do is respond to the duo query to your device.")
        popUpBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        x = popUpBox.exec()
        # User pressed ok.
        if (x == 1024):
            scriptRunner = ScriptRunner(username, password, crns, self.temp_type, term, duo)
            out = scriptRunner.run()
