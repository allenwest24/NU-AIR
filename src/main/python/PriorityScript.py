# PyQt5 imports
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# Selenium imports.
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Standard Python imports.
import sys
import os
import time

PASS = "password"

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
        self.login(driver)

    # Driver is initialized during run()
    def login(self, driver):
        driver.get("https://my.northeastern.edu/")
        go_to_login = driver.find_elements_by_xpath('//*[@id="portlet_com_liferay_journal_content_web_portlet_JournalContentPortlet_INSTANCE_GhAIpHlwoE3O"]/div/div/div/div[2]/div/div[2]/div/a')[0]
        go_to_login.click()
        # TODO: Allen - replace the placeholder input with the user-given stuff
        username_box = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID,'username')))
        username_box.send_keys("west.all")
        password_box = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID,'password')))
        password_box.send_keys(PASS)
        print("hello)")
        login = driver.find_elements_by_xpath("/html/body/section/div/div[1]/div/form/div[3]/button")[0]
        login.click()
        WebDriverWait(webdriver, 5)
        driver.switch_to.frame("duo_iframe")
        send_push = driver.find_element_by_xpath('//*[@id="auth_methods"]/fieldset/div[1]/button')
        send_push.click()
        WebDriverWait(driver, 10)
        driver.switch_to.default_content()
        WebDriverWait(driver, 10)
        driver.execute_script("window.open('https://google.com','_blank')")
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(10)
        print("Got here1")
        driver.switch_to.window(driver.window_handles[1])
        driver.get("https://nubanner.neu.edu/StudentRegistrationSsb")

    def link_has_gone_stale(self, driver):
        try:
            # poll the link with an arbitrary call
            driver.find_elements_by_id('mail')
            return False
        except StaleElementReferenceException:
            return True
