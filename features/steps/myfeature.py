import os
import time

from behave import given, when, then
from pynput.keyboard import Controller, Key
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core import driver


@given('I launch Chrome browser')
def open_chrome(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.maximize_window()

@when('I open Greatify URL')
def open_url(context):
    context.driver.get("https://qashok.greatifystg.school/school/login")
    time.sleep(1)

@then('I enter the username and password')
def enter_credentials(context):
    context.driver.find_element(By.XPATH, "//*[@id='name1']").send_keys("HCSCHOOL0205")
    time.sleep(1)
    context.driver.find_element(By.XPATH, "//*[@placeholder='Enter Password']").send_keys("Ashok@98")
    time.sleep(1)
    context.driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()
    time.sleep(1)


@then(u'I choose an image file to upload')
def step_impl(context):
    # Adjust the XPath to match your <input type="file"> element
    context.driver.find_element(By.XPATH, "//*[@class='profile_img']").click()
    time.sleep(2)

    keyboard = Controller()
    keyboard.type("D:\\null value\\bharathiyaruniversity1.jpg")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2)

@then(u'I click the Syllabus Dropdown')
def step_impl(context):
    # Adjust the XPath to match your actual upload button
    # Locate the dropdown (by ID, NAME, or XPATH)
    dropdown_element = context.driver.find_element(By.XPATH, "//*[@class='syllabus']")  # Replace with actual ID
    time.sleep(2)
    # Create a Select object
    dropdown = Select(dropdown_element)

    # Select options in three different ways:
   # dropdown.select_by_visible_text("CBSE")  # If you know the visible name
    dropdown.select_by_value("EKV603687X0E")         # If the <option value="...">
    dropdown.select_by_index(8)                      # By position (0 = first optio
    time.sleep(2)

@then(u'I Click the Medium of School')
def step_impl(context):
    # Adjust the XPath to match your actual upload button
    # Locate the dropdown (by ID, NAME, or XPATH)
    dropdown_element = context.driver.find_element(By.XPATH, "//*[@class='medium_of_school']")  # Replace with actual ID
    time.sleep(2)
    # Create a Select object
    dropdown = Select(dropdown_element)

    # Select options in three different ways:
    # dropdown.select_by_visible_text("CBSE")  # If you know the visible name
    dropdown.select_by_value("English")  # If the <option value="...">
    dropdown.select_by_index(1)  # By position (0 = first option
    time.sleep(2)

@then(u'I enter the contact name')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//*[@class='contact_name alphabetsOnly']").send_keys("ASHOK")
    time.sleep(2)

@then(u'I enter the Phonenumber')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@class='mob_num numberOnly']").send_keys("1234500345")
    time.sleep(2)


@then(u'I enter the Website Address')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@class='web_addr']").send_keys("ashok.in")
    time.sleep(2)


@then(u'I enter the Latitude and Longitude')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@class='latitude']").send_keys("12.1234")
    context.driver.find_element(By.XPATH, "//*[@class='longitude']").send_keys("80.1234")
    time.sleep(2)

@then(u'I enter the Address line 1')
def step_impl(context):

    context.driver.find_element(By.XPATH, "//*[@class='add_line1']").send_keys("786, Anna Salai,Near Teynampet metro ")
    time.sleep(2)

@then(u'I enter the Address line 2')
def step_impl(context):

    context.driver.find_element(By.XPATH, "//*[@class='add_line2']").send_keys("Teynampet")
    time.sleep(2)

@then(u'I choose the country')
def step_impl(context):

    # Adjust the XPath to match your actual upload button
    # Locate the dropdown (by ID, NAME, or XPATH)
    dropdown_element = context.driver.find_element(By.XPATH, "//*[@class='country']")  # Replace with actual ID
    time.sleep(2)
    # Create a Select object
    dropdown = Select(dropdown_element)

    # Select options in three different ways:
    # dropdown.select_by_visible_text("CBSE")  # If you know the visible name
    dropdown.select_by_value("101")  # If the <option value="...">
    dropdown.select_by_index(101)  # By position (0 = first optio
    time.sleep(2)

