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
    def __init__(self, username, password, CRNs, type, term):
        self.username = username
        self.password = password
        self.crns = CRNs
        self.type = type
        self.term = term

    # Called from the UI
    def run(self):
        # Add the chromedriver
        chromedriver = r"C:\Users\Allen\Desktop\NU-AIR\src\main\resources\base\chromedriver"
        # TODO: Allen - figure out how to get_resource for the chromedriver.
        #chromedriver = self.get_resource('chromedriver')
        driver = webdriver.Chrome(chromedriver)
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
        # TODO: Allen - allow for user to use any of the three types of duo notifications.
        # Handle sending a duo push messahe for dual verification.
        WebDriverWait(webdriver, 5)
        driver.switch_to.frame("duo_iframe")
        send_push = driver.find_element_by_xpath('//*[@id="auth_methods"]/fieldset/div[1]/button')
        send_push.click()
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

    # The "by priority list" version of the script.
    def runPriorityScript(self, driver):
        # Send us to the registration screen.
        driver.get("https://nubanner.neu.edu/StudentRegistrationSsb")
        # Get to the select term screen.
        register_for_classes = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID,'registerLink')))
        register_for_classes.click()
        WebDriverWait(driver, 5)
        term_selector = driver.find_element_by_xpath("/html/body/main/div[3]/div/div/div[2]/div[1]/fieldset/div[2]/div[1]/div[1]/a/span[2]/b")
        term_selector.click()
        # These are all my sad attempts.
        #term_input = driver.find_element_by_xpath("/html/body/div[5]/ul/li[1]")
        #term_input.click()
        #term_input = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID,'s2id_autogen1_search')))
        #term_input.sendKeys("dfhfgh")
        #term_selector = driver.find_element_by_xpath("/html/body/div[5]/ul")
        #term_selector.select()
