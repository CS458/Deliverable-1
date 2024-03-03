from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Initialize the webdriver (choose your preferred browser)
driver = webdriver.Chrome()

# Open the login page
driver.get("https://yourloginpage.com")

# Find the username and password fields and enter your credentials
username_field = driver.find_element_by_name("username")
password_field = driver.find_element_by_name("password")

username_field.send_keys("your_username")
password_field.send_keys("your_password")

# Submit the form
password_field.send_keys(Keys.RETURN)

# You can add assertions or checks here to verify if the login was successful
# For example, you can check if a certain element is present on the next page after login

# Close the webdriver
driver.quit()