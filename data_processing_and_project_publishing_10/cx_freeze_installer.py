# Below is an example of a code to log in.
# To use CX-Freeze. just put in the terminal
# cxfreeze path/path/path
# click on the app inside the generated folder to run the code

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# Start the webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 1 - Navigate to https://automatize.netlify.app/
driver.get('https://automatize.netlify.app')
sleep(2)

# Find the email field element
email_field = driver.find_element(By.ID, 'email')
sleep(2)

# 2 - Click on the email field
email_field.click()
sleep(2)

# 3 - Type an email
email_field.send_keys('jhonatanf@hotmail.com')
sleep(2)

# Find password field
password_field = driver.find_element(By.XPATH, "//input[@type='password']")
sleep(2)

# 4 - Click on the password field
password_field.click()
sleep(2)

# 5 - Type a password
password_field.send_keys('123456')
sleep(2)
