from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Gmail credentials
GMAIL_USER = "automate61@gmail.com"
GMAIL_PASS = "Automation1221"

# Initialize the Firefox WebDriver
driver = webdriver.Firefox()

try:
    # Step 1: Open Gmail
    driver.get("https://mail.google.com/")

    # Step 2: Enter email and proceed
    email_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))
    )
    email_field.send_keys(GMAIL_USER)
    email_field.send_keys(Keys.RETURN)
    time.sleep(2)

    # Step 3: Enter password and proceed
    password_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='password']"))
    )
    password_field.send_keys(GMAIL_PASS)
    password_field.send_keys(Keys.RETURN)
    time.sleep(5)

    # Step 4: Wait for inbox to load
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "zA"))
    )
    print("Successfully logged into Gmail!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    time.sleep(5)
    driver.quit()