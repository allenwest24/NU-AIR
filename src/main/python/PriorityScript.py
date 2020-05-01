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
        # Add the chromedriver
        chromedriver = r"C:\Users\Allen\Desktop\src\main\resources\base\chromedriver"
        # TODO: Allen - figure out how to get_resource for the chromedriver.
        #chromedriver = self.get_resource('chromedriver')
        driver = webdriver.Chrome(chromedriver)
        #driver.get("http:google.com")
        self.login(driver)

    # Drvier is initialized during run()
    def login(self, driver):
        driver.get("https://my.northeastern.edu/")
        # TBD below.
        #driver.find_element_by_id("email").send_keys("username")
        #driver.find_element_by_id("pass").send_keys("password")
        #iver.find_element_by_id("loginbutton").click()
