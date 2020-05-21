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

# Class that will handle the CRN priority registering version of the application.
class ScriptRunner:
    def __init__(self, username, password, CRNs, type, term, duo):
        self.username = username
        self.password = password
        self.crns = CRNs
        self.type = type
        self.term = term
        self.duo = duo

    # Called from the UI
    def run(self):
        # Add the chromedriver
        chromedriver = r"C:\Users\Allen\Desktop\NU-AIR\src\main\resources\base\chromedriver"
        print("3")
        # TODO: Allen - figure out how to get_resource for the chromedriver.
        #chromedriver = self.get_resource('chromedriver')
        driver = webdriver.Chrome(chromedriver)
        print("4")
        self.login(driver)
        if (self.type == "priority"):
            self.runPriorityScript(driver)

    # Logs the user in, then opens a new tab to maneuver to the destination easier
    def login(self, driver):
        driver.get("https://my.northeastern.edu/")
        # Click on the go to login screeen button.
        go_to_login = driver.find_elements_by_xpath('//*[@id="portlet_com_liferay_journal_content_web_portlet_JournalContentPortlet_INSTANCE_GhAIpHlwoE3O"]/div/div/div/div[2]/div/div[2]/div/a')[0]
        go_to_login.click()
        # TODO: Allen - replace the placeholder input with the user-given stuff
        # Fill the boxes with the given username and password.
        username_box = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID,'username')))
        username_box.send_keys(self.username)
        password_box = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID,'password')))
        password_box.send_keys(self.password)
        # Click the login button.
        login = driver.find_elements_by_xpath("/html/body/section/div/div[1]/div/form/div[3]/button")[0]
        login.click()
        WebDriverWait(webdriver, 5)
        self.sendDuoCheck(driver)
        WebDriverWait(driver, 10)
        # Get back the main frame back from the duo frame.
        driver.switch_to.default_content()
        WebDriverWait(driver, 10)
        # Open another tab at google.
        driver.execute_script("window.open('https://google.com','_blank')")
        driver.switch_to.window(driver.window_handles[0])
        # Wait until the duo situation gets solved and pushes us to the next screen.
        while (driver.current_url == "https://neuidmsso.neu.edu/idp/profile/SAML2/POST/SSO?execution=e1s3"):
            time.sleep(1)
        # Go to the new tab and use the credible session in the other tab to do whatever we want in this tab.
        driver.switch_to.window(driver.window_handles[1])

    # Depending on what duo you have set up this will allow you to select the proper choice.
    def sendDuoCheck(self, driver):
        driver.switch_to.frame("duo_iframe")
        if self.duo == "Send me push notification":
            send_push = driver.find_element_by_xpath('//*[@id="auth_methods"]/fieldset/div[1]/button')
        elif self.duo == "Call me":
            send_push = driver.find_element_by_xpath('//*[@id="auth_methods"]/fieldset/div[2]/button')
        elif self.duo == "Enter Code":
            send_push = driver.find_element_by_xpath('//*[@id="auth_methods"]/fieldset/div[3]/button')
        send_push.click()

    # The "by priority list" version of the script.
    def runPriorityScript(self, driver):
        # Send us to the registration screen.
        driver.get("https://nubanner.neu.edu/StudentRegistrationSsb")
        # Get to the select term screen.
        register_for_classes = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID,'registerLink')))
        register_for_classes.click()
        self.selectTerm(driver)
        self.registerAll(driver)

    # Select term
    def selectTerm(self, driver):
        term_selector = driver.find_element_by_xpath("/html/body/main/div[3]/div/div/div[2]/div[1]/fieldset/div[2]/div[1]/div[1]/a/span[1]")
        term_selector.click()
        # TODO - Allen - make this into a switch for all the different terms you are allowed to select.
        fall = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID,'202110')))
        fall.click()
        submit = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID,'term-go')))
        submit.click()

    # The actual 'algorithm' work for registering the crns.
    def registerAll(self, driver):
        # Switch to the easiest tab to enter in this info.
        crnTab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,'enterCRNs-tab')))
        crnTab.click()
        # Actual parsing through the user-entered crns.
        ii = 1
        while ii <= len(self.crns):
            # Click on the crn entry box.
            txt_crn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID,"txt_crn" + str(ii))))
            txt_crn.click()
            # Send current top-priority crn.
            txt_crn.send_keys(self.crns[ii - 1])
            # If we are going to want another one, click the button to add another entry box.
            # If not, don't.
            if ii < len(self.crns):
                add_another = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID,"addAnotherCRN")))
                add_another.click()
            # Inrement through the provided crns.
            ii += 1
