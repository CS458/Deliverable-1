from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def test_error_message(input, expected_error):
    passed = False
    identifier, password = input
    driver = webdriver.Chrome()

    driver.get("http://127.0.0.1:5000/")
    time.sleep(3)

    identifier_input = driver.find_element("name", "identifier")
    password_input = driver.find_element("name", "password")

    identifier_input.send_keys(identifier)
    password_input.send_keys(password)

    submit_button = driver.find_element("name", "submit")
    submit_button.click()

    driver.implicitly_wait(10)
    time.sleep(3)

    error_element = driver.find_element("id", "message")
    error_message = error_element.get_attribute("innerHTML")

    if error_message == expected_error:
        passed = True

    driver.quit()

    return passed

def test_success_credentials(input):
    passed = False
    driver = webdriver.Chrome()
    identifier, password = input


    driver.get("http://127.0.0.1:5000/")
    time.sleep(3)

    identifier_input = driver.find_element("name", "identifier")
    password_input = driver.find_element("name", "password")

    identifier_input.send_keys(identifier)
    password_input.send_keys(password)

    submit_button = driver.find_element("name", "submit")
    submit_button.click()

    driver.implicitly_wait(10)
    time.sleep(3)

    if "http://127.0.0.1:5000/success" in driver.current_url:
        passed = True

    driver.quit()

    return passed

def test_google():
    passed = False
    driver = webdriver.Chrome()

    driver.get("http://127.0.0.1:5000/")
    time.sleep(3)


    submit_button = driver.find_element("css", "css=form:nth-child(2) > #submit")
    submit_button.click()

    submit_button = driver.find_element("css", "css=.wLBAL")
    submit_button.click()

    driver.implicitly_wait(10)
    time.sleep(3)


    if "http://127.0.0.1:5000/success" in driver.current_url:
        passed = True

    driver.quit()

    return passed

if __name__=="__main__":
    #4.1.1 Valid Credentials with Phone
    if test_success_credentials(("+905540244745", "1234$cdA6578")):
        print("4.1.1 PASSED")

    else:
        print("4.1.1 FAILED")

    #4.1.2 Valid Credentials with email
    if test_success_credentials(("sahandmoslemi@gmail.com", "1234#@!%!6578")):
        print("4.1.2 PASSED")

    else:
        print("4.1.2 FAILED")

    #4.2.1 Invalid Identifier with email
    if test_error_message(("erengazi@gmail.com", "12SA2d1S$"), "Credentials are not correct."):
        print("4.2.1 PASSED")

    else:
        print("4.2.1 FAILED")
    
    #4.2.2 Invalid Identifier with phone
    if test_error_message(("+94351544745", "12SA2d1S$"), "Credentials are not correct."):
        print("4.2.2 PASSED")

    else:
        print("4.2.2 FAILED")

    #4.2.3 Valid email with wrong password 
    if test_error_message(("sahandmoslemi@gmail.com", "12SA2d1S$"), "Credentials are not correct."):
        print("4.2.3 PASSED")

    else:
        print("4.2.3 FAILED")

    #4.2.4 Valid password with wrong password 
    if test_error_message(("+905540244745", "12SA2d1S$"), "Credentials are not correct."):
        print("4.2.4 PASSED")

    else:
        print("4.2.4 FAILED")

    #4.3. Empty email/phone or password
    if test_error_message(("+905540244745", ""), "All the fields are required."):
        print("4.3.1 PASSED")

    else:
        print("4.3.1 FAILED")

    if test_error_message(("", "12345678"), "All the fields are required."):
        print("4.3.2 PASSED")

    else:
        print("4.3.2 FAILED")

    #4.4 Invalid format phone/email
    if test_error_message(("540244745", "13246"), "The phone number or email has not a valid format."):
        print("4.4.1 PASSED")

    else:
        print("4.4.1 FAILED")

    if test_error_message(("sahandmoslemi#gmail.com", "13246"), "The phone number or email has not a valid format."):
        print("4.4.2 PASSED")

    else:
        print("4.4.2 FAILED")

    #4.5. Google authentication
    if test_google():
        print("4.5 PASSED")

    else:
        print("4.5 FAILED")