@then(u'I choose the State')
def step_impl(context):

    # Adjust the XPath to match your actual upload button
    # Locate the dropdown (by ID, NAME, or XPATH)
    dropdown_element = context.driver.find_element(By.XPATH, "//*[@class='state']")  # Replace with actual ID
    time.sleep(2)
    # Create a Select object
    dropdown = Select(dropdown_element)

    # Select options in three different ways:
    # dropdown.select_by_visible_text("CBSE")  # If you know the visible name
    dropdown.select_by_value("35")  # If the <option value="...">
    dropdown.select_by_index(35)  # By position (0 = first optio
    time.sleep(2)

@then(u'I choose the city')
def step_impl(context):

    # Adjust the XPath to match your actual upload button
    # Locate the dropdown (by ID, NAME, or XPATH)
    dropdown_element = context.driver.find_element(By.XPATH, "//*[@class='city']")  # Replace with actual ID
    time.sleep(2)
    # Create a Select object
    dropdown = Select(dropdown_element)

    # Select options in three different ways:
    # dropdown.select_by_visible_text("CBSE")  # If you know the visible name
    dropdown.select_by_value("3659")  # If the <option value="...">
    dropdown.select_by_index(109)  # By position (0 = first option)
    time.sleep(2)

@then(u'I choose the pincode')
def step_impl(context):

    context.driver.find_element(By.XPATH, "//*[@class='pincode numberOnly']").send_keys(600019)
    time.sleep(2)

@then(u'I selected for next step 2')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@class='Continue-btn cont-btn-1 school_details']").click()
    time.sleep(2)

#step 2

@then(u'I choose Onboard subject file')
def step_impl(context):
    # Adjust the XPath to match your <input type="file"> element
    context.driver.find_element(By.XPATH, "(//*[@class='upload_filed'])[1]").click()
    time.sleep(2)

    keyboard = Controller()
    keyboard.type("D:\\KANGUVA\\SubjectCsv.csv")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2)
    # after upload - click ok
    context.driver.find_element(By.XPATH, "//*[@class='swal-button-container']").click()
    time.sleep(2)
    # next step
    context.driver.find_element(By.XPATH, "//*[@class='Continue-btn cont-btn-2 cont_btn_sub']").click()
    time.sleep(2)


@then(u'I choose Onboard teacher file')
def step_impl(context):
    # Adjust the XPath to match your <input type="file"> element
    context.driver.find_element(By.XPATH, "(//*[@class='upload_filed'])[2]").click()
    time.sleep(2)

    keyboard = Controller()
    keyboard.type("D:\\KANGUVA\\TeacherCsv.csv")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2)
    # after upload - click ok
    context.driver.find_element(By.XPATH, "//*[@class='swal-button-container']").click()
    time.sleep(2)
    # next step
    context.driver.find_element(By.XPATH, "//*[@class='Continue-btn cont-btn-3 cont_btn_teacher']").click()
    time.sleep(2)

@then(u'I choose Onboard class file')
def step_impl(context):
    # Adjust the XPath to match your <input type="file"> element
    context.driver.find_element(By.XPATH, "(//*[@class='upload_filed'])[3]").click()
    time.sleep(2)

    keyboard = Controller()
    keyboard.type('D:\\KANGUVA\\ClassCsv.csv')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2)
    # after upload - click ok
    context.driver.find_element(By.XPATH, "//*[@class='swal-button-container']").click()
    time.sleep(2)
    # next step
    context.driver.find_element(By.XPATH, "//*[@class='Continue-btn cont-btn-4 cont_btn_class']").click()
    time.sleep(2)

@then(u'I choose Onboard Student file')
def step_impl(context):
    # Adjust the XPath to match your <input type="file"> element
    context.driver.find_element(By.XPATH, "(//*[@class='upload_filed'])[4]").click()
    time.sleep(2)

    keyboard = Controller()
    keyboard.type('D:\\KANGUVA\\StudentCsv_new.csv')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2)
    # after upload - click ok
    context.driver.find_element(By.XPATH, "//*[@class='swal-button-container']").click()
    time.sleep(10)
    # next step
    context.driver.find_element(By.XPATH, "//*[@class='Continue-btn submit']").click()
    time.sleep(30)

@then(u'Onboarded Successfully')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@class='Credentials_btn']").click()
    time.sleep(10)

