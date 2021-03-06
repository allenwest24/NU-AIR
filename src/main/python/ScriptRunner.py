# PyQt5 imports
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# Selenium imports.
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
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
        # With this new import using the ChromeDriverManager we no longer need
        # to manually go in and update the ChromeDriver every time a new one is
        # available. Just run 'pip install webdriver-manager' before using
        # this code. ChromeDriverManager is unreal.
        driver = webdriver.Chrome(ChromeDriverManager().install())
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
        switcher = {
            "Send me push notification": driver.find_element_by_xpath('//*[@id="auth_methods"]/fieldset/div[1]/button'),
            "Call me": driver.find_element_by_xpath('//*[@id="auth_methods"]/fieldset/div[2]/button'),
            "Enter Code": driver.find_element_by_xpath('//*[@id="auth_methods"]/fieldset/div[3]/button')
        }
        send_push = switcher.get(self.duo, None)
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
    # TODO: Allen - A major todo here will be the fact that we need to wait until the user is able to register and only THEN go past this point.
    def selectTerm(self, driver):
        term_selector = driver.find_element_by_xpath("/html/body/main/div[3]/div/div/div[2]/div[1]/fieldset/div[2]/div[1]/div[1]/a/span[1]")
        term_selector.click()
        # TODO - Allen - Fix it to the actual terms available
        switcher = {
            "Fall 2020 Semester": WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID,'202110'))),
            "Fall 2020 CPS Quarter": WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID,'202115'))),
            "Fall 2020 CPS Semester": WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID,'202114'))),
        }
        term = switcher.get(self.term, None)
        term.click()
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
        add2Sum = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,'addCRNbutton')))
        add2Sum.click()
        saveButt = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,'saveButton')))
        saveButt.click()
