# To utilize command line arguments.
import argparse
# To utilize email functionality.
import smtplib
# To utilize session requests.
import requests

# Prompt user for login credentials.
myNortheasternUsername = input("Please enter your myNortheastern Username: ")
myNortheasternPassword = input("Please enter your myNortheastern Password: ")

# Try to login
url = "https://neuidmsso.neu.edu/idp/profile/SAML2/POST/SSO?execution=e2s1"
session_requests = requests.session()
result = session_requests.get(url)

# TODO: Allen - remove print check.
print(myNortheasternUsername)
print(myNortheasternPassword)
print(result)
