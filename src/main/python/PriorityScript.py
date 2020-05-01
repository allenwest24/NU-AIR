# PyQt5 imports
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# Selenium imports.
from selenium import webdriver

# Standard Python imports.
import sys
import os

# Class that will handle the CRN priority registering version of the application.
class PriorityScript:
    def __init__(self, username, password, CRNs):
        self.username = username
        self.password = password
        self.crns = CRNs

    # Called from the UI
    def run(self):
        # Have to add a chromedriver.
        driver = webdriver.Chrome()
        print("getting stuck here")
        #self.login(driver)

    # Drvier is initialized during run()
    def login(self, driver):
        driver.get ("https://neuidmsso.neu.edu/idp/profile/SAML2/POST/SSO?execution=e1s2")
        driver.find_element_by_id("email").send_keys("username")
        driver.find_element_by_id("pass").send_keys("password")
        iver.find_element_by_id("loginbutton").click()
