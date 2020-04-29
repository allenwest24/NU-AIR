from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import sys
import os

class PriorityScript:
    def __init__(self, username, password, CRNs):
        self.username = username
        self.password = password
        self.crns = CRNs
