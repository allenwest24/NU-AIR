# PyQt5 imports
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# Standard Python imports.
import sys
import os

# Class that will handle the CRN priority registering version of the application.
class PriorityScript:
    def __init__(self, username, password, CRNs):
        self.username = username
        self.password = password
        self.crns = CRNs
