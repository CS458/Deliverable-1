from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Create a new instance of the Firefox driver
driver = webdriver.Chrome()

# Open the login webpage
driver.get("http://127.0.0.1:5000/")
time.sleep(2)

# Find the input fields by their name attribute and enter your credentials
identifier_input = driver.find_element("name", "identifier")
password_input = driver.find_element("name", "password")

# Enter your username and password
identifier_input.send_keys("sahandmoslemi@gmail.com")
password_input.send_keys("12345678")

# Find and click the submit button
submit_button = driver.find_element("name", "submit")
submit_button.click()

# Wait for the page to load (you can use WebDriverWait for more complex cases)
driver.implicitly_wait(10)

time.sleep(2)


# Check if login was successful (you can assert on some element presence or URL)
if "http://127.0.0.1:5000/success" in driver.current_url:
    print("Login successful!")
else:
    print("Login failed!")

# Close the browser
driver.quit()