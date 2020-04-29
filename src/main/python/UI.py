from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class UI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "NU-AIR (NU-And-Improved-Registration)"
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
        main_layout = QGridLayout()
        main_layout.addWidget(QLabel('Feature not yet available!'))
        main = QWidget()
        main_layout.setAlignment(Qt.AlignCenter)
        main.setLayout(main_layout)
        return main

    def ui2(self):
        main_layout = QGridLayout()
        bigEditor = QTextEdit()
        runButton = QPushButton("Run")
        main_layout.addWidget(bigEditor, 0, 1, 5, 4)
        main_layout.addWidget(QPushButton("Clear"), 0, 0, 1, 1)
        main_layout.addWidget(QPushButton("Check"), 1, 0, 1, 1)
        main_layout.addWidget(QPushButton("Save"), 2, 0, 1, 1)
        main_layout.addWidget(runButton, 3, 0, 1, 1)
        main_layout.addWidget(QLabel('\n'), 4, 0, 1, 1)
        main_layout.addWidget(QLabel('\n'), 5, 0, 1, 1)
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
        + "the website allows! :)"), 6, 0, 1, 4)
        main = QWidget()
        main_layout.setAlignment(Qt.AlignTop)
        main.setLayout(main_layout)
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
        main_layout.addWidget(QLabel('Feature not yet available!'))
        main = QWidget()
        main_layout.setAlignment(Qt.AlignCenter)
        main.setLayout(main_layout)
        return main

    def prompt_login(self):
        loginBox = QMessageBox()
        loginBox.setWindowTitle("Login to MyNEU")
        loginBox.setGeometry(409, 343, 680, 500)
        loginBox.setText('This shit has been giving me such a hard time')

        #username_label = QLabel("Username")
        #loginBox.lineEdit_username = QLineEdit()
        #loginBox.addWidget(username_label)
        #loginBox.addWidget(loginBox.lineEdit_username)
        #loginBox.lineEdit_username.setPlaceHolderText("Please enter your MyNEU "
        #+ "username.")
        #layout.addWidget(username_label, 0, 0)
        #layout.addWidget(loginBox.lineEdit_username, 0, 1)

        #password_label = QLabel("Password")
        #loginBox.lineEdit_password = QLineEdit()
        #loginBox.lineEdit_passwrod.setPlaceHolderText("Please enter your MyNEU "
        #+ "password.")
        #layout.addWidget(password_label, 1, 0)
        #layout.addWidget(loginBox.lineEdit_password, 1, 1)

        #button_login = QPushButton('Login')
        #button_login.clicked.connect(self.check_password)
        #layout.addWidget(button_login, 2, 0, 1, 2)
        #layout.setRowMinimumHeight(2, 75)

        #self.setLayout(layout)

    #def check_password(self):
        #pass
        
        x = loginBox.exec()
